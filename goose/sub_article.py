from copy import deepcopy

from goose.utils import ParsingCandidate

class SubArticle(object):
    def __init__(self, node, parser):
        self.parser = parser
        self.node = node
        self.outer_html = self.parser.outerHtml(node)

    @classmethod
    def get_parsing_candidate(cls, node):
        return ParsingCandidate(None, raw_html=html)
