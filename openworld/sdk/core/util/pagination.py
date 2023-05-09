from openworld.sdk.core.constant import header as header_constant


def extract_rapid_next_page_link(headers: dict) -> str:
    # TODO: Raise an exception instead of any empty string.
    if not headers or header_constant.LINK not in headers.keys():
        return ""

    link: str = headers[header_constant.LINK].split(";")[0]

    if not (link or "<" in link or ">" in link):
        return ""

    link: str = link[link.index("<") + 1 : link.index(">")]

    return link
