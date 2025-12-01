# users/tests.py
from django.test import TestCase
from django.contrib.auth.models import User


class UserModelTest(TestCase):
    """Тесты для пользователей"""

    def test_create_user(self):
        """Тест создания пользователя"""
        print("👤 Тест: Создание пользователя...")

        user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('testpass123'))

        print(f"✅ Пользователь {user.username} создан")

    def test_create_superuser(self):
        """Тест создания суперпользователя"""
        print("👑 Тест: Создание суперпользователя...")

        admin = User.objects.create_superuser(
            username='admin',
            password='adminpass123',
            email='admin@example.com'
        )

        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_staff)

        print(f"✅ Суперпользователь {admin.username} создан")
