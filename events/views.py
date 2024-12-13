from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer
from .filters import EventFilter
from rest_framework.exceptions import ValidationError


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category', 'title', 'date_time']

class EventDetail(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class RegisterEvent(generics.CreateAPIView):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

class FilteredEventsView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EventFilter
    
    def get_queryset(self):
        valid_filters = ['title', 'category', 'date_time','location']
        filters = self.request.query_params

        for key in filters.keys():
            if key not in valid_filters:
                raise ValidationError(f"El filtro '{key}' no es válido.")

        return super().get_queryset()
