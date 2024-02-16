from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AddressViewset,
    CategoryViewset,
    StoreViewset,
    ItemViewset
)

app_name = 'prime'

router = DefaultRouter()
router.register('address', AddressViewset)
router.register("categories", CategoryViewset)
router.register("stores", StoreViewset)
router.register("items", ItemViewset)


urlpatterns = [
    path('', include(router.urls)),
    path(
            "stores/image/<int:pk>/",
            StoreViewset.as_view({"put": "upload_store_image"})
        ),
    path(
            "items/image/<int:pk>/",
            ItemViewset.as_view({"put": "upload_item_image"})
        )
]
