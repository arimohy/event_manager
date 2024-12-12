from django.urls import path
from .views import EventList, EventDetail, RegisterEvent , FilteredEventsView

urlpatterns = [
    path('events/', EventList.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetail.as_view(), name='event-detail'),
    path('register/', RegisterEvent.as_view(), name='register-event'),
    path('events/filter/', FilteredEventsView.as_view(), name='event-filter'),

]
