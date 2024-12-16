# Comprehensive Guide to Python Logging

## Introduction to Logging
Logging is a crucial part of software development that allows developers to monitor, debug, and maintain applications effectively. Unlike `print` statements, logging provides a flexible and standardized way to record diagnostic messages and runtime events.

### Why Use Logging?
- Provides better control over the granularity of output (via logging levels).
- Logs can be redirected to files, making it easier to trace application issues.
- Works seamlessly in production environments.

---

## Logging Levels
Python's `logging` module defines five standard logging levels, each assigned a numeric value.

| Level       | Numeric Value | Description                                  | Example Use Case                     |
|-------------|---------------|----------------------------------------------|--------------------------------------|
| `DEBUG`     | 10            | Detailed information for diagnosing problems.| Debugging during development.        |
| `INFO`      | 20            | General information about application events.| Startup or shutdown messages.        |
| `WARNING`   | 30            | Indicates potential problems.               | Deprecated API usage.                |
| `ERROR`     | 40            | Error messages for significant problems.    | Failed database connection.          |
| `CRITICAL`  | 50            | Severe errors causing application shutdown. | Out-of-memory errors.                |

### Priority of Logging Levels
Messages are processed in the order of their severity. For example, if the log level is set to `WARNING`, only `WARNING`, `ERROR`, and `CRITICAL` messages will be logged.

---

## Basic Logging Configuration
The `logging` module's `basicConfig` method allows for quick setup.

### Example: Basic Configuration
```python
import logging

def setup_basic_logger():
    logging.basicConfig(level=logging.INFO)
    logging.info("Application started")
    logging.debug("This debug message will not appear")
    logging.warning("This is a warning")

setup_basic_logger()
```
**Output:**
```
INFO:root:Application started
WARNING:root:This is a warning
```

---

## Redirecting Logs
### Logging to the Screen
```python
import logging

def log_to_console():
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')
    logging.info("Logging to console only")

log_to_console()
```
**Output:**
```
INFO:Logging to console only
```

### Logging to a File
```python
import logging

def log_to_file():
    logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("This will be logged to a file")

log_to_file()
```
**File Content (app.log):**
```
2024-12-16 12:00:00,000 - INFO - This will be logged to a file
```

### Logging to Both Screen and File
```python
import logging

def log_to_screen_and_file():
    # Create handlers
    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('dual_output.log')

    # Create formatters
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Configure logger
    logger = logging.getLogger('MyLogger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("This will appear on both screen and file")

log_to_screen_and_file()
```
**File Content (dual_output.log):**
```
2024-12-16 12:00:00,000 - MyLogger - INFO - This will appear on both screen and file
```

---

## Logging Format
You can customize log messages using the `format` parameter.

### Example: Custom Format
```python
import logging

def custom_format_logger():
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                        level=logging.INFO)
    logging.info("Custom log message format")

custom_format_logger()
```
**Output:**
```
2024-12-16 12:00:00,000 - INFO - Custom log message format
```

---

