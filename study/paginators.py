from rest_framework.pagination import PageNumberPagination


class ItemPaginator(PageNumberPagination):
    page_size = 2
    page_query_param = 'page-size'
    max_page_size = 50
