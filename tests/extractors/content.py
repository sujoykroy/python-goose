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
from base import TestExtractionBase, MockResponseExtractors

from goose.text import StopWordsChinese
from goose.text import StopWordsArabic
from goose.text import StopWordsKorean
from goose.crawler import Crawler, CrawlCandidate

from goose.extractors import site_plugins

class MockContentResponseExtractors(MockResponseExtractors):
    def response_file_map(self, url, func):
        if url.startswith(site_plugins.latimes.API_BASE_URL):
            return func + "_api_json"
        return func

class TestExtractions(TestExtractionBase):
    callback = MockContentResponseExtractors

    def test_allnewlyrics1(self):
        article = self.getArticle()
        fields = ['title', 'cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_cnn1(self):
        article = self.getArticle()
        fields = ['title', 'cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_businessWeek1(self):
        article = self.getArticle()
        fields = ['title', 'cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_businessWeek2(self):
        article = self.getArticle()
        fields = ['title', 'cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_businessWeek3(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_cbslocal(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_elmondo1(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_elpais(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_liberation(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_lefigaro(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_techcrunch1(self):
        article = self.getArticle()
        fields = ['title', 'cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_foxNews(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_aolNews(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_huffingtonPost2(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_testHuffingtonPost(self):
        article = self.getArticle()
        fields = ['cleaned_text', 'meta_description', 'title', ]
        self.runArticleAssertions(article=article, fields=fields)

    def test_espn(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_engadget(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_msn1(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    # #########################################
    # # FAIL CHECK
    # # UNICODE
    # def test_guardian1(self):
    #     article = self.getArticle()
    #     fields = ['cleaned_text']
    #     self.runArticleAssertions(article=article, fields=fields)
    def test_time(self):
        article = self.getArticle()
        fields = ['cleaned_text', 'title']
        self.runArticleAssertions(article=article, fields=fields)

    def test_time2(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_cnet(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_yahoo(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_politico(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_businessinsider3(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_cnbc1(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_marketplace(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_issue24(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_issue25(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_issue28(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_issue32(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_issue4(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_gizmodo1(self):
        article = self.getArticle()
        fields = ['cleaned_text', 'meta_description', 'meta_keywords']
        self.runArticleAssertions(article=article, fields=fields)

    def test_mashable_issue_74(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_usatoday_issue_74(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_okaymarketing(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_issue129(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_issue115(self):
        # https://github.com/grangier/python-goose/issues/115
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_project_syndicate(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_weforum(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_latimes(self):
        self.response_file_map

        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_latimes_subsc(self):
        self.response_file_map

        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)


class TestArticleTopNode(TestExtractionBase):

    def test_articlebody_itemprop(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_articlebody_attribute(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_articlebody_tag(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)


class TestExtractWithUrl(TestExtractionBase):

    def test_get_canonical_url(self):
        article = self.getArticle()
        fields = ['cleaned_text', 'canonical_link']
        self.runArticleAssertions(article=article, fields=fields)


class TestExtractChinese(TestExtractionBase):

    def getConfig(self):
        config = super(TestExtractChinese, self).getConfig()
        config.stopwords_class = StopWordsChinese
        return config

    def test_bbc_chinese(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)


class TestExtractArabic(TestExtractionBase):

    def getConfig(self):
        config = super(TestExtractArabic, self).getConfig()
        config.stopwords_class = StopWordsArabic
        return config

    def test_cnn_arabic(self):
        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)


class TestExtractKorean(TestExtractionBase):

    def getConfig(self):
        config = super(TestExtractKorean, self).getConfig()
        config.stopwords_class = StopWordsKorean
        return config

    def test_donga_korean(self):
        article = self.getArticle()
        fields = ['cleaned_text', 'meta_description', 'meta_keywords']
        self.runArticleAssertions(article=article, fields=fields)


class TestExtractionsRaw(TestExtractions):

    def extract(self, instance):
        article = instance.extract(raw_html=self.getRawHtml())
        return article


class TestSubArticleExtraction(TestExtractionBase):
    def test_raw_article_content(self):
        config = self.getConfig()

        raw_html = """
            <article class="story theme-summary  " itemscope="" itemtype="http://schema.org/NewsArticle">
                <div class="story-body">
                    <a class="story-link" data-rref="" href="https://www.nytimes.com/2018/08/07/us/politics/rosie-odonnell-broadway-white-house-protest.html">
                        <div class="story-meta">
                                            <h2 class="headline" itemprop="headline">
                                Rosie O'Donnell and Chorus of Broadway Stars Perform Musical Protest at White House                </h2>
                            <p class="summary" itemprop="description">On the 22nd night of a series of protests, cast members from &#8220;Wicked,&#8221; &#8220;Hamilton&#8221; and other shows sang songs meant to evoke a political edge or offer a tinge of hope for the hundreds of demonstrators.</p>
                                                <p class="byline" itemprop="author">By ALEXANDRA YOON-HENDRICKS</p>
                                        </div><!-- close story-meta -->
                                        <div class="wide-thumb">
                                <img role="presentation" src="https://static01.nyt.com/images/2018/08/07/us/politics/-08dc-occupy-3/merlin_142080273_0d5bed71-f59c-438c-8157-4166a5ee6dde-mediumThreeByTwo210.jpg" alt="" itemprop="thumbnailUrl"/>
                                                                    </div><!-- close wide-thumb -->
                                </a>
                </div><!-- close story-body -->
                <footer class="story-footer">
                    <time class="dateline" datetime="2018-08-07" itemprop="dateModified" content="2018-08-07">Aug. 7, 2018</time>
                </footer>
            </article>
        """
        crawler = Crawler(config)
        article = crawler.crawl(
            CrawlCandidate(config, None, raw_html), crawl_sub=False)
        self.assertEqual(
            "Rosie O'Donnell and Chorus of Broadway Stars Perform Musical"[0:50],
            article.title[0:50])
        self.assertEqual(
            "https://www.nytimes.com/2018/08/07/us/politics/rosie-odonnell-broadway-white-house-protest.html", article.links[0])
        self.assertEqual(
            article.microdata.get("newsarticle")[0].get("thumbnailurl"),
            "https://static01.nyt.com/images/2018/08/07/us/politics/-08dc-occupy-3/merlin_142080273_0d5bed71-f59c-438c-8157-4166a5ee6dde-mediumThreeByTwo210.jpg")


    def test_sub_articles_2(self):
        article = self.getArticle()
        self.assertEqual(43, len(article.sub_articles))
        self.assertEqual(
            article.sub_articles[0].crawled_article.title[0:20],
            "Boris Johnson Speaks, and His Many Critics"[0:20])
        self.assertEqual(
            article.sub_articles[40].crawled_article.title[0:20],
            "Top Trump Campaign Aides Are Portrayed"[0:20])


    def test_sub_articles_1(self):
        article = self.getArticle()
        self.assertTrue(len(article.html_links) > 0)
        self.assertTrue(len(article.sub_articles) == 0)
