from goose.extractors import BaseExtractor


class MicroDataExtractor(BaseExtractor):

    def extract(self):
        item_scopes = {}
        nodes = self.parser.getElementsByXPath(
                            self.article.doc, '//*[@itemscope]')

        for node in nodes:
            item_type = self.parser.getAttribute(node, 'itemtype')
            item_type = item_type.lower().split("/")[-1]
            if item_type not in item_scopes:
                item_scopes[item_type] = []
            item_scopes[item_type].append(self.getItemprops(node))
        return item_scopes

    def getItemprops(self, node):
        item_props = {}
        nodes = self.parser.getElementsByXPath(node, 'descendant::*[@itemprop]')
        for child in nodes:
            prop_name = self.parser.getAttribute(child, 'itemprop').lower()
            itemscope = self.parser.getAttribute(child, 'itemscope')
            if itemscope:
                prop_name = prop_name.split("/")[-1]
                prop = [self.getItemprops(child)]
            else:
                tag_name = self.parser.getTag(child)
                if tag_name == "time":
                    prop = self.parser.getAttribute(child, 'datetime')
                elif tag_name == "meta":
                    prop = self.parser.getAttribute(child, 'content')
                elif tag_name == "url":
                    prop = self.parser.getAttribute(child, 'href')
                    if prop is None:
                        prop = self.parser.getAttribute(child, 'content')
                else:
                    prop = self.parser.getText(child)
            item_props[prop_name] = prop
        return item_props
