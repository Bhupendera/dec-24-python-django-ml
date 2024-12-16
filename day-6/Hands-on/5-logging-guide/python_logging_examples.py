import logging

def reset_logging():
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

# Basic Logging Configuration
def setup_basic_logger():
    reset_logging()
    logging.basicConfig(level=logging.INFO)
    logging.info("Application started")
    logging.debug("This debug message will not appear")
    logging.warning("This is a warning")

# Logging to the Screen
def log_to_console():
    reset_logging()
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)s:%(message)s')
    logging.info("Logging to console only")

# Logging to a File
def log_to_file():
    reset_logging()
    # Create a file handler
    file_handler = logging.FileHandler('app.log', mode='a+')
    file_handler.setLevel(logging.INFO)
    
    # Create a formatter and set it for the handler
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    
    # Get the root logger and add the handler to it
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    
    logger.info("This will be logged to a file")

# Logging to Both Screen and File
def log_to_screen_and_file():
    reset_logging()
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

# Main Execution to Run All Examples
if __name__ == "__main__":
    print("Running: setup_basic_logger")
    setup_basic_logger()

    print("\nRunning: log_to_console")
    log_to_console()

    print("\nRunning: log_to_file")
    log_to_file()

    print("\nRunning: log_to_screen_and_file")

    log_to_screen_and_file()