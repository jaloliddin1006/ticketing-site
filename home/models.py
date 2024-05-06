from django.db import models
from .utilits import BaseModel, VerifyEmailCode
from PIL import Image
import qrcode
from ckeditor.fields import RichTextField
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
    
    @property
    def get_events(self):
        return self.events.all().filter(is_active=True)
    

class Event(BaseModel):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='events')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='events')
    banner_image = models.ImageField(upload_to='event/', null=True, blank=True)
    card_image = models.ImageField(upload_to='event/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.card_image.path)
        o_size = (370,395)
        img.thumbnail(o_size)
        img.save(self.card_image.path, quality=50)

        img = Image.open(self.banner_image.path)
        o_size = (1920,1149)
        img.thumbnail(o_size)
        img.save(self.banner_image.path)

class EventDate(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='event_dates')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    price = models.IntegerField(default=10000)
    seats = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.event.name} - {self.date}"
    
    @property
    def is_full(self):
        return self.get_seats >= self.seats+1
    
    @property
    def get_seats(self):
        seats =  self.tickets.all().aggregate(models.Sum('people', defoult=0))['people__sum']
        if seats:
            return self.seats - seats
        return self.seats

    

class Ticket(BaseModel):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    event_date = models.ForeignKey(EventDate, on_delete=models.CASCADE, related_name='tickets')
    people = models.IntegerField(default=1)
    ticket_number = models.CharField(null=True, blank=True, max_length=255)
    qr_code = models.ImageField(upload_to='ticket/', null=True, blank=True)
    is_sold = models.BooleanField(default=False)

    def __str__(self):
        return self.ticket_number
    
    def save(self, *args, **kwargs):
        if not self.ticket_number:
            s = VerifyEmailCode()
            self.ticket_number = s.new_code()
                
            img = qrcode.make(f'#{self.id}-{self.ticket_number}-{self.event_date.event.name}')
            img.save(f"media/ticket/{self.id}_{self.ticket_number}.png")
            
            self.qr_code = f'ticket/{self.id}_{self.ticket_number}.png'

        super(Ticket, self).save(*args, **kwargs)
        



class About(BaseModel):
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=355)
    body = RichTextField()
    image = models.ImageField(upload_to='about/', null=True, blank=True)
    telegram_url = models.URLField(null=True, blank=True)
    instagram_url = models.URLField(null=True, blank=True)
    facebook_url = models.URLField(null=True, blank=True)
    twitter_url = models.URLField(null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title
    


class EventImages(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='event/', null=True, blank=True)

    def __str__(self):
        return self.event.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        o_size = (640,429)
        img.thumbnail(o_size)
        img.save(self.image.path, quality=50)



class Contact(BaseModel):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.name