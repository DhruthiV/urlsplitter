from urllib.parse import urlparse

def split_url(url: str) -> str:
    """Takes a URL and returns a formatted string with its components."""
    parsed = urlparse(url)
    return (
        f"Scheme: {parsed.scheme}\n"
        f"Domain: {parsed.netloc}\n"
        f"Path: {parsed.path}\n"
        f"Query: {parsed.query}\n"
        f"Fragment: {parsed.fragment}"
    )
