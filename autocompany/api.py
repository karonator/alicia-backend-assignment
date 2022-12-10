from rest_framework import routers

from base.viewsets import (
    ProductViewSet
)

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)

urlpatterns = router.urls
