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
import re
from goose.extractors import BaseExtractor
import goose.text

class LinkItem(dict):
    def __init__(self, url, text):
        self["url"] = url
        self["text"] = text

    @property
    def url(self):
        return self["url"]

    @property
    def text(self):
        return self["text"]

    def __repr__(self):
        return "(url={0}, text={1})".format(self.url, self.text.encode("utf-8"))

class LinksExtractor(BaseExtractor):
    BAD_HTML_LINK_NAME = re.compile(r'/style/')

    def extract(self):
        links = []
        items = self.parser.getElementsByTag(self.article.top_node, 'a')
        for i in items:
            attr = self.parser.getAttribute(i, 'href')
            if attr:
                links.append(attr)
        return links

    def extract_html_links(self):
        links = []
        items = self.parser.getElementsByTag(self.article.doc, 'a')
        for i in items:
            attr = self.parser.getAttribute(i, 'href')
            if not attr:
                continue
            text = self.parser.getText(i).strip()
            if not text or len(text.split(' ')) < 3:
                continue
            if self.BAD_HTML_LINK_NAME.search(attr):
                continue
            attr = self.get_clean_href(attr)
            if not attr:
                continue
            links.append(LinkItem(attr, text))
        return links

    READ_MORE_RE = re.compile(r"read.*more", flags=re.IGNORECASE)
    def extract_read_more(self):
        items = self.parser.getElementsByTag(self.article.doc, "a")
        for link in items:
            text = self.parser.getText(link)
            if not self.READ_MORE_RE.search(text):
                continue
            href = self.parser.getAttribute(link, 'href')
            if href:
                return href
        return None

    def get_clean_href(self, href):
        if href[0] == "/" and href[1:2] != "/":#exlcude //ww.abc.com type names
            href = self.article.site_domain + href[1:]
        else:
            link_site_domain = goose.text.get_site_domain(href)
            if self.article.site_domain and link_site_domain != self.article.site_domain:
                return None
            last_seg = href.split("/")[-1]
            if not last_seg or last_seg[0] == "#":
                return None
        return href
