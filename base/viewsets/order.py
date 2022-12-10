from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin

from base.models import Order
from base.serializers import OrderSerializer


class OrderViewSet(CreateModelMixin, ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.request.user.id is not None:
            items = Order.objects.filter(user=self.request.user)
            return items
        return []
