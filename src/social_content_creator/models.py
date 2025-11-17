"""
Data models for Social Content Creator
"""
from datetime import datetime
from typing import List, Dict, Optional, Any
from enum import Enum
from pydantic import BaseModel, Field


class Platform(str, Enum):
    """Social media platforms"""
    TIKTOK = "tiktok"
    INSTAGRAM = "instagram"
    TWITTER = "twitter"
    YOUTUBE = "youtube"


class TrendType(str, Enum):
    """Types of trends"""
    SOUND = "sound"
    HASHTAG = "hashtag"
    FORMAT = "format"
    TOPIC = "topic"
    CONTENT = "content"


class ContentType(str, Enum):
    """Types of content"""
    VIDEO = "video"
    IMAGE = "image"
    TEXT = "text"
    CAROUSEL = "carousel"


class Trend(BaseModel):
    """Trend data model"""
    id: str
    platform: Platform
    type: TrendType
    name: str
    description: Optional[str] = None
    engagement_score: float = Field(ge=0, le=100)
    growth_rate: float
    timestamp: datetime = Field(default_factory=datetime.now)
    metadata: Dict[str, Any] = Field(default_factory=dict)
    tags: List[str] = Field(default_factory=list)


class ViralContent(BaseModel):
    """Viral content data model"""
    id: str
    platform: Platform
    content_type: ContentType
    url: str
    engagement_metrics: Dict[str, int]
    creator: str
    timestamp: datetime
    description: Optional[str] = None
    tags: List[str] = Field(default_factory=list)


class NicheAnalysis(BaseModel):
    """Niche analysis data model"""
    niche_name: str
    profitability_score: float = Field(ge=0, le=100)
    competition_level: float = Field(ge=0, le=100)
    saturation_level: float = Field(ge=0, le=100)
    potential_score: float = Field(ge=0, le=100)
    target_audience: Dict[str, Any]
    monetization_opportunities: List[str]
    recommended_platforms: List[Platform]
    growth_strategy: Dict[str, Any]


class ContentAsset(BaseModel):
    """Generated content asset"""
    id: str
    type: ContentType
    platform: Platform
    file_path: Optional[str] = None
    caption: str
    hashtags: List[str]
    call_to_action: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=datetime.now)


class PerformanceMetrics(BaseModel):
    """Performance metrics for content"""
    content_id: str
    platform: Platform
    views: int = 0
    likes: int = 0
    comments: int = 0
    shares: int = 0
    engagement_rate: float = 0.0
    reach: int = 0
    impressions: int = 0
    timestamp: datetime = Field(default_factory=datetime.now)


class CreationCycle(BaseModel):
    """Complete content creation cycle output"""
    cycle_id: str
    trend_report: List[Trend]
    niche_recommendations: List[NicheAnalysis]
    video_assets: List[ContentAsset]
    image_assets: List[ContentAsset]
    copywriting: Dict[Platform, str]
    publishing_plan: Dict[str, Any]
    growth_strategy: Dict[str, Any]
    created_at: datetime = Field(default_factory=datetime.now)
