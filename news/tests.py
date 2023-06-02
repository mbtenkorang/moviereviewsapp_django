from django.test import TestCase
from django.urls import reverse

from .models import News


# Create your tests here.
class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.news = News.objects.create(
            headline="breaking news", body="the news in detail", date="2022-01-01"
        )

    def test_news_model(self):
        self.assertEqual(self.news.headline, "breaking news")
        self.assertEqual(self.news.body, "the news in detail")
        self.assertEqual(self.news.date, "2022-01-01")

    def test_url_exists_at_correct_location_news(self):
        response = self.client.get(reverse("news"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "news.html")
