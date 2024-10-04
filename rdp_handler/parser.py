import urllib.parse


def parse_rdp_url(url: str) -> dict:
    if not url.startswith("rdp://"):
        raise ValueError("Invalid URL scheme. URL must start with 'rdp://'")

    # Remove the 'rdp://' prefix
    url = url[6:]

    # Parse the URL
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)

    # Flatten the query parameters
    params = {k: v[0] for k, v in query_params.items()}

    # Include the netloc as 'v' if not present in query
    if parsed_url.netloc:
        params['v'] = parsed_url.netloc

    # Handle boolean and integer conversions
    for key in ['w', 'h']:
        if key in params:
            params[key] = int(params[key])

    for key in ['multimon', 'f']:
        if key in params:
            params[key] = params[key].lower() == 'true'

    return params
