import logging

# Get logger for this module
logger = logging.getLogger("models")

# Add a NullHandler to avoid "No handlers could be found" warnings
logger.addHandler(logging.NullHandler())



