from openworld.sdk.core.client.pagination import Paginator
from openworld.sdk.core.constant import header


def extract_rapid_next_page_link(paginator: Paginator) -> str:
    # TODO: Raise an exception instead of any empty string.
    if not paginator.request_headers or not paginator.last_response_headers or not paginator.is_link_in_request_headers():
        return ""

    link: str = paginator.last_response_headers[header.LINK].split(";")[0]

    if not (link or "<" in link or ">" in link):
        return ""

    link = link[link.index("<") + 1: link[link.index(">")]]

    return link
