# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Event
from datetime import datetime

class EventAPITests(TestCase):
    def setUp(self):

        Event.objects.create(title="Evento 1", description="Descripción 1", date_time="2024-12-12T10:00:00Z", location="Bogotá", category="Conferencia")
        Event.objects.create(title="Evento 2", description="Descripción 2", date_time="2024-12-13T10:00:00Z", location="Ibagué", category="Taller")
        Event.objects.create(title="Evento 3", description="Descripción 3", date_time="2024-12-14T10:00:00Z", location="Bogotá", category="Conferencia")
        Event.objects.create(title="Evento 4", description="Descripción 4", date_time="2024-12-12T10:00:00Z", location="Cali", category="Conferencia")

        self.client = APIClient()

    def test_get_all_events(self):
        """Probar la obtención de todos los eventos sin filtros"""
        response = self.client.get('/api/events/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_filter_by_category(self):
        """Probar el filtrado de eventos por categoría"""
        response = self.client.get('/api/events/filter/', {'category': 'Conferencia'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3) 

    def test_filter_by_date(self):
        """Probar el filtrado de eventos por fecha"""
        response = self.client.get('/api/events/filter/', {'date_time': '2024-12-12T10:00:00Z'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_filter_by_location(self):
        """Probar el filtrado de eventos por ubicación"""
        response = self.client.get('/api/events/filter/', {'location': 'Bogotá'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  

    def test_filter_no_results(self):
        """Probar el filtrado sin resultados"""
        response = self.client.get('/api/events/filter/', {'category': 'Deporte'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0) 

    def test_combined_filters(self):
        """Probar el filtrado combinado por categoría y ubicación"""
        response = self.client.get('/api/events/filter/', {'category': 'Conferencia', 'location': 'Bogotá'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2) 

    def test_invalid_filter(self):
        """Probar un filtro inválido"""
        response = self.client.get('/api/events/filter/', {'invalid_filter': 'test'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST) 
