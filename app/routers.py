from rest_framework.routers import SimpleRouter

from app.views import ProviderViewSet

router = SimpleRouter()
router.register('providers', ProviderViewSet)
