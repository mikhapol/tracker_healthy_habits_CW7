from rest_framework.pagination import PageNumberPagination


class HabitPaginator(PageNumberPagination):
    """
    Для вывода списка привычек реализовать
    пагинацию с выводом по 5 привычек на страницу.
    """

    page_size = 5
