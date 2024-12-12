import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    date_time = django_filters.DateFilter(field_name="date_time", lookup_expr='exact')
    category = django_filters.CharFilter(field_name="category", lookup_expr='icontains')

    class Meta:
        model = Event
        fields = ['date_time', 'category', 'location']
