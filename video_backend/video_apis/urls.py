from .api import PlaceViewSet, BookingViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = router.urls
