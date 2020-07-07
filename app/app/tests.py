from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """ Test to add two numbers"""
        self.assertEqual(add(2, 5), 7)

    def test_subtarct_and_return(self):
        """Subtracted """
        self.assertEquals(subtract(2, 1), 1)
