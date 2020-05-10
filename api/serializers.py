from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class SafeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'last_login',
            'first_name',
            'last_name',
            'email',
            'username',
        )


class TicketStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketStatus
        fields = '__all__'


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'


class ListTicketSerializer(serializers.HyperlinkedModelSerializer):
    status = TicketStatusSerializer(required=True)
    released_user = SafeUserSerializer(required=True)
    reporting_user = SafeUserSerializer(required=True)

    class Meta:
        model = Ticket
        fields = (
            'date_opened',
            'date_closed',
            'status',
            'title',
            'ticket_description',
            'solution',
            'released_user',
            'reporting_user',
        )


class TicketEvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketSolutionEvidence
        fields = '__all__'


class TicketEvidenceListSerializer(serializers.HyperlinkedModelSerializer):
    uploader = SafeUserSerializer(required=True)
    ticket = TicketSerializer(required=True)

    class Meta:
        model = TicketSolutionEvidence
        fields = (
            'file_data',
            'file_name',
            'ticket',
            'uploader',
        )
