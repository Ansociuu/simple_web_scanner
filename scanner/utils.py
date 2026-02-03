# utils.py
from urllib.parse import urlparse

def normalize_url(url):
    if not url.startswith("http"):
        url = "http://" + url
    return url

def get_domain(url):
    return urlparse(url).netloc
