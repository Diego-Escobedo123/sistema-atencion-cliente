'''
Unit tests for Priority Queue.
10 scenarios tested.
'''

import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.pq = PriorityQueue()

    # Test 1: Queue starts empty
    def test_01_queue_starts_empty(self):
        self.assertTrue(self.pq.is_empty())
        self.assertEqual(len(self.pq), 0)

    # Test 2: Insert one ticket
    def test_02_insert_one_ticket(self):
        self.pq.insert('Ana Garcia', 'Cannot login', 2)
        self.assertFalse(self.pq.is_empty())
        self.assertEqual(len(self.pq), 1)

    # Test 3: Critical ticket goes first
    def test_03_critical_goes_first(self):
        self.pq.insert('Carlos Lopez', 'Minor issue', 4)
        self.pq.insert('Maria Torres', 'System down', 1)
        self.assertEqual(self.pq.peek().priority, 1)

    # Test 4: Same priority respects FCFS
    def test_04_same_priority_fcfs(self):
        self.pq.insert('Client A', 'Problem A', 2)
        self.pq.insert('Client B', 'Problem B', 2)
        self.assertEqual(self.pq.delete().client, 'Client A')
        self.assertEqual(self.pq.delete().client, 'Client B')

    # Test 5: Delete returns highest priority ticket
    def test_05_delete_returns_highest_priority(self):
        self.pq.insert('Luis Perez', 'General question', 3)
        self.pq.insert('Sofia Diaz', 'Server down', 1)
        self.assertEqual(self.pq.delete().client, 'Sofia Diaz')

    # Test 6: Delete on empty queue returns None
    def test_06_delete_empty_queue(self):
        self.assertIsNone(self.pq.delete())

    # Test 7: Search finds existing ticket
    def test_07_search_existing_ticket(self):
        node = self.pq.insert('Roberto Soto', 'Payment error', 1)
        self.assertIsNotNone(self.pq.search(node.ticket_id))

    # Test 8: Search returns None for non-existing ticket
    def test_08_search_nonexistent_ticket(self):
        self.assertIsNone(self.pq.search('TKT-9999'))

    # Test 9: Update priority repositions ticket
    def test_09_update_priority_repositions(self):
        self.pq.insert('Andres Mora', 'Minor issue', 4)
        node = self.pq.insert('Valeria Rios', 'Occasional error', 3)
        self.pq.update_priority(node.ticket_id, 1)
        self.assertEqual(self.pq.peek().ticket_id, node.ticket_id)

    # Test 10: Correct order with multiple priorities
    def test_10_correct_order_multiple_priorities(self):
        self.pq.insert('D', 'Low', 4)
        self.pq.insert('B', 'High', 2)
        self.pq.insert('A', 'Critical', 1)
        self.pq.insert('C', 'Medium', 3)

        priorities = []
        while not self.pq.is_empty():
            priorities.append(self.pq.delete().priority)
        self.assertEqual(priorities, [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main(verbosity=2)