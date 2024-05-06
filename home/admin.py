from django.contrib import admin
from .models import Location, Category, Event, EventDate, Ticket, About, EventImages, Contact
# Register your models here.

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'phone']
    search_fields = ['name', 'city', 'phone']
    list_filter = ['city']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


class EventDateInline(admin.TabularInline):
    model = EventDate
    extra = 1

class EventImagesInline(admin.TabularInline):
    model = EventImages
    extra = 1

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    inlines = [EventDateInline, EventImagesInline]
    list_display = ['name', 'location', 'category']
    search_fields = ['name', 'location__name', 'category__name']
    list_filter = ['location', 'category']


class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 1


@admin.register(EventDate)
class EventDateAdmin(admin.ModelAdmin):
    inlines = [TicketInline]
    list_display = ['event', 'date', 'start_time', 'end_time', 'price', 'seats', 'get_seats']
    search_fields = ['event__name', 'date', 'start_time', 'end_time', 'price', 'seats']
    list_filter = ['event', 'date', 'price', 'seats']

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'phone', 'event_date', 'created_at']
    search_fields = ['full_name', 'phone', 'event_date__event__name']
    list_filter = ['event_date', 'created_at']


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['title', 'subtitle']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'message', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    list_filter = ['created_at']