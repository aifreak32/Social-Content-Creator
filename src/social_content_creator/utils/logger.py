"""
Logging utilities
"""
import logging
import sys
from ..config import config


def setup_logger(name: str = "social_content_creator") -> logging.Logger:
    """Setup logger with proper formatting"""
    
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, config.app.log_level.upper(), logging.INFO))
    
    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.DEBUG)
    
    # Formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    return logger


# Global logger instance
logger = setup_logger()
