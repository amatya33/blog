from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.

from .models import Post

class BlogTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='admin1',
            email='admin1@admin1.com',
            password='admin1'
        )
        self.post = Post.objects.create(
            title = 'A good title',
            body = 'Nice body content',
            author=self.user,
        )
    def test_string_representation(self):
        post = Post(title='A sample title')
        self.assertEqual(str(post), post.title)

    # def test_post_content(self):
    #     self.assertEqual(f'{self.post.title}', 'A good title')
    #     self.assertEqual(f'{self.post.title}', 'A good title')
    #     self.assertEqual(f'{self.post.title}', 'A good title')

