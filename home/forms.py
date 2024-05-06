from django import forms
from datetime import datetime
from home.models import Contact, EventDate, Ticket, Event
from django.db.models import Q

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=False, max_length=20)
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message', 'phone']



class TicketForm(forms.ModelForm):
    event_date = forms.CharField(widget=forms.HiddenInput())
    # event = forms.CharField()

    class Meta:
        model = Ticket
        fields = ['full_name', 'phone', 'people', 'event_date']

    
    def clean_event_date(self):
        date_str = self.cleaned_data.get('event_date')
        events = EventDate.objects.filter(Q(id=date_str))
        if not events:
            raise forms.ValidationError('Invalid date')
        return events.first()
    
    def clean_people(self):
        people = self.cleaned_data.get('people')
        if people < 1:
            raise forms.ValidationError('Invalid number of people')
        return people
    
    # def save(self, commit=True):
    #     ticket = super().save(commit=False)
    #     print( self.cleaned_data.get('event_date'))
    #     # ticket.event_date = self.cleaned_data.get('event_date')
    #     if commit:
    #         ticket.save()
    #     return ticket

        