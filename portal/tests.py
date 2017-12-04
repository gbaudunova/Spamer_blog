from django.test import TestCase, Client
from django.urls import reverse

from .forms import *
from .models import *


_CLIENT = Client()


class PortalTest(TestCase):
    def create_portal(self):
        portal_models = Portal.objects.create(name='name1', user="user1")
        return Portal.objects.create(name='name', user="user")
        self.assertEqual(portal_models.name, 'name1')
        self.assertEqual(portal_models.user, 'user1')

    def test_creation(self):
        new_portal = self.create_portal()
        self.assertTrue(isinstance(new_portal, Portal))
        self.assertEqual(new_portal.__str__(), new_portal.name)


class User_Form_Test(TestCase):

    def test_user_form_valid(self):
        form = PortalForm(data={'name': "us", 'user': "user"})

        self.assertTrue(form.is_valid())


class ViewTest(TestCase):

    def setUp(self):
        self._CLIENT = Client()
        self.user_valid_data = {
            'login': 'login',
            'password': 'password'

        }
        self.valid_data = {
            'name': 'Reddit',
            'user': 'user1'
        }
        self.data = {
            'name': 'Hacker news',
            'portals': 'Hacker news'
        }

    def test_for_connection(self):
        response = self._CLIENT.get('https://127.0.0.1:8000/portal/create/')

        self.assertTemplateUsed('index.html')

        self.assertRedirects(response, '/main/', status_code=302, target_status_code=200)

    def test_for_auth_user(self):
        data = {'login': 'login_user', 'password': 'password_user'}

        response = self._CLIENT.post(reverse('portal:create_portal'), data=data, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_for_auth_user_using_wrong_data(self):
        wrong_data = {'login': 'L', 'password': ''}

        response = self._CLIENT.post(reverse('portal:create_portal'), data=wrong_data, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_for_selected_portal(self):
        response = self._CLIENT.post(reverse('portal:create_portal'), data=self.data)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, '/portal/create/', status_code=302, target_status_code=302)

    def test_if_portal_form_valid_should_return_text_portal_exists_in_your_list(self):
        portal_form = {'name': 'Golang news', 'user': 'admin'}

        portal_models = Portal.objects.create(name='Golang news', user='user1')

        response = self._CLIENT.post(reverse('portal:create_portal'), data=portal_form)

        self.assertEqual(response.status_code, 302)

        self.assertEqual(response.context, "Портал %s  уже существует в вашем списке!" % portal_form['name'])

    # def test_for_create_portal_in_selected_portal(self):
    #     r = self._CLIENT.post(reverse('portal:create_portal'), data=self.valid_data)
    #     self.assertEqual(r.status_code, 302)
    #     self.assertRedirects(r, '/portal/create/', status_code=302, target_status_code=302)

    def test_for_delete_portals(self):

        data = {'login': 'login', 'password': '2323232'}

        response = self._CLIENT.post(reverse('portal:delete_portal', kwargs={'id_portal': 1}), data=data)

        self.assertEqual(response.status_code, 302)

        self.assertRedirects(response, '/main/', status_code=302, target_status_code=200)





