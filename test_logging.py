#!/usr/bin/env python3
"""
Test script to verify logging functionality
"""

from INFORMATION_logger import get_logger

def test_logging():
    """Test basic logging functionality"""
    logger = get_logger('test')
    
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    
    print("Logging test completed. Check the logs directory for output files.")

if __name__ == "__main__":
    test_logging() 