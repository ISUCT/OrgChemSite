"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from templatetags.myfilter import cut


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_cut(self):
        text = "some new text"
        res = cut(text,"new")
        self.assertEqual("some ",res)

    #def test_cut_preserve(self):
        #text = "<p>some new text</p>"
        #res = cut(text,"new")
        #self.assertEqual("<p>some </p>",res)
