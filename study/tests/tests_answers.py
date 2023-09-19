from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Materials, Answers
from user.models import UserCustom


class AnswersMemberTestCase(APITestCase):
    def setUp(self) -> None:
        test_user = UserCustom.objects.create_user(
            email='test_member@test.ru',
            password='123456',
            role='member'
        )
        self.client.force_authenticate(test_user)

    def test_create_answers(self):
        """Тест на создание ответа пользователем"""
        data = {
            'answer': 'Квантовая',
            'user_answer': 'True',
            'is_correct_answer': 'True',
            'is_user_correct': 'True'
        }
        response = self.client.post(
            '/answers/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )

        self.assertFalse(
            Answers.objects.all().exists()
        )

    def test_update_answers(self):
        """Тест на изменение (выбор) ответа пользователем"""
        answer = Answers.objects.create()

        data = {
            'user_answer': 'True'
        }
        response = self.client.put(
            f'/answers/{answer.pk}/update/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertTrue(
            Answers.objects.filter(pk=answer.pk, user_answer=True).exists()
        )
