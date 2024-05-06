from django.db import models
from .utilits import BaseModel, VerifyEmailCode


class Location(BaseModel):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='location/', null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.name
    

class Category(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Event(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='events')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events')
    banner_image = models.ImageField(upload_to='event/', null=True, blank=True)
    card_image = models.ImageField(upload_to='event/', null=True, blank=True)

    def __str__(self):
        return self.name
    

class EventDate(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_dates')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.IntegerField(default=10000)
    seats = models.IntegerField(default=1)

    def __str__(self):
        return self.event.name
    
    @property
    def is_full(self):
        return self.tickets.count() >= self.seats
    
    @property
    def get_seats(self):
        return self.seats - self.tickets.count()

    

class Ticket(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    event_date = models.ForeignKey(EventDate, on_delete=models.CASCADE, related_name='tickets')
    people = models.IntegerField(default=1)
    ticket_number = models.CharField(null=True, blank=True, max_length=255)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.ticket_number
    
    def save(self, *args, **kwargs):
        if not self.ticket_number:
            self.ticket_number = VerifyEmailCode().new_code()
        super(Ticket, self).save(*args, **kwargs)