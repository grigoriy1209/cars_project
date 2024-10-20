from rest_framework.pagination import PageNumberPagination as Pagination
from rest_framework.response import Response


class PageNumberPagination(Pagination):
    page_size = 3
    max_page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        return Response(
            {
                'total_items': count,
                'total_page': self.page.paginator.num_pages,
                'previous_page': bool(self.page.previous_link()),
                'next_page': bool(self.page.next_link()),
                'results': data,
            }
        )
