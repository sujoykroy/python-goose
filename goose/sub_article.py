from copy import deepcopy

from goose.utils import ParsingCandidate

class SubArticle(object):
    def __init__(self, node, parser):
        self.parser = parser
        self.node = node
        self.outer_html = self.parser.outerHtml(node)
        self.crawled_article = None


    @property
    def authors(self):
        if not self.crawled_article:
            return []
        return self.crawled_article.authors

    @property
    def cleaned_text(self):
        if not self.crawled_article:
            return ''
        return self.crawled_article.cleaned_text

    @classmethod
    def get_parsing_candidate(cls, node):
        return ParsingCandidate(None, raw_html=html)
