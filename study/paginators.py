from rest_framework.pagination import PageNumberPagination


class ItemPaginator(PageNumberPagination):
    page_size = 5
    page_query_param = 'page-size'
    max_page_size = 50
