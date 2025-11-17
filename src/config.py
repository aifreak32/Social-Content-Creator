"""
Configuration Management Module
Handles loading and managing configuration from environment variables
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Config:
    """Central configuration class for the Social Content Creator"""
    
    # API Keys
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
    
    # Twitter/X Configuration
    TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", "")
    TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", "")
    TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "")
    TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET", "")
    TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "")
    
    # Instagram Configuration
    INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME", "")
    INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD", "")
    
    # Database
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///social_content_creator.db")
    
    # Agent Configuration
    TREND_ANALYSIS_INTERVAL_MINUTES = int(os.getenv("TREND_ANALYSIS_INTERVAL_MINUTES", "30"))
    CONTENT_GENERATION_INTERVAL_HOURS = int(os.getenv("CONTENT_GENERATION_INTERVAL_HOURS", "4"))
    NICHE_ANALYSIS_INTERVAL_HOURS = int(os.getenv("NICHE_ANALYSIS_INTERVAL_HOURS", "24"))
    STRATEGY_OPTIMIZATION_INTERVAL_HOURS = int(os.getenv("STRATEGY_OPTIMIZATION_INTERVAL_HOURS", "12"))
    
    # Content Settings
    MIN_ENGAGEMENT_SCORE = float(os.getenv("MIN_ENGAGEMENT_SCORE", "7.0"))
    MAX_POSTS_PER_DAY = int(os.getenv("MAX_POSTS_PER_DAY", "10"))
    VIDEO_GENERATION_ENABLED = os.getenv("VIDEO_GENERATION_ENABLED", "true").lower() == "true"
    IMAGE_GENERATION_ENABLED = os.getenv("IMAGE_GENERATION_ENABLED", "true").lower() == "true"
    
    # Monetization
    MIN_FOLLOWERS_FOR_MONETIZATION = int(os.getenv("MIN_FOLLOWERS_FOR_MONETIZATION", "10000"))
    TARGET_ENGAGEMENT_RATE = float(os.getenv("TARGET_ENGAGEMENT_RATE", "0.05"))
    
    # Directories
    BASE_DIR = Path(__file__).parent.parent
    GENERATED_CONTENT_DIR = BASE_DIR / "generated_content"
    LOGS_DIR = BASE_DIR / "logs"
    
    @classmethod
    def ensure_directories(cls):
        """Create necessary directories if they don't exist"""
        cls.GENERATED_CONTENT_DIR.mkdir(exist_ok=True)
        cls.LOGS_DIR.mkdir(exist_ok=True)
        (cls.GENERATED_CONTENT_DIR / "images").mkdir(exist_ok=True)
        (cls.GENERATED_CONTENT_DIR / "videos").mkdir(exist_ok=True)
    
    @classmethod
    def validate(cls):
        """Validate that required configuration is present"""
        errors = []
        
        if not cls.OPENAI_API_KEY and not cls.ANTHROPIC_API_KEY:
            errors.append("At least one AI API key (OpenAI or Anthropic) must be set")
        
        return errors


# Ensure directories exist on import
Config.ensure_directories()
