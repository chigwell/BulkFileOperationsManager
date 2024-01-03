[![PyPI version](https://badge.fury.io/py/BulkFileOperationsManager.svg)](https://badge.fury.io/py/BulkFileOperationsManager)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://static.pepy.tech/badge/bulkfileoperationsmanager)](https://pepy.tech/project/bulkfileoperationsmanager)

# BulkFileOperationsManager

`BulkFileOperationsManager` is a Python tool designed to manage and execute bulk Create, Read, Update, and Delete (CRUD) operations on files, especially useful for handling large files that need to be processed in chunks to fit into memory constraints.

## Installation

To install `BulkFileOperationsManager`, you can use pip:

```bash
pip install BulkFileOperationsManager
```

## Usage

### As a Python Module

`BulkFileOperationsManager` can be used as a Python module in your scripts for orchestrating bulk file operations.

#### Adding and Executing Tasks

```python
from bulkfileoperationsmanager.bulk_operations_manager import BulkOperationsManager
from filechunkcrud import FileHandler

# Initialize the manager
manager = BulkOperationsManager()

# Example of adding and executing a create task
file_path = '/path/to/your/largefile.txt'
manager.add_task(("create", file_path, "Initial content"))
manager.run()

# Example of adding and executing a read task with handler
def read_handler(chunk):
    print(chunk)  # or process the chunk

manager.add_task(("read", file_path, 1024, read_handler))
manager.run()

# Example of adding and executing an update task with content generator
def additional_data_generator():
    yield "\nMore data...\n"

manager.add_task(("update", file_path, additional_data_generator()))
manager.run()

# Example of adding and executing a delete task
manager.add_task(("delete", file_path))
manager.run()
```

## Features

- **Manage Bulk Operations**: Efficiently manage and execute multiple file operations in a queue-based system.
- **Integration with FileChunkCRUD**: Seamlessly integrates with FileChunkCRUD for handling large files in chunks.
- **Supports CRUD operations**: Supports creating, reading, updating, and deleting files, especially suitable for large files.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/BulkFileOperationsManager/issues).

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/).
