from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    AddressViewset
)

app_name = 'prime'

router = DefaultRouter()
router.register('address', AddressViewset)
urlpatterns = [
    path('', include(router.urls))
]
