from rest_framework.routers import SimpleRouter
from users.viewsets import UserViewSet, JWTViewSet


router = SimpleRouter()
router.register("accounts", UserViewSet)
router.register("auth", JWTViewSet)


urlpatterns = router.urls
