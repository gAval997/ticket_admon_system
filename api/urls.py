from django.urls import include, path
from rest_framework import routers
from api import views
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register(r'ticket', views.TicketViewSet)
router.register(r'ticket-list', views.TicketListViewSet)
router.register(r'ticket-status', views.TicketStatusViewSet)
router.register(r'user', views.SafeUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', views.CustomObtainAuthToken.as_view(), name='api_token_auth'),
]