from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

from app.routers import router

schema_view = get_swagger_view(title='Mozio Test API')

urlpatterns = [
    path('docs/', schema_view),
    path('api/', include(router.urls)),
]
