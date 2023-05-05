import http
from collections.abc import Generator
from enum import Enum
from typing import Any, Callable
from uuid import uuid4

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.constant import header
from openworld.sdk.core.util.pagination import extract_rapid_next_page_link


class PageLinkExtractionStrategy(Enum):
    DEFAULT: Callable = extract_rapid_next_page_link


class Paginator:
    __api_client: ApiClient
    __response_models: list[Any]
    __request_headers: dict[Any, Any]
    __endpoint: str
    __first_page: list[Any]
    __last_response_headers: dict[Any, Any]
    __pagination_total_results: int
    __extract_page_link: PageLinkExtractionStrategy

    def __init__(
        self,
        api_client: ApiClient,
        response_models: list = [None],  # noqa
        request_headers: dict = dict(),  # noqa
        endpoint: str = "",
        link_extraction_strategy: PageLinkExtractionStrategy = PageLinkExtractionStrategy.DEFAULT
    ):
        self.__api_client = api_client
        self.__response_models = response_models
        self.__request_headers = request_headers
        self.__endpoint = endpoint
        self.__extract_page_link = link_extraction_strategy

        self.__post_init__()

    def __post_init__(self):
        self.__last_response_headers, self.__first_page = self.__get_first_page_with_headers()
        self.__pagination_total_results = self.__extract_pagination_total_results()
        self.__update_next_page_endpoint(page_num=2)

    def __get_first_page_with_headers(
        self,
    ) -> tuple[dict[Any, Any], list[Any]]:
        return self.__api_client.call(
            method=http.HTTPMethod.GET, url=self.__endpoint, body=None, headers=self.__request_headers,
            response_models=self.__response_models
        )

    def get_pages(
        self,
    ) -> Generator[Any]:
        # TODO: Add docstrings.
        if not self.__last_response_headers or not self.__pagination_total_results:
            raise StopIteration()

        for page_num in range(1, self.__pagination_total_results + 1):
            if page_num == 1:
                yield self.__first_page
                continue

            self.__last_response_headers, new_page = self.__api_client.call(
                method=http.HTTPMethod.GET, url=self.__endpoint, body=None, headers=self.__request_headers,
                response_models=self.__response_models
            )

            self.__update_next_page_endpoint(page_num=page_num)

            yield new_page

    def __iter__(self):
        self.get_pages()

    def is_link_in_request_headers(self) -> bool:
        return header.LINK in self.__last_response_headers.keys()

    def __update_next_page_endpoint(
        self,
        page_num: int = 1,
    ) -> None:
        # TODO: Add docstrings.
        if page_num <= 1 or not self.__last_response_headers or not self.is_link_in_request_headers():  # noqa
            return

        self.__endpoint = self.__extract_page_link(self)

    def __update_transaction_id(self):
        # TODO: Add docstrings.
        if not self.__request_headers:
            return

        self.__request_headers[header.TRANSACTION_ID] = str(uuid4())

    def __extract_pagination_total_results(self) -> int:
        if not self.__last_response_headers or not header.PAGINATION_TOTAL_RESULTS in self.__last_response_headers.keys():  # noqa
            return 0

        return int(self.__last_response_headers[header.PAGINATION_TOTAL_RESULTS])

    @property
    def request_headers(self):
        return self.__request_headers

    @property
    def last_response_headers(self):
        return self.__last_response_headers

    @property
    def endpoint(self):
        return self.__endpoint

    @property
    def first_page(self):
        return self.__first_page
