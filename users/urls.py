from rest_framework.routers import SimpleRouter
from users.viewsets import UserViewSet


router = SimpleRouter()
router.register('accounts', UserViewSet)


urlpatterns = router.urls
