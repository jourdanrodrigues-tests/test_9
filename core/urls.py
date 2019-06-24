from django.urls import path, include

from app.routers import router

urlpatterns = [
    path('api/', include(router.urls)),
]
