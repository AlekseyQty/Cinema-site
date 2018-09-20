from django.core.management.base import BaseCommand
from cinema.models import *

class Command(BaseCommand):
    def create_tickets(self,hall_id,session_id):
    	hall = Hall.objects.get(id = hall_id)
    	i = 1 
    	j = 1
    	while (i <= hall.hall_cols):
    		while (j <= hall.hall_rows):
    			t = Ticket(ticket_col = i,ticket_row = j, ticket_sold = False, ticket_price = hall.hall_price,ticket_session_id = session_id)
    			t.save()
    			j = j+1
    		j = 1
    		i = i+1

    def handle(self, *args, **options):
        self.create_tickets(2,4)