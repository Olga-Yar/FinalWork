from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Materials
from user.models import UserCustom


class MaterialsAdminTestCase(APITestCase):
    def setUp(self) -> None:
        test_user = UserCustom.objects.create_user(
            email='test_t@test.ru',
            password='123456',
            role='moderator'
        )
        self.client.force_authenticate(test_user)

    def test_create_materials(self):
        """Тест на создание подраздела модератором"""
        data = {
            'name_m': 'Квантовая'
        }
        response = self.client.post(
            '/materials/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Materials.objects.all().exists()
        )

    def test_create_materials_empty_name(self):
        """Тест на создание подраздела модератором без названия"""
        data = {
            'name_m': ''
        }
        response = self.client.post(
            '/materials/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertFalse(
            Materials.objects.all().exists()
        )

    def test_create_materials_step_name(self):
        """Тест на создание подраздела модератором с неподходящим названием"""
        data = {
            'name_m': ' '
        }
        response = self.client.post(
            '/materials/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )

        self.assertFalse(
            Materials.objects.all().exists()
        )


class MaterialsMemberTestCase(APITestCase):
    def setUp(self) -> None:
        test_user = UserCustom.objects.create_user(
            email='test_member@test.ru',
            password='123456',
            role='member'
        )
        self.client.force_authenticate(test_user)

    def test_create_materials(self):
        """Тест на создание подраздела пользователем"""
        data = {
            'name_m': 'Квантовая'
        }
        response = self.client.post(
            '/materials/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

        self.assertFalse(
            Materials.objects.all().exists()
        )
