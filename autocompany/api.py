from rest_framework import routers

from base.viewsets import (
    ProductViewSet,
    CartItemViewSet
)

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'cart_item', CartItemViewSet, basename='cart_item')

urlpatterns = router.urls
