from django.contrib import admin
from api.models import *

# Register your models here.
admin.site.register(Ticket)
admin.site.register(TicketStatus)
admin.site.register(TicketSolutionEvidence)
