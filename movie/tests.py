from django.test import TestCase
from django.urls import reverse

from .models import Movie


# Create your tests here.
class MovieTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.movie = Movie.objects.create(
            title="dummy title",
            description="dummy movie description",
            image="movie/images/movie_image.jpg",
        )

    def test_movie_model(self):
        self.assertEqual(self.movie.title, "dummy title")
        self.assertEqual(self.movie.description, "dummy movie description")
        self.assertEqual(self.movie.image, "movie/images/movie_image.jpg")

    def test_url_exists_at_correct_location_home(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "dummy title")

    def test_url_exists_at_correct_location_signup(self):
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "signup.html")
