from django.db import models

class Film(models.Model):
    film_name = models.CharField(max_length=100)
    def __str__(self):
    	return self.film_name

class Hall(models.Model):
	hall_name = models.CharField(max_length = 100)
	hall_price = models.IntegerField()
	hall_rows = models.IntegerField()
	hall_cols = models.IntegerField()
	def __str__(self):
		return self.hall_name

class Session(models.Model):
    film_name = models.ForeignKey(Film,on_delete=models.CASCADE)
    hall_name = models.ForeignKey(Hall,on_delete = models.CASCADE)
    session_name = models.CharField(max_length=100)
    session_time = models.TimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
    	return self.session_name

class Ticket(models.Model):
	ticket_session = models.ForeignKey(Session,on_delete=models.CASCADE)
	ticket_row = models.IntegerField()
	ticket_price = models.IntegerField()
	ticket_col = models.IntegerField()
	ticket_sold = models.BooleanField(default = False)
