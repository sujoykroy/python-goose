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
import glob
from copy import deepcopy
from goose.article import Article
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


class CrawlCandidate(object):

    def __init__(self, config, url, raw_html):
        self.config = config
        # parser
        self.parser = self.config.get_parser()
        self.url = url
        self.raw_html = raw_html


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

    def crawl(self, crawl_candidate):

        # parser candidate
        parse_candidate = self.get_parse_candidate(crawl_candidate)

        # raw html
        raw_html = self.get_html(crawl_candidate, parse_candidate)

        if raw_html is None:
            return self.article

        # create document
        doc = self.get_document(raw_html)

        # article
        self.article.final_url = parse_candidate.url
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

        # authors
        self.article.authors = self.authors_extractor.extract()

        # title
        self.article.title = self.title_extractor.extract()

        self.article.microdata = self.microdata_extractor.extract()
        self.article.hcards = self.hcard_extractor.extract()

        # check for known node as content body
        # if we find one force the article.doc to be the found node
        # this will prevent the cleaner to remove unwanted text content
        self.article_body = self.extractor.get_known_article_tags()
        if self.article_body is not None:
            self.article.doc = self.article_body

        # before we do any calcs on the body itself let's clean up the document
        self.article.doc = self.cleaner.clean()
        # big stuff
        self.article.top_node = self.extractor.calculate_best_node()

        #print("doc", self.article.doc , self.article.doc .attrib)
        #print("top_node", self.article.top_node , self.article.top_node .attrib)
        #if article_body was already found, use it as topnode
        #if self.article.top_node is not None and \
        #    self.article_body is not None and \
        #        self.extractor.get_score_by_avg(self.article.top_node) < 1.5:
        #    self.article.top_node = self.article_body

        # if we have a top node
        # let's process it
        if self.article.top_node is not None:
            # article links
            self.article.links = self.links_extractor.extract()

            # tweets
            self.article.tweets = self.tweets_extractor.extract()

            # video handling
            self.video_extractor.get_videos()

            # image handling
            if self.config.enable_image_fetching:
                self.get_image()

            # post cleanup
            self.article.top_node = self.extractor.post_cleanup()

            # clean_text
            self.article.cleaned_text = self.formatter.get_formatted_text()

        # cleanup tmp file
        self.release_resources()

        # return the article
        return self.article

    def get_parse_candidate(self, crawl_candidate):
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
