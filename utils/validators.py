import datetime
import urllib.parse


def url_validator(url: str) -> bool:
    """Validate if a given string is a URL"""
    try:
        result = urllib.parse.urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False
