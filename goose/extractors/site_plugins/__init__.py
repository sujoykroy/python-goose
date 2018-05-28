from . import latimes

def get_more_extractor(domain):
    if domain is None:
        return None
    module = None
    if "latimes.com" in domain:
        module = latimes
    if module:
        return module.extract_more
    return None


