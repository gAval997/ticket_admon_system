from rest_framework import viewsets
from api.serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from tickets_backend.settings import DEVELOPMENT


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({
            'token': token.key,
            'uid': token.user_id
        })


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    if not DEVELOPMENT:
        permission_classes = (IsAuthenticated,)

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class SafeUserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed (only safe data).
    """
    if not DEVELOPMENT:
        permission_classes = (IsAuthenticated,)

    queryset = User.objects.all()
    serializer_class = SafeUserSerializer


class TicketStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """
    if not DEVELOPMENT:
        permission_classes = (IsAuthenticated,)

    queryset = TicketStatus.objects.all()
    serializer_class = TicketStatusSerializer


class TicketViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be viewed or edited.
    """
    if not DEVELOPMENT:
        permission_classes = (IsAuthenticated,)

    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class TicketListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tickets to be listed (with foreign keys data).
    """
    if not DEVELOPMENT:
        permission_classes = (IsAuthenticated,)

    queryset = TicketSolutionEvidence.objects.all()
    serializer_class = ListTicketSerializer


class TicketEvidenceViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows tickets evidences to be viewed or edited.
        """
    if not DEVELOPMENT:
        permission_classes = (IsAuthenticated,)

    queryset = TicketSolutionEvidence.objects.all()
    serializer_class = TicketEvidenceSerializer


class TicketEvidenceListViewSet(viewsets.ModelViewSet):
    """
        API endpoint that allows tickets evidences to be viewed or edited.
        """
    if not DEVELOPMENT:
        permission_classes = (IsAuthenticated,)

    queryset = TicketSolutionEvidence.objects.all()
    serializer_class = TicketEvidenceListSerializer
