from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, PetViewSet, DoctorViewSet, AppointmentViewSet

router = DefaultRouter()
router.register(r'owners', OwnerViewSet, basename='owner')
router.register(r'pets', PetViewSet, basename='pet')
router.register(r'procedures', DoctorViewSet, basename='procedure')
router.register(r'medical-records', AppointmentViewSet, basename='medical-record')

urlpatterns = [
    path('', include(router.urls)),
]