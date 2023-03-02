from django.urls import path, include
from rest_framework import routers
from core.utils.views_redoc import schema_view
from core.views import UserViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet, basename='user_set')

urlpatterns = [
    path('', include(router.urls)),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
