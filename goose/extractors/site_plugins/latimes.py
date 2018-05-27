import urllib2
import json

API_BASE_URL = 'http://www.latimes.com/pb/api/v2/render/feature/article/body?'
API_URL = API_BASE_URL + 'contentConfig={0}&fromAPICall=true&customFields={1}&fromPoller=true&wrapper=false&service=content-api'

def extract_more(extractor, htmlfetcher):
    read_more_btn = extractor.parser.xpath_re(
        extractor.article.doc, "descendant::button[@name='readMore']")
    if not read_more_btn:
        return
    btn = read_more_btn[0]

    config_keys = extractor.parser.getAttribute(btn, "data-content-config-keys").split(",")
    config_values = extractor.parser.getAttribute(btn, "data-content-config-values").split(",")

    custom_keys = extractor.parser.getAttribute(btn, "data-custom-field-keys").split(",")
    custom_values = extractor.parser.getAttribute(btn, "data-custom-field-values").split(",")

    content_configs = []
    for i in range(len(config_keys)):
        content_configs.append('"{0}":"{1}"'.format(config_keys[i], config_values[i]))
    content_config = '{' + (",".join(content_configs)) + '}'

    custom_field_items = []
    for i in range(len(custom_keys)):
        custom_field_items.append('"{0}":"{1}"'.format(custom_keys[i], custom_values[i]))
    custom_fields = '{' + (",".join(custom_field_items)) + '}'

    more_link = API_URL.format(urllib2.quote(content_config), urllib2.quote(custom_fields))

    data = htmlfetcher.get_html(more_link)
    json_data = json.loads(data)
    extra_node = extractor.parser.stringToNode(json_data["rendering"])
    if extra_node is not None:
        btn_parent = extractor.parser.getParent(btn)
        extractor.parser.appendChild(btn_parent, extra_node)

