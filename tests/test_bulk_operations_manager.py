import unittest
import os
from bulkfileoperationsmanager.bulk_operations_manager import BulkOperationsManager
from filechunkcrud import FileHandler

class TestBulkOperationsManager(unittest.TestCase):
    def setUp(self):
        self.manager = BulkOperationsManager()
        self.test_file_path = "large_test_file.txt"
        with open(self.test_file_path, "w") as file:
            file.write("Hello, world!" * 1000000)  # Adjust size as needed

    def tearDown(self):
        # Cleanup the large test file only if it exists
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_read_chunks(self):
        # Initialize the file handler
        file_handler = FileHandler(self.test_file_path)

        # Use a smaller chunk size for demonstration
        chunk_size = 1024
        total_read = 0

        # Read and process each chunk
        for chunk in file_handler.read_chunks(chunk_size):
            self.assertTrue(len(chunk) <= chunk_size)
            total_read += len(chunk)

        # Check total read size
        self.assertEqual(total_read, os.path.getsize(self.test_file_path))

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

        # Correctly pass the read handler to the task
        self.manager.add_task(("read", self.test_file_path, 1024, mock_read_handler))
        self.manager.run()

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
