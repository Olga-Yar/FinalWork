from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Item
from user.models import UserCustom


class ItemAdminTestCase(APITestCase):
    def setUp(self) -> None:
        test_user = UserCustom.objects.create_user(
            email='test_t@test.ru',
            password='123456',
            role='moderator'
        )
        self.client.force_authenticate(test_user)

    def test_create_item(self):
        """Тест на создание раздела модератором"""
        data = {
            'name': 'Химия',
            'about': 'Раздел о химии'
        }
        response = self.client.post(
            '/item/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Item.objects.all().exists()
        )

    def test_create_item_without_name(self):
        """Тест на создание раздела модератором без названия"""
        data = {
            'about': 'Раздел о химии'
        }
        response = self.client.post(
            '/item/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertFalse(
            Item.objects.all().exists()
        )

    def test_create_item_bad_name(self):
        """Тест на создание раздела модератором с неподходящим названием"""
        data = {
            'name': 'jjjjjj',
            'about': 'Раздел о химии'
        }
        response = self.client.post(
            '/item/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertFalse(
            Item.objects.all().exists()
        )


class ItemMemberTestCase(APITestCase):
    def setUp(self) -> None:
        test_user = UserCustom.objects.create_user(
            email='test_member@test.ru',
            password='123456',
            role='member'
        )
        self.client.force_authenticate(test_user)

    def test_create_item(self):
        """Тест на создание раздела пользователем"""
        data = {
            'name': 'Химия',
            'about': 'Раздел о химии'
        }
        response = self.client.post(
            '/item/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertFalse(
            Item.objects.all().exists()
        )
