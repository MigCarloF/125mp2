import unittest
import manager

class TestProcesses(unittest.TestCase):

    def test_create_processes(self):
        processes = manager.create_processes("./tests/test.txt")
        self.assertEqual(len(processes), 6)
        
        with self.assertRaises(manager.IncorrectFirstRowException):
            manager.create_processes("./tests/test2.txt")
        
        with self.assertRaises(manager.ValueQuantityException):
            manager.create_processes("./tests/test3.txt")

if __name__ == '__main__':
    unittest.main()