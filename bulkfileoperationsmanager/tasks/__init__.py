import unittest
import os
from bulkfileoperationsmanager.bulk_operations_manager import BulkOperationsManager

class TestBulkOperationsManager(unittest.TestCase):
    def setUp(self):
        # Setup for each test
        self.test_file_path = "test_file.txt"
        self.manager = BulkOperationsManager()

    def tearDown(self):
        # Cleanup after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_add_and_execute_create_task(self):
        # Test adding and executing a create task
        self.manager.add_task(("create", self.test_file_path, "Test content"))
        self.manager.run()

        with open(self.test_file_path, "r") as file:
            content = file.read()
        self.assertEqual(content, "Test content")

    def test_add_and_execute_read_task(self):
        # Setup a file to read
        with open(self.test_file_path, "w") as file:
            file.write("Hello, world!")

        # Test adding and executing a read task
        read_content = []
        def mock_read_handler(chunk):
            read_content.append(chunk)
        self.manager.add_task(("read", self.test_file_path, 1024, mock_read_handler))
        self.manager.run()

        # Check if content was read correctly
        self.assertEqual("".join(read_content), "Hello, world!")

    def test_add_and_execute_update_task(self):
        # Setup a file to update
        with open(self.test_file_path, "w") as file:
            file.write("Initial content")

        # Test adding and executing an update task
        self.manager.add_task(("update", self.test_file_path, "\nAdditional content"))
        self.manager.run()

        with open(self.test_file_path, "r") as file:
            content = file.read()
        self.assertIn("Additional content", content)

    def test_add_and_execute_delete_task(self):
        # Setup a file to delete
        with open(self.test_file_path, "w") as file:
            file.write("Temporary file.")

        # Test adding and executing a delete task
        self.manager.add_task(("delete", self.test_file_path))
        self.manager.run()

        self.assertFalse(os.path.exists(self.test_file_path))

if __name__ == '__main__':
    unittest.main()
