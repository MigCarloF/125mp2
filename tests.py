import unittest
import manager
import scheduler
from process import Process

class TestProcesses(unittest.TestCase):

    def test_create_processes(self):
        processes = manager.create_processes("./tests/test.txt")
        self.assertEqual(len(processes), 6)
        
        with self.assertRaises(manager.IncorrectFirstRowException):
            manager.create_processes("./tests/test2.txt")
        
        with self.assertRaises(manager.ValueQuantityException):
            manager.create_processes("./tests/test3.txt")

class TestScheduler(unittest.TestCase):
    def test_fcfs(self):
        processes = scheduler.fcfs(manager.create_processes("./tests/test.txt"))
        self.assertEqual(processes[0].turnaround_time, 4)
        self.assertEqual(processes[1].turnaround_time, 7)
        self.assertEqual(processes[2].turnaround_time, 10)
        self.assertEqual(processes[3].turnaround_time, 16)
        self.assertEqual(processes[4].turnaround_time, 22)
        self.assertEqual(processes[5].turnaround_time, 29)
        self.assertEqual(processes[0].waiting_time, 0)
        self.assertEqual(processes[1].waiting_time, 3)
        self.assertEqual(processes[2].waiting_time, 5)
        self.assertEqual(processes[3].waiting_time, 7)
        self.assertEqual(processes[4].waiting_time, 12)
        self.assertEqual(processes[5].waiting_time, 17)

        processes = scheduler.fcfs(manager.create_processes("./tests/process3.txt"))
        self.assertEqual(processes[0].turnaround_time, 3)
        self.assertEqual(processes[1].turnaround_time, 18)
        self.assertEqual(processes[2].turnaround_time, 29)
        self.assertEqual(processes[3].turnaround_time, 38)
        self.assertEqual(processes[0].waiting_time, 0)
        self.assertEqual(processes[1].waiting_time, 2)
        self.assertEqual(processes[2].waiting_time, 16)
        self.assertEqual(processes[3].waiting_time, 26)

    def test_sjf(self):
        processes = scheduler.sjf(manager.create_processes("./tests/process3.txt"))
        self.assertEqual(processes[0].turnaround_time, 3)
        self.assertEqual(processes[1].turnaround_time, 12)
        self.assertEqual(processes[2].turnaround_time, 23)
        self.assertEqual(processes[3].turnaround_time, 38)
        self.assertEqual(processes[0].waiting_time, 0)
        self.assertEqual(processes[1].waiting_time, 0)
        self.assertEqual(processes[2].waiting_time, 10)
        self.assertEqual(processes[3].waiting_time, 22)

    def test_priority(self):
        processes = scheduler.priority(manager.create_processes("./tests/process4.txt"))
        self.assertEqual(processes[0].turnaround_time, 3)
        self.assertEqual(processes[1].turnaround_time, 18)
        self.assertEqual(processes[2].turnaround_time, 29)
        self.assertEqual(processes[3].turnaround_time, 38)
        self.assertEqual(processes[0].waiting_time, 0)
        self.assertEqual(processes[1].waiting_time, 2)
        self.assertEqual(processes[2].waiting_time, 16)
        self.assertEqual(processes[3].waiting_time, 26)

    def test_srpt(self):
        processes = scheduler.srpt(manager.create_processes("./tests/process5.txt"))
        self.assertEqual(processes[0].turnaround_time, 9)
        self.assertEqual(processes[1].turnaround_time, 14)
        self.assertEqual(processes[2].turnaround_time, 25)
        self.assertEqual(processes[3].turnaround_time, 41)
        self.assertEqual(processes[0].waiting_time, 0)
        self.assertEqual(processes[1].waiting_time, 3)
        self.assertEqual(processes[2].waiting_time, 10)
        self.assertEqual(processes[3].waiting_time, 23)

    def test_round_robin(self):
        processes = scheduler.round_robin(manager.create_processes("./tests/process5.txt"))
        self.assertEqual(processes[0].turnaround_time, 19)
        self.assertEqual(processes[1].turnaround_time, 32)
        self.assertEqual(processes[2].turnaround_time, 35)
        self.assertEqual(processes[3].turnaround_time, 41)
        self.assertEqual(processes[0].waiting_time, 10)
        self.assertEqual(processes[1].waiting_time, 21)
        self.assertEqual(processes[2].waiting_time, 20)
        self.assertEqual(processes[3].waiting_time, 23)


if __name__ == '__main__':
    unittest.main()