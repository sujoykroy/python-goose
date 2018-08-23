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

class TestExtractions(TestExtractionBase):
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

    def test_msn2(self):
        config = self.getConfig()
        config.enable_image_fetching = True
        article = self.getArticle()
        fields = ["authors", 'cleaned_text']
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

    def test_politico_2(self):
        article = self.getArticle()
        fields = ['cleaned_text', 'publish_date', 'authors']
        self.runArticleAssertions(article=article, fields=fields)

    def test_politico_3(self):
        article = self.getArticle()
        fields = ['authors', 'publish_date', 'cleaned_text']
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
        #self.response_file_map

        article = self.getArticle()
        fields = ['cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_latimes_subsc(self):
        article = self.getArticle()
        fields = ['authors', 'cleaned_text']
        self.runArticleAssertions(article=article, fields=fields)

    def test_miami_herald(self):
        article = self.getArticle()
        fields = ['cleaned_text', 'publish_date', "authors"]
        self.runArticleAssertions(article=article, fields=fields)

    def test_normantranscript(self):
        article = self.getArticle()
        fields = ['json_ld']
        self.runArticleAssertions(article=article, fields=fields)

    def test_newslocker(self):
        article = self.getArticle()
        fields = ["title", 'read_more_url']
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
    def test_raw_article_content_1(self):
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

    def test_raw_article_content_2(self):
        config = self.getConfig()
        config.enable_image_fetching = True
        raw_html = """
        <article class="story-frag format-m">
            <figure class="thumb">
                    <div class="fig-graphic ">
                        <a href="https://www.politico.com/story/2018/08/10/manhattan-madam-mueller-trump-stone-771182" target="_top"><img data-lazy-img="https://static.politico.com/dims4/default/9bbeb3b/2147483647/resize/403x%3E/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2Fe9%2F11%2Fba5f49dd4d5c840708c71ad6b403%2F180809-kristin-davis-ap-1160.jpg" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" alt=" Kristin Davis, aka the Manhattan Madam, is pictured. | AP Photo" data-size="promo_medium"></a></div>
                </figure>
            <div class="summary">
                <header>
                    <p class="category">
                                <a href="https://www.politico.com/tag/mueller-investigation" target="_blank">mueller investigation</a></p>
                        <h3>
                        <a href="https://www.politico.com/story/2018/08/10/manhattan-madam-mueller-trump-stone-771182" target="_top">Mystery surrounds former sex-ring operator&#039;s Mueller probe role</a></h3>
                </header>
                <footer class="meta">
                <div itemprop="author" itemscope itemtype="https://schema.org/Person">
                            <meta itemprop="name" content="Kyle Cheney"/>
                            <meta itemprop="email" content="kcheney@politico.com"/>
                        </div>
                    <p class="byline">
                                By <a href="https://www.politico.com/staff/kyle-cheney" rel="author" class="url fn" target="_top">KYLE CHENEY</a></p>
                        <p class="timestamp"><time itemprop="datePublished" datetime='2018-08-10 05:05:04'>08/10/2018 05:05 AM EDT</time></p>
                                </footer><div class="social">
                    <ul class="social">
                        </ul>
                </div>
            </div>
        </article>
        """
        crawler = Crawler(config)
        article = crawler.crawl(
            CrawlCandidate(config, None, raw_html), crawl_sub=False)
        self.assertEqual(
            "Mystery surrounds former sex-ring operato"[0:30],
            article.title[0:30])
        self.assertEqual(
            "https://www.politico.com/story/2018/08/10/manhattan-madam-mueller-trump-stone-771182", article.links[0])
        self.assertEqual(
            "https://static.politico.com/dims4/default/9bbeb3b/2147483647/resize/403x%3E/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2Fe9%2F11%2Fba5f49dd4d5c840708c71ad6b403%2F180809-kristin-davis-ap-1160.jpg", article.top_image.get_src())

    def test_raw_article_content_3(self):
        config = self.getConfig()
        config.enable_image_fetching = True
        config.enable_image_download = False
        raw_html = """
        <article class="story-frag format-xs">
            <figure class="thumb">
                <div class="fig-graphic">
                    <a href="https://www.politico.com/magazine/story/2018/08/08/alex-jones-banned-lowry-219343" target="_top" data-tracking="mpos=right-rail&mid=LeadAndThumbnailModule&lindex=4&lcol=1" class="js-tealium-tracking"><img data-lazy-img="https://static.politico.com/dims4/default/e17797b/2147483647/resize/403x%3E/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2Fd8%2F15%2F216feb3148138735a9f0cf2f6924%2F180808-alex-jones-gtty-1160.jpg" src="data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==" alt="Alex Jones is pictured. | Getty Images" data-size="promo_medium"></a></div>
            </figure>
            <div class="summary">
                <header>
                    <h3><a href="https://www.politico.com/magazine/story/2018/08/08/alex-jones-banned-lowry-219343" target="_top" data-tracking="mpos=right-rail&mid=LeadAndThumbnailModule&lindex=4&lcol=1" class="js-tealium-tracking">Don't Ban Alex Jones</a></h3>
                </header>
                <footer class="meta">
                    <p class="byline">
                            By <span class="vcard">Rich Lowry</span></p>
                    </footer>
            </div>
        </article>
        """
        crawler = Crawler(config)
        article = crawler.crawl(
            CrawlCandidate(config, None, raw_html), crawl_sub=False)
        self.assertEqual(
            "Don't Ban Alex Jones"[0:30],
            article.title[0:30])
        self.assertEqual(
            "https://www.politico.com/magazine/story/2018/08/08/alex-jones-banned-lowry-219343", article.links[0])
        self.assertEqual(
            "https://static.politico.com/dims4/default/e17797b/2147483647/resize/403x%3E/quality/90/?url=https%3A%2F%2Fstatic.politico.com%2Fd8%2F15%2F216feb3148138735a9f0cf2f6924%2F180808-alex-jones-gtty-1160.jpg", article.top_image.get_src())
        self.assertEqual(article.hcards[0]["n"], "Rich Lowry")

    def test_raw_article_content_4(self):
        config = self.getConfig()
        config.enable_image_fetching = True
        raw_html = """
        <article class="story theme-summary">
            <a class="story-link" href="https://www.nytimes.com/video/us/politics/100000006037851/sanders-media-enemy-of-the-people.html">
                        <div class="wide-thumb">
                    <img src="https://static01.nyt.com/images/2018/08/03/us/politics/03acosta-alpha2/03acosta-alpha2-videoSmall.jpg" role="presentation" alt="Sanders Won't Say the Media Is Not the ‘Enemy’">
                    <div class="media-action-overlay">
                        <i class="icon video-icon"></i>
                    </div>
                </div>
                        <div class="story-body">
                    <h2 class="headline">Sanders Won't Say the Media Is Not the ‘Enemy’</h2>
                    <time class="dateline" datetime="2018-08-02" itemprop="dateModified" content="2018-08-02">Aug. 2, 2018</time>
                </div>
            </a>
        </article>
        """
        crawler = Crawler(config)
        article = crawler.crawl(
            CrawlCandidate(config, None, raw_html), crawl_sub=False)
        self.assertEqual(
            "Sanders Won't Say the Media Is Not the "[0:30],
            article.title[0:30])

        self.assertEqual(
            "https://www.nytimes.com/video/us/politics/100000006037851/sanders-media-enemy-of-the-people.html", article.html_links[0].url)
        self.assertEqual(
            "https://static01.nyt.com/images/2018/08/03/us/politics/03acosta-alpha2/03acosta-alpha2-videoSmall.jpg", article.top_image.get_src())
        self.assertEqual(article.microdata["article"]["datemodified"], "2018-08-02")


    def test_raw_article_author_1(self):
        config = self.getConfig()
        raw_html = """
            <article class="story theme-summary  " itemscope="" itemtype="http://schema.org/NewsArticle">
                <div class="story-body">
                    <a class="story-link" href="https://www.nytimes.com/2018/08/13/nyregion/welfare-immigrants-trump-public-charge-rule.html?rref=collection%2Ftimestopic%2FTrump%2C%20Donald%20J.">
                        <div class="story-meta">
                                            <h2 class="headline" itemprop="headline">
                                How Trump’s Plan for Immigrants on Welfare Could Hurt a Million New Yorkers                </h2>
                            <p class="summary" itemprop="description">A proposed rule would make it difficult for immigrants and their family members who use government services to obtain permanent residency, city officials said.</p>
                                                <p class="byline" itemprop="author">By LIZ ROBBINS</p>
                                        </div><!-- close story-meta -->
                                        <div class="wide-thumb">
                                <img role="presentation" src="https://static01.nyt.com/images/2018/08/10/nyregion/10nyimmig/merlin_142140306_73a2c749-16e6-4fa0-b1d5-9851f715b353-mediumThreeByTwo210.jpg" alt="" itemprop="thumbnailUrl">
                                                                    </div><!-- close wide-thumb -->
                                </a>
                </div><!-- close story-body -->
                <footer class="story-footer">
                    <time class="dateline" datetime="2018-08-13" itemprop="dateModified" content="2018-08-13">Aug. 13, 2018</time>
                </footer>
            </article>
        """
        crawler = Crawler(config)
        article = crawler.crawl(
            CrawlCandidate(config, None, raw_html), crawl_sub=False)
        self.assertEqual(article.authors[0], "LIZ ROBBINS")


    def test_sub_articles_1(self):
        article = self.getArticle()
        self.assertTrue(len(article.html_links) > 0)
        self.assertTrue(len(article.sub_articles) == 0)

    def test_sub_articles_2(self):
        article = self.getArticle()
        self.assertEqual(42, len(article.sub_articles))
        self.assertEqual(
            article.sub_articles[0].crawled_article.title[0:20],
            "Donald Trump Runs For Governor"[0:20])
        self.assertEqual(
            article.sub_articles[39].crawled_article.title[0:20],
            "Top Trump Campaign Aides Are Portrayed"[0:20])

    def test_sub_articles_3(self):
        article = self.getArticle()
        self.assertTrue(len(article.sub_articles) > 0)
