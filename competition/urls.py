from django.urls import path
from . import views

from rest_framework.routers import SimpleRouter

from competition.views import PhotoPostViewSet

router = SimpleRouter()

router.register(r'gallery', PhotoPostViewSet)

urlpatterns = [
    path('', views.HomePageView.as_view(), name='main'),

]

urlpatterns += router.urls