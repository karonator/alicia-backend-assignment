from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from base.models import CartItem
from base.serializers import CartItemSerializer, CartItemFullSerializer


class CartItemViewSet(CreateModelMixin, DestroyModelMixin, ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CartItemFullSerializer
        return CartItemSerializer

    def get_queryset(self):
        if self.request.user.id is not None:
            items = CartItem.objects.filter(user=self.request.user)
            return items
        return []
