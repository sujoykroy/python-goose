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

class LinkItem(object):
    def __init__(self, url, text):
        self.url = url
        self.text = text

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
        items = self.parser.getElementsByTag(self.article.top_node, 'a')
        for i in items:
            attr = self.parser.getAttribute(i, 'href')
            if not attr:
                continue
            text = self.parser.getText(i).strip()
            if not text or len(text.split(' ')) < 3:
                continue
            if self.BAD_HTML_LINK_NAME.search(attr):
                continue
            if attr[0] == "/":
                attr = self.article.site_domain + attr
            else:
                link_site_domain = goose.text.get_site_domain(attr)
                if link_site_domain != self.article.site_domain:
                    continue

            links.append(LinkItem(attr, text))
        return links
