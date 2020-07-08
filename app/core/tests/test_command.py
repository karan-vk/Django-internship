from unittest.mock import patch

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import TestCase


class ComandTests(TestCase):
    def test_wait_for_db_ready(self):
        # Test wating for db when db is available
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)
    def test_wait_for_db(self):
        # Test waiting for db
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError]*5+[True]
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)
