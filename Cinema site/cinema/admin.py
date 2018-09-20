from django.contrib import admin

from .models import Film,Session,Hall,Ticket
admin.site.register(Film)
admin.site.register(Session)
admin.site.register(Hall)
admin.site.register(Ticket)