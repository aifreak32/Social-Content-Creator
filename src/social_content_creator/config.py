"""
Configuration management for Social Content Creator
"""
import os
from typing import Optional
from pydantic import BaseModel, Field
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class APIConfig(BaseModel):
    """API credentials configuration"""
    openai_api_key: Optional[str] = Field(default_factory=lambda: os.getenv("OPENAI_API_KEY"))
    anthropic_api_key: Optional[str] = Field(default_factory=lambda: os.getenv("ANTHROPIC_API_KEY"))
    
    # Social Media APIs
    tiktok_session_id: Optional[str] = Field(default_factory=lambda: os.getenv("TIKTOK_SESSION_ID"))
    instagram_username: Optional[str] = Field(default_factory=lambda: os.getenv("INSTAGRAM_USERNAME"))
    instagram_password: Optional[str] = Field(default_factory=lambda: os.getenv("INSTAGRAM_PASSWORD"))
    twitter_api_key: Optional[str] = Field(default_factory=lambda: os.getenv("TWITTER_API_KEY"))
    twitter_api_secret: Optional[str] = Field(default_factory=lambda: os.getenv("TWITTER_API_SECRET"))
    twitter_access_token: Optional[str] = Field(default_factory=lambda: os.getenv("TWITTER_ACCESS_TOKEN"))
    twitter_access_secret: Optional[str] = Field(default_factory=lambda: os.getenv("TWITTER_ACCESS_SECRET"))
    youtube_api_key: Optional[str] = Field(default_factory=lambda: os.getenv("YOUTUBE_API_KEY"))


class AppConfig(BaseModel):
    """Application configuration"""
    log_level: str = Field(default_factory=lambda: os.getenv("LOG_LEVEL", "INFO"))
    output_dir: str = Field(default_factory=lambda: os.getenv("OUTPUT_DIR", "./output"))
    language: str = Field(default_factory=lambda: os.getenv("LANGUAGE", "ITA"))


class Config:
    """Main configuration class"""
    
    def __init__(self):
        self.api = APIConfig()
        self.app = AppConfig()
        self._ensure_output_dir()
    
    def _ensure_output_dir(self):
        """Ensure output directory exists"""
        os.makedirs(self.app.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.app.output_dir, "videos"), exist_ok=True)
        os.makedirs(os.path.join(self.app.output_dir, "images"), exist_ok=True)
        os.makedirs(os.path.join(self.app.output_dir, "reports"), exist_ok=True)


# Global configuration instance
config = Config()
