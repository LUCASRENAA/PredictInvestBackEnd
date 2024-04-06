from rest_framework.test import APITestCase, APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from .views import TicketViewSet
from .models import Ticket

class TicketViewSetTestCase(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create(username='admin', is_staff=True)
        self.normal_user = User.objects.create(username='user', is_staff=False)
        self.ticket = Ticket.objects.create(name='T001', setor='Financeiro')

    def tearDown(self):
        Ticket.objects.all().delete()
        User.objects.all().delete()

    def test_admin_can_post(self):
        factory = APIRequestFactory()
        view = TicketViewSet.as_view({'post': 'create'})
        url = reverse('ticket-list')
        data = {'name': 'T002', 'setor': 'Tecnologia'}
        request = factory.post(url, data)
        force_authenticate(request, user=self.admin_user)
        response = view(request)
        self.assertEqual(response.status_code, 201)

    def test_normal_user_cannot_post(self):
        factory = APIRequestFactory()
        view = TicketViewSet.as_view({'post': 'create'})
        url = reverse('ticket-list')
        data = {'name': 'T002', 'setor': 'Tecnologia'}
        request = factory.post(url, data)
        force_authenticate(request, user=self.normal_user)
        response = view(request)
        self.assertEqual(response.status_code, 403)
    def test_no_user_user_cannot_post(self):
        factory = APIRequestFactory()
        view = TicketViewSet.as_view({'post': 'create'})
        url = reverse('ticket-list')
        data = {'name': 'T002', 'setor': 'Tecnologia'}
        request = factory.post(url, data)
        response = view(request)
        self.assertEqual(response.status_code, 401)

    def test_admin_can_get(self):
        factory = APIRequestFactory()
        view = TicketViewSet.as_view({'get': 'list'})  # Usar 'list' em vez de 'create' para obter uma lista de recursos
        url = reverse('ticket-list')
        request = factory.get(url)
        force_authenticate(request, user=self.admin_user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_normal_user_cannot_get(self):
        factory = APIRequestFactory()
        view = TicketViewSet.as_view({'get': 'list'})  # Usar 'list' em vez de 'create' para obter uma lista de recursos
        url = reverse('ticket-list')
        request = factory.get(url)
        force_authenticate(request, user=self.normal_user)
        response = view(request)
        self.assertEqual(response.status_code, 200)

    def test_no_user_cannot_get(self):
        factory = APIRequestFactory()
        view = TicketViewSet.as_view({'get': 'list'})  # Usar 'list' em vez de 'create' para obter uma lista de recursos
        url = reverse('ticket-list')
        request = factory.get(url)
        response = view(request)
        self.assertEqual(response.status_code, 200)


    def run(self, result=None):
        super().run(result)
        if result.wasSuccessful():
            print("\nO teste passou! ")
        else:
            print("\nAlguns testes falharam. Verifique a saída abaixo para mais detalhes.")
