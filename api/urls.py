from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'ticket-status', views.TicketStatusViewSet)
router.register(r'ticket', views.TicketViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]