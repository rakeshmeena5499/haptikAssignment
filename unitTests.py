from task1 import most_active_user
from task3 import can_create
import unittest


class TestProblems(unittest.TestCase):

    def test_can_create(self):
        self.assertEqual(can_create(['back','end','front','tree'],'backend'), True)
        self.assertEqual(can_create(['back','end','front','tree'],'frontyard'), False)
        self.assertEqual(can_create(['back','end','front','tree'],'frontend'), True)

    def test_most_active_users(self):
    	self.assertEqual(most_active_user('chats.txt'), ['John', 'Ram', 'Adam'])


if __name__ == '__main__':
    unittest.main()