from collections.abc import Callable, Generator
from enum import Enum
from typing import Any
from uuid import uuid4

from openworld.sdk.core.client.api import ApiClient
from openworld.sdk.core.constant import header
from openworld.sdk.core.model.api import Response
from openworld.sdk.core.util.pagination import extract_rapid_next_page_link


class PageLinkExtractionStrategy(Enum):
    r"""Enums of available links extraction strategies."""
    DEFAULT: Callable = extract_rapid_next_page_link


class Paginator:
    __api_client: ApiClient
    __response_models: list[Any]
    __request_headers: dict[Any, Any]
    __next_page_endpoint: str
    __first_page_endpoint: str
    __first_page: Any
    __last_response_headers: dict[Any, Any]
    __pagination_total_results: int
    __extract_page_link: PageLinkExtractionStrategy

    def __init__(
        self,
        api_client: ApiClient,
        response_models: list = [None],  # noqa
        request_headers: dict = dict(),  # noqa
        endpoint: str = "",
        link_extraction_strategy: PageLinkExtractionStrategy = PageLinkExtractionStrategy.DEFAULT,
    ):
        r"""Sends requests to API and handles pagination for paginated endpoints.

        Args:
            api_client(ApiClient): ApiClient instance that handles requests.
            response_models(list[Any]): A list of types that can be used to deserialize responses.
            request_headers(dict): Request headers.
            endpoint(str): Endpoint used to get first page.
            link_extraction_strategy(PageLinkExtractionStrategy): Strategy used for links extraction from response headers.
        """
        self.__api_client = api_client
        self.__response_models = response_models
        self.__request_headers = request_headers
        self.__next_page_endpoint = endpoint
        self.__first_page_endpoint = endpoint
        self.__extract_page_link = link_extraction_strategy

        self.__post_init__()

    def __post_init__(self):
        response: Response = self.__get_first_page_response()

        self.__last_response_headers, self.__first_page = response.raw.headers, response.body

        self.__pagination_total_results = self.__extract_pagination_total_results()

        self.__update_next_page_endpoint(page_num=2)
        self.__update_transaction_id()

    def __get_first_page_response(
        self,
    ) -> Response:
        return self.__api_client.call_with_response(
            method="GET", url=self.__next_page_endpoint, headers=self.__request_headers, response_models=self.__response_models
        )

    def get_pages(
        self,
    ) -> Generator[Any]:
        r"""Gets pages in a paginated endpoint, sends request per page.

        Returns:
            Generator[Any]: A generator (or iterator) that wraps pages in order.
        """
        if not self.__last_response_headers or not self.__pagination_total_results:
            raise StopIteration()

        for page_num in range(1, self.__pagination_total_results + 1):
            if page_num == 1:
                yield self.__first_page
                continue

            response = self.__api_client.call_with_response(
                method="GET", url=self.__next_page_endpoint, headers=self.__request_headers, response_models=self.__response_models
            )

            self.__last_response_headers, new_page = response.raw.headers, response.body
            self.__update_next_page_endpoint(page_num=page_num)
            self.__update_transaction_id()

            yield new_page

    def is_link_in_last_response_headers(self) -> bool:
        r"""Verifies if a link exists in headers of last received response.

        Returns:
            bool
        """
        return header.LINK in self.__last_response_headers.keys()

    def __update_next_page_endpoint(
        self,
        page_num: int = 1,
    ) -> None:
        is_page_num_out_of_bound: bool = page_num < 1 or page_num > self.__pagination_total_results
        is_last_page: bool = page_num == self.__pagination_total_results
        is_link_missing: bool = not (is_last_page or self.is_link_in_last_response_headers())

        if is_page_num_out_of_bound or is_link_missing or not self.__last_response_headers:  # noqa
            raise StopIteration()

        self.__next_page_endpoint = self.__extract_page_link(self.__last_response_headers)

        if page_num == self.__pagination_total_results:
            self.__next_page_endpoint = self.__first_page_endpoint

    def __update_transaction_id(self):
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
        return self.__next_page_endpoint

    @property
    def first_page(self):
        return self.__first_page

    @property
    def response_models(self):
        return self.__response_models
