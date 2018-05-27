from . import latimes

def get_more_extractor(domain):
    module = None
    if "latimes.com" in domain:
        module = latimes
    if module:
        return module.extract_more
    return None


