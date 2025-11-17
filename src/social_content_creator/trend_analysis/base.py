"""
Base Trend Analyzer - Abstract class for platform-specific analyzers
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any
from ..models import Trend, Platform


class BaseTrendAnalyzer(ABC):
    """Base class for trend analyzers"""
    
    def __init__(self, platform: Platform):
        self.platform = platform
    
    @abstractmethod
    async def fetch_trending_topics(self, limit: int = 10) -> List[Trend]:
        """Fetch trending topics from the platform"""
        pass
    
    @abstractmethod
    async def fetch_trending_hashtags(self, limit: int = 10) -> List[Trend]:
        """Fetch trending hashtags"""
        pass
    
    @abstractmethod
    async def analyze_competitor(self, competitor_id: str) -> Dict[str, Any]:
        """Analyze a competitor's performance"""
        pass
    
    @abstractmethod
    async def get_engagement_metrics(self, content_id: str) -> Dict[str, int]:
        """Get engagement metrics for specific content"""
        pass
