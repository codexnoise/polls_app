import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question

# TEST OF MODELS


class QuestionModelTest(TestCase):
    def test_was_publish_recently_with_future_questions(self):
        """"was_publish_recently() retuns False for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(
            question_text="Quien es el mejor CD of Platzi", pub_date=time)
        self.assertIs(future_question.was_publish_recently(), False)
