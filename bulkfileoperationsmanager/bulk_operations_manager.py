# bulk_operations_manager.py
from filechunkcrud import FileHandler
from queue import Queue
import threading

class BulkOperationsManager:
    def __init__(self):
        self.tasks_queue = Queue()

    def add_task(self, task):
        """Добавление задания в очередь."""
        self.tasks_queue.put(task)

    def run(self):
        """Запуск обработки заданий."""
        while not self.tasks_queue.empty():
            task = self.tasks_queue.get()
            self._execute_task(task)

    def _execute_task(self, task):
        operation, file_path, *args = task
        file_handler = FileHandler(file_path)

        if operation == "read":
            chunk_size, handler = args
            for chunk in file_handler.read_chunks(chunk_size):
                handler(chunk)
        elif operation == "create":
            file_handler.create_file(*args)
        elif operation == "update":
            file_handler.update_file(*args)
        elif operation == "delete":
            file_handler.delete_file()
        else:
            raise ValueError("Неизвестная операция")

        self.tasks_queue.task_done()
