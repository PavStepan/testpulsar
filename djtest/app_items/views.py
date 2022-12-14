from rest_framework.viewsets import ReadOnlyModelViewSet
from app_items.serializer import ItemSerializer
from app_items.models import ItemModel


class ItemViewSet(ReadOnlyModelViewSet):
    """ Представление для получения списка товаров """

    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = ItemModel.objects.all()
        status = self.request.query_params.get('status')
        code = self.request.query_params.get('code')
        title = self.request.query_params.get('title')
        if status:
            queryset = queryset.filter(status=status)
        if code:
            queryset = queryset.filter(code=code)
        if title:
            queryset = queryset.filter(title=title)

        return queryset
