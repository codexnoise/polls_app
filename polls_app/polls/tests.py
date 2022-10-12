import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

# TEST OF MODELS


class QuestionModelTest(TestCase):
    def setUp(self):
        self.question = Question(
            question_text="Quien es el mejor CD de Platzi?")

    def test_was_publish_recently_with_future_questions(self):
        """"was_publish_recently() retuns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        self.question.pub_date = time
        self.assertIs(self.question.was_publish_recently(), False)

    def test_was_publish_recently_with_present_questions(self):
        """"was_publish_recently() retuns True for questions whose pub_date is in the present"""
        time = timezone.now() - datetime.timedelta(hours=23)
        self.question.pub_date = time
        self.assertIs(self.question.was_publish_recently(), True)

    def test_was_publish_recently_with_past_questions(self):
        """"was_publish_recently() retuns False for questions whose pub_date is in the past"""
        time = timezone.now() - datetime.timedelta(days=1, minutes=1)
        self.question.pub_date = time
        self.assertIs(self.question.was_publish_recently(), False)
