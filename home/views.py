from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from home.forms import ContactForm, TicketForm
from .models import *
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

class HomePageView(View):
    def get(self, request):
        events = Event.objects.all().filter(is_active=True).order_by('-id')[:9]
        categories = Category.objects.all().filter(is_active=True)
        context = {
            'events': events,
            'categories': categories
        }
        return render(request, 'index.html', context)
    

class AllEventsView(View):
    def get(self, request):
        events = Event.objects.all().filter(is_active=True)
        context = {
            'events': events
        }
        return render(request, 'all-events.html', context)
    


class EventDetailView(View):
    form_class = TicketForm
    def get(self, request, pk):
        event = Event.objects.get(id=pk)
        other_events = Event.objects.all().filter(is_active=True).exclude(id=pk).order_by('-id')[:6]
        
        context = {
            'event': event,
            'other_events': other_events,
        }
        return render(request, 'detail.html', context)
    
    def post(self, request, pk):
        event = Event.objects.get(id=pk)
        other_events = Event.objects.all().filter(is_active=True).exclude(id=pk).order_by('-id')[:6]
        
        context = {
            'event': event,
            'other_events': other_events,
        }
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ticket', pk=form.instance.id)
        return  render(request, 'detail.html', context)

      

class ContactUsView(View):
    form_class = ContactForm
    def get(self, request):
        form = self.form_class()
        context = {
            'form': form
        }
        return render(request, 'contacts.html', context)
    
    def post(self, request):
        print(request.POST)
        form = self.form_class(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return render(request, 'contacts.html', {'success': True})
        return render(request, 'contacts.html', {'form': form})
    


class TicketView(View):
    def get(self, request, pk):
        ticket = Ticket.objects.get(id=pk)
        context = {
            'ticket': ticket
        }
        return render(request, 'ticket.html', context)
    

    