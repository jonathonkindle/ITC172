from django.test import TestCase
# from .models import Meeting, MeetingMinutes, ResourceType, Resource, Event
from .models import Meeting, MeetingMinutes, ResourceType, Resource, Event
# Create your tests here.

class MeetingTest(TestCase):
   def test_string(self):
       meet=Meeting(meetingtitle='New Members')
       self.assertEqual(str(meet), meet.meetingtitle)


   def test_table(self):
       self.assertEqual(str(Meeting._meta.db_table), 'meeting')