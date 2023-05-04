import http
from typing import Union, Any, Generator
from uuid import uuid4

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.constant import header


class Paginator:
    __api_client: ApiClient
    __response_models: list[Any]
    __request_headers: dict[Any, Any]
    __endpoint: str
    __first_page: list[Any]
    __last_response_headers: dict[Any, Any]
    __pagination_total_results: int

    def __init__(
        self,
        api_client: ApiClient,
        response_models: list = [None],
        request_headers: dict = dict(),
        endpoint: str = "",
    ):
        self.__api_client = api_client
        self.__response_models = response_models
        self.__request_headers = request_headers
        self.__endpoint = endpoint

        self.__post_init__()

    def __post_init__(self):
        self.__last_response_headers, self.__first_page = self.__get_first_page_with_headers()[1]
        self.__pagination_total_results = self.__extract_pagination_total_results()
        self.__update_next_page_endpoint(page_num=2)

    def __get_first_page_with_headers(self, ) -> tuple[dict[Any, Any], list[Any]]:
        return self.__api_client.call(
            method=http.HTTPMethod.GET,
            url=self.__endpoint,
            body=None,
            headers=self.__request_headers,
            response_models=self.__response_models
        )

    def get_pages(self, ) -> Generator[Any]:
        # TODO: Add docstrings.
        if not self.__last_response_headers or not self.__pagination_total_results:
            raise StopIteration()

        for page_num in range(1, self.__pagination_total_results + 1):
            if page_num == 1:
                yield self.__first_page
                continue

            self.__last_response_headers, new_page = self.__api_client.call(
                method=http.HTTPMethod.GET,
                url=self.__endpoint,
                body=None,
                headers=self.__request_headers,
                response_models=self.__response_models
            )

            self.__update_next_page_endpoint(page_num=page_num)

            yield new_page

    def __iter__(self):
        self.get_pages()

    def __update_next_page_endpoint(self, page_num: int = 1, ) -> None:
        # TODO: Add docstrings.
        if page_num <= 1 or not self.__last_response_headers or header.LINK not in self.__last_response_headers.keys():
            return

        self.__endpoint = self.__extract_page_link(self.__last_response_headers)

    def __extract_page_link(self, last_response_headers: dict) -> Union[str, None]:
        # TODO: Add docstrings.
        if not self.__request_headers or not last_response_headers or header.LINK not in self.__request_headers.keys():
            return

        link: str = last_response_headers[header.LINK].split(";")[0]

        if not (link or "<" in link or ">" in link):
            return

        link = link[link.index("<") + 1: link[link.index(">")]]

        return link

    def __update_transaction_id(self):
        # TODO: Add docstrings.
        if not self.__request_headers:
            return

        self.__request_headers[header.TRANSACTION_ID] = str(uuid4())

    def __extract_pagination_total_results(self) -> int:
        if not self.__last_response_headers or not header.PAGINATION_TOTAL_RESULTS in self.__last_response_headers.keys():
            return 0

        return int(self.__last_response_headers[header.PAGINATION_TOTAL_RESULTS])
