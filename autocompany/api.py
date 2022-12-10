from rest_framework import routers

from base.viewsets import (
    ProductViewSet,
    CartItemViewSet,
    OrderViewSet
)

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'cart_item', CartItemViewSet, basename='cart_item')
router.register(r'order', OrderViewSet, basename='order')


urlpatterns = router.urls
