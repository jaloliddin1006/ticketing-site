from django.urls import path
from .views import HomePageView, EventDetailView, ContactUsView, TicketView, AllEventsView

urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
    path('ticket/<int:pk>/', TicketView.as_view(), name='ticket'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
    path('contact/', ContactUsView.as_view(), name='contact'),
    path('events/', AllEventsView.as_view(), name='all_events'),

]