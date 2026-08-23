from django.contrib.auth import get_user_model
from django.test import TestCase

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
