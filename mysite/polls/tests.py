from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from django.test import TestCase
from polls.models import Poll


class PollMethodTests(TestCase):

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
