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

KNOWN_AUTHOR_TAGS = [
    {'attribute': 'class', 'value': 'ng_byline_name', 'content': None},
    {'attribute': 'class', 'value': 'author-name', 'content': None},
    {'xpath': "descendant::*[contains(@class, 'byline')]", 'content': None},
]

class AuthorsExtractor(BaseExtractor):
    AUTHOR_REPLACER = re.compile("(^by\s+)|([\|\/].+)", flags=re.IGNORECASE)
    AUTHOR_SPLITTER = re.compile(ur"\band\b|,", flags=re.IGNORECASE|re.U)

    def extract(self):
        authors = []
        author_nodes = self.parser.getElementsByTag(
                            self.article.doc,
                            attr='itemprop',
                            value='author')
        for author_node in author_nodes:
            name_nodes = self.parser.getElementsByTag(
                            author_node,
                            attr='itemprop',
                            value='name')
            if len(name_nodes) > 0:
                name = self.parser.getText(name_nodes[0])
                authors.append(name)
            else:
                authors.append(self.parser.getText(author_node))

        for known_tag in KNOWN_AUTHOR_TAGS:
            if known_tag.get('xpath'):
                tags = self.parser.xpath_re(self.article.doc, known_tag.get('xpath'))
            else:
                tags = self.parser.getElementsByTag(
                                self.article.doc,
                                attr=known_tag['attribute'],
                                value=known_tag['value'])
            if tags:
                if not known_tag['content']:
                    author = self.parser.getText(tags[0])
                else:
                    author = self.parser.getAttribute(
                        tags[0],
                        known_tag['content']
                    )
                authors.append(author)

        for item in self.article.microdata.get("newsarticle", []):
            author = item.get('author')
            if author:
                authors.append(author)

        for item in self.article.microdata.get("person", []):
            author = item.get('name')
            if author:
                authors.append(author)

        for item in self.article.microdata.get("hcard", []):
            author = item.get('n')
            if author:
                authors.append(author)

        author = self.article.metatags.get("author")
        if author:
            authors.append(author)

        clean_authors = []
        author_keys = {}
        for full_author in authors:
            if not full_author:
                continue
            if not isinstance(full_author, str) and \
               not isinstance(full_author, unicode):
                continue
            for author in self.AUTHOR_SPLITTER.split(full_author):
                author = self.AUTHOR_REPLACER.sub("", author).strip()
                if author.lower() in author_keys:
                    continue
                author_keys[author.lower()] = True
                clean_authors.append(author)

        clean_authors = list(set(clean_authors))
        return clean_authors
