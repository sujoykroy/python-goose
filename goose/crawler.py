# -*- coding: utf-8 -*-
"""\
This is a python port of "Goose" orignialy licensed to Gravity.com
under one or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.

Python port was written by Xavier Grangier for Recrutae

Gravity.com licenses this file
to you under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os
import re
import glob
import urllib
import json

from copy import deepcopy
from goose.article import Article
from goose.sub_article import SubArticle
from goose.utils import URLHelper, RawHelper
from goose.extractors.content import StandardContentExtractor
from goose.extractors.videos import VideoExtractor
from goose.extractors.title import TitleExtractor
from goose.extractors.images import ImageExtractor
from goose.extractors.links import LinksExtractor
from goose.extractors.tweets import TweetsExtractor
from goose.extractors.authors import AuthorsExtractor
from goose.extractors.tags import TagsExtractor
from goose.extractors.opengraph import OpenGraphExtractor
from goose.extractors.publishdate import PublishDateExtractor
from goose.extractors.metas import MetasExtractor
from goose.extractors.microdata import MicroDataExtractor
from goose.extractors.hcard import HCardExtractor
from goose.cleaners import StandardDocumentCleaner
from goose.outputformatters import StandardOutputFormatter

from goose.network import HtmlFetcher

import goose.text


class CrawlCandidate(object):

    def __init__(self, config, url, raw_html, doc=None):
        self.config = config
        # parser
        self.parser = self.config.get_parser()
        self.url = url
        self.raw_html = raw_html
        self.doc = doc

class Crawler(object):

    def __init__(self, config):
        # config
        self.config = config
        # parser
        self.parser = self.config.get_parser()

        # article
        self.article = Article()

        # init the extractor
        self.extractor = self.get_extractor()

        # init the document cleaner
        self.cleaner = self.get_cleaner()

        # init the output formatter
        self.formatter = self.get_formatter()

        # metas extractor
        self.metas_extractor = self.get_metas_extractor()

        # publishdate extractor
        self.publishdate_extractor = self.get_publishdate_extractor()

        # opengraph extractor
        self.opengraph_extractor = self.get_opengraph_extractor()

        # tags extractor
        self.tags_extractor = self.get_tags_extractor()

        # authors extractor
        self.authors_extractor = self.get_authors_extractor()

        # tweets extractor
        self.tweets_extractor = self.get_tweets_extractor()

        # links extractor
        self.links_extractor = self.get_links_extractor()

        # video extractor
        self.video_extractor = self.get_video_extractor()

        # title extractor
        self.title_extractor = self.get_title_extractor()

        # image extrator
        self.image_extractor = self.get_image_extractor()

        #microdata extractor
        self.microdata_extractor = self.get_microdata_extractor();

        #hCard extractor
        self.hcard_extractor = self.get_hcard_extractor();

        # html fetcher
        htmlfetcher_class = config.htmlfetcher_class
        if not htmlfetcher_class:
            htmlfetcher_class = HtmlFetcher

        self.htmlfetcher = htmlfetcher_class(self.config)

        # TODO : log prefix
        self.logPrefix = "crawler:"

    def crawl(self, crawl_candidate, crawl_sub=True):
        # parser candidate
        parse_candidate = self.get_parse_candidate(crawl_candidate)

        if self.config.logger:
            self.config.logger.info('crawl begins. crawl_sub={0}'.format(crawl_sub))

        if crawl_candidate.doc is None:
            # raw html
            raw_html = self.get_html(crawl_candidate, parse_candidate)

            if raw_html is None:
                return self.article

            # create document
            doc = self.get_document(raw_html)
        else:
            doc = crawl_candidate.doc
            raw_html = None

        # article
        self.article.final_url = parse_candidate.url
        self.article.site_domain =  goose.text.get_site_domain(parse_candidate.url)
        self.article.link_hash = parse_candidate.link_hash
        self.article.raw_html = raw_html
        self.article.doc = doc
        self.article.raw_doc = deepcopy(doc)

        # open graph
        self.article.opengraph = self.opengraph_extractor.extract()

        # publishdate
        self.article.publish_date = self.publishdate_extractor.extract()

        # meta
        metas = self.metas_extractor.extract()
        self.article.meta_lang = metas['lang']
        self.article.meta_favicon = metas['favicon']
        self.article.meta_description = metas['description']
        self.article.meta_keywords = metas['keywords']
        self.article.canonical_link = metas['canonical']
        self.article.domain = metas['domain']
        self.article.metatags = metas['metatags']

        # tags
        self.article.tags = self.tags_extractor.extract()

        #Parse json ld
        json_ld_tags = self.parser.xpath_re(
            self.article.doc, 'descendant::script[@type="application/ld+json"]')
        if json_ld_tags:
            json_ld_text = self.parser.getText(json_ld_tags[0])
            for i in range(2):
                try:
                    self.article.json_ld = json.loads(json_ld_text)
                except Exception as ex:
                    if i == 0:
                        json_ld_text = json_ld_text.replace('""', '", "')

        # check for known node as content body
        # if we find one force the article.doc to be the found node
        # this will prevent the cleaner to remove unwanted text content
        if crawl_sub:
            self.article_body = self.extractor.get_known_article_tags()
        else:
            self.article_body = doc

        if self.article_body is not None:
            self.article.doc = self.article_body

        self.article.doc = self.cleaner.remove_nested_article_tags(self.article.doc)

        #microdata
        self.article.microdata = self.microdata_extractor.extract()

        # authors
        self.article.authors = self.authors_extractor.extract()

        # title
        self.article.title = self.title_extractor.extract()

        for sub_article in self.article.sub_articles:
            if sub_article.node == self.article.doc:
                continue
            self.parser.remove(sub_article.node)

        #hcard
        self.article.hcards = self.hcard_extractor.extract()

        self.article.read_more_url = self.links_extractor.extract_read_more()

        # before we do any calcs on the body itself let's clean up the document
        self.article.doc = self.cleaner.clean()

        # big stuff
        self.article.top_node = self.extractor.calculate_best_node()
        if self.article.top_node is None:
            self.article.top_node = self.article.doc

        # if we have a top node
        # let's process it
        if self.article.top_node is not None:
            # article links
            self.article.links = self.links_extractor.extract()
            self.article.html_links = self.links_extractor.extract_html_links()

            # tweets
            self.article.tweets = self.tweets_extractor.extract()

            # video handling
            self.video_extractor.get_videos()

            # image handling
            if self.config.enable_image_fetching:
                self.get_image()

            # post cleanup
            if crawl_sub:
                self.article.top_node = self.extractor.post_cleanup()

            # clean_text
            self.article.cleaned_text = self.formatter.get_formatted_text(
                remove_fewwords=crawl_sub)
        # cleanup tmp file
        self.release_resources()
        if crawl_sub and len(self.article.sub_articles) > 1:
            active_sub_articles = []
            for i in range(len(self.article.sub_articles)):
                sub_article = self.article.sub_articles[i]
                if sub_article.node == self.article.doc:
                    continue
                crawler = Crawler(self.config)
                if self.config.logger:
                    self.config.logger.info('sub-crawl for index: {0}'.format(i))
                crawled_article = crawler.crawl(
                    CrawlCandidate(
                        self.config, None, raw_html=sub_article.outer_html),
                    crawl_sub=False
                )
                sub_article.crawled_article = crawled_article
                active_sub_articles.append(sub_article)

            del self.article.sub_articles[:]
            self.article.sub_articles.extend(active_sub_articles)

        # return the article
        if self.config.logger:
            self.config.logger.info('crawl ends. crawl_sub={0}'.format(crawl_sub))
        if crawl_sub and self.article.sub_articles:
            self.article.sub_articles.sort(
                    key=lambda obj: -len(obj.cleaned_text))
            if not self.article.cleaned_text and \
               self.article.sub_articles[0].crawled_article:
                self.article.cleaned_text = \
                    self.article.sub_articles[0].crawled_article.cleaned_text
            if not self.article.authors:
                self.article.authors = \
                    self.article.sub_articles[0].authors
        return self.article

    def get_parse_candidate(self, crawl_candidate):
        if crawl_candidate.doc is not None:
            return SubArticle.get_parsing_candidate(crawl_candidate.doc)
        if crawl_candidate.raw_html:
            return RawHelper.get_parsing_candidate(crawl_candidate.url, crawl_candidate.raw_html)
        return URLHelper.get_parsing_candidate(crawl_candidate.url)

    def get_image(self):
        doc = self.article.raw_doc
        top_node = self.article.top_node
        self.article.top_image = self.image_extractor.get_best_image(doc, top_node)

    def get_html(self, crawl_candidate, parsing_candidate):
        # we got a raw_tml
        # no need to fetch remote content
        if crawl_candidate.raw_html:
            return crawl_candidate.raw_html

        # fetch HTML
        html = self.htmlfetcher.get_html(parsing_candidate.url)
        if not html:
            html = ""
        crawl_candidate.raw_html = html

        #Twitter/Facebook specific news crawling. Should be transferred to separate module.
        site_domain = goose.text.get_site_domain(parsing_candidate.url)
        if site_domain == "twitter.com":
            doc = self.parser.fromstring(html)
            a_links = self.parser.getElementsByTag(
                doc, tag='a', attr='class', value='twitter-timeline-link')
            if a_links:
                parsing_candidate.url = self.parser.getAttribute(a_links[0], 'href')
                html = self.htmlfetcher.get_html(parsing_candidate.url)
                crawl_candidate.raw_html = html
        elif site_domain == "www.facebook.com" and "/posts/" in parsing_candidate.url:
            html = html.replace("<!--", "")
            html = html.replace("-->", "")
            doc = self.parser.fromstring(html)
            a_links = self.parser.xpath_re(
                doc, "//*[@class='hidden_elem']/descendant::a")

            link_re = re.compile(r"https?://l\.facebook\.com/l\.php\?u=(?P<url>[^&]+)&h")
            for a_link in a_links:
                href = a_link.attrib.get('href')
                match = link_re.search(href)
                if match:
                    url = match.groupdict()["url"]
                    parsing_candidate.url = urllib.unquote(url)
                    html = self.htmlfetcher.get_html(parsing_candidate.url)
                    crawl_candidate.raw_html = html
                    break

        self.article.additional_data.update({
            'request': self.htmlfetcher.request,
            'result': self.htmlfetcher.result,
            })
        return html

    def get_metas_extractor(self):
        return MetasExtractor(self.config, self.article)

    def get_publishdate_extractor(self):
        return PublishDateExtractor(self.config, self.article)

    def get_opengraph_extractor(self):
        return OpenGraphExtractor(self.config, self.article)

    def get_tags_extractor(self):
        return TagsExtractor(self.config, self.article)

    def get_authors_extractor(self):
        return AuthorsExtractor(self.config, self.article)

    def get_tweets_extractor(self):
        return TweetsExtractor(self.config, self.article)

    def get_links_extractor(self):
        return LinksExtractor(self.config, self.article)

    def get_title_extractor(self):
        return TitleExtractor(self.config, self.article)

    def get_image_extractor(self):
        return ImageExtractor(self.config, self.article)

    def get_video_extractor(self):
        return VideoExtractor(self.config, self.article)

    def get_microdata_extractor(self):
        return MicroDataExtractor(self.config, self.article)

    def get_hcard_extractor(self):
        return HCardExtractor(self.config, self.article)

    def get_formatter(self):
        return StandardOutputFormatter(self.config, self.article)

    def get_cleaner(self):
        return StandardDocumentCleaner(self.config, self.article)

    def get_document(self, raw_html):
        doc = self.parser.fromstring(raw_html)
        return doc

    def get_extractor(self):
        return StandardContentExtractor(self.config, self.article)

    def release_resources(self):
        if self.config.file_handler:
            self.config.file_handler.release_resources()
        else:
            path = os.path.join(self.config.local_storage_path, '%s_*' % self.article.link_hash)
            for fname in glob.glob(path):
                try:
                    os.remove(fname)
                except OSError:
                    # TODO better log handeling
                    pass
