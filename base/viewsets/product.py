from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.permissions import AllowAny

from base.models import Product
from base.serializers import ProductShortSerializer, ProductFullSerializer


class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "list":
            return ProductShortSerializer
        if self.action == "retrieve":
            return ProductFullSerializer
        return None
