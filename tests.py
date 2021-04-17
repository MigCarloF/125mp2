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

    def test_fcfs_turn_around_time(self):
        processes = scheduler.fcfs(manager.create_processes("./tests/test.txt"))
        for process in processes:
            print("Process %d arrived at %d" % (process.process_number, process.arrival_time))
        self.assertEqual(processes[0].turnaround_time, 4)
        self.assertEqual(processes[1].turnaround_time, 7)
        self.assertEqual(processes[2].turnaround_time, 10)
        self.assertEqual(processes[3].turnaround_time, 16)
        self.assertEqual(processes[4].turnaround_time, 22)
        self.assertEqual(processes[5].turnaround_time, 29)
            

            
        

if __name__ == '__main__':
    unittest.main()