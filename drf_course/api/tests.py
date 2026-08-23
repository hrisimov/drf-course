from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.models import Order

UserModel = get_user_model()


class UserOrdersTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user1 = UserModel.objects.create_user(
            username='user1',
            password='test',
        )
        cls.user2 = UserModel.objects.create_user(
            username='user2',
            password='test',
        )
        Order.objects.create(
            user=cls.user1,
        )
        Order.objects.create(
            user=cls.user1,
        )
        Order.objects.create(
            user=cls.user2,
        )
        Order.objects.create(
            user=cls.user2,
        )

    def test_get__when_user_is_authenticated__expect_to_return_only_his_orders(self):
        self.client.force_login(self.user1)

        response = self.client.get(reverse('user-orders'))

        assert response.status_code == status.HTTP_200_OK
        orders = response.json()
        self.assertTrue(all(order['user'] == self.user1.pk for order in orders))
