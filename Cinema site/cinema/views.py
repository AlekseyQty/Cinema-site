from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.db.models import Max

from .models import *

def IndexView(request):
    films = Film.objects.all()
    return render(request,'index.html',{'latest_film_list':films})

def SessionView(request,pk):
    sessions = Session.objects.select_related().filter(film_name_id = pk)
    return render(request,'session.html',{'session_list':sessions})

def DetailView(request,pk):
    tickets = Ticket.objects.filter(ticket_session_id = pk)
    maxval_col = tickets.aggregate(Max('ticket_col'))
    maxval_col_value = maxval_col['ticket_col__max']
    maxval_row = tickets.aggregate(Max('ticket_row'))
    maxval_row_value = maxval_row['ticket_row__max']
    
    ticket_array = [[0 for x in range(maxval_row_value)] for y in range(maxval_col_value)]
    i = 0
    j = 0

    while (i < maxval_col_value):
        while (j < maxval_row_value):
            ticket_array[i][j] = Ticket.objects.get(ticket_session_id = pk, ticket_col = i+1, ticket_row = j+1)
            j = j+1
        j = 0
        i = i+1
    return render(request,'test_temp.html',{'ticket_list':ticket_array,'ticket_session_id':pk})

def PurchaseView(request,pk):
    if (request.method == 'POST'):
        check_array = request.POST.getlist('seat[]')
    if (check_array):
        seat_array = []
        total_price = 0
        for num in check_array:
            seat_array.append(Ticket.objects.get(ticket_session_id = pk, id = num))
        for s in seat_array:
            total_price = total_price + s.ticket_price
        request.session.set_expiry(60)
        request.session['seats'] = []
        request.session['seats'] = check_array
        request.session['session_id'] = pk
    else:
        return render(request,'index.html')
    return render(request,'purcashe.html', {'seat_list':seat_array,'total_price':total_price,'session_id':pk})

def EndView(request):
    for s in request.session['seats']:
        t = Ticket.objects.get(ticket_session_id = request.session['session_id'],id = s)
        t.ticket_sold = 1
        t.save()
    return render(request,'detail.html')

def MainIndexView(request):
    return render(request,'base.html')