from rest_framework import pagination


class StandardResultSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_query_param = 'page'
    page_size_query_param = 'pg_size'
    max_page_size = 50