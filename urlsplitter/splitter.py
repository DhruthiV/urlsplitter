from urllib.parse import urlparse, unquote

def split_url(url: str, decode: bool = False) -> dict:
    """
    Takes a URL and returns a dictionary with its components.
    
    Args:
        url (str): The URL to parse.
        decode (bool): If True, decodes percent-encoded characters.

    Returns:
        dict: Parsed URL components.
    """
    try:
        parsed = urlparse(url)

        return {
            "scheme": parsed.scheme,
            "domain": parsed.netloc,
            "path": unquote(parsed.path) if decode else parsed.path,
            "query": unquote(parsed.query) if decode else parsed.query,
            "fragment": unquote(parsed.fragment) if decode else parsed.fragment
        }
    
    except Exception as e:
        return {"error": f"Invalid URL: {str(e)}"}

# Example usage:
# print(split_url("https://example.com/path?query=123#frag", decode=True))
