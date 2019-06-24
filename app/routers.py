from rest_framework.routers import SimpleRouter

from app.views import ProviderViewSet, ServiceAreaViewSet

router = SimpleRouter()
router.register('providers', ProviderViewSet)
router.register('service_areas', ServiceAreaViewSet)
