from goose.extractors import BaseExtractor

class HCardExtractor(BaseExtractor):

    def extract(self):
        vcards = []
        vcard_nodes = self.parser.getElementsByXPath(
                            self.article.doc, '//*[contains(@class, "vcard")]')

        for vcard_node in vcard_nodes:
            vcard = {}
            for node_type in ["fn", "url", "org", "n"]:
                nodes = self.parser.getElementsByXPath(
                    vcard_node, 'descendant::*[contains(@class, "{}")]'.format(node_type))

                if len(nodes) > 0:
                    if node_type == "url":
                        text = self.parser.getAttribute(nodes[0], "href")
                        vcard[node_type] = text
                        vcard["url_text"] = self.parser.getText(nodes[0])
                    else:
                        text = self.parser.getText(nodes[0])
                        vcard[node_type] = text
            if vcard.keys():
                vcards.append(vcard)
            else:
                vcards.append({"n": self.parser.getText(vcard_node)})
        return vcards
