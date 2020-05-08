from django.contrib.auth.models import User
from django.db import models


class TicketStatus(models.Model):
    name = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Ticket Statuses"

    def __str__(self):
        return self.name


class Ticket(models.Model):
    date_opened = models.DateTimeField()
    date_closed = models.DateTimeField(
        blank=True,
        null=True,
    )
    ticket_uid = models.CharField(max_length=16)
    status_id = models.ForeignKey(
        TicketStatus,
        on_delete=models.DO_NOTHING,
        related_name='ticket_status',
    )
    title = models.CharField(max_length=500)
    ticket_description = models.CharField(max_length=500)
    solution = models.CharField(max_length=500)
    released_user_id = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='ticket_released_by',
    )
    reporting_user_id = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        related_name='ticket_reporting_iser'
    )

    class Meta:
        verbose_name_plural = "Tickets"

    def __str__(self):
        return self.ticket_uid
