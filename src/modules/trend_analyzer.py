"""
Trend Analysis Module
Real-time trend detection and analysis from multiple social media platforms
"""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any
import requests
from collections import Counter
import re

logger = logging.getLogger(__name__)


class TrendAnalyzer:
    """Analyzes social media trends in real-time"""
    
    def __init__(self, config):
        self.config = config
        self.trends_cache = []
        self.last_update = None
        
    def analyze_trends(self) -> List[Dict[str, Any]]:
        """
        Analyze current trends across social media platforms
        Returns a list of trending topics with metadata
        """
        logger.info("Starting trend analysis...")
        trends = []
        
        # Combine trends from different sources
        twitter_trends = self._get_twitter_trends()
        google_trends = self._get_google_trends()
        
        # Merge and score trends
        all_trends = twitter_trends + google_trends
        trend_scores = self._score_trends(all_trends)
        
        # Store for later analysis
        self.trends_cache = trend_scores
        self.last_update = datetime.now()
        
        logger.info(f"Found {len(trend_scores)} trending topics")
        return trend_scores
    
    def _get_twitter_trends(self) -> List[Dict[str, Any]]:
        """Fetch trending topics from Twitter/X"""
        trends = []
        
        if not self.config.TWITTER_BEARER_TOKEN:
            logger.warning("Twitter API token not configured, skipping Twitter trends")
            return trends
        
        try:
            # This is a simplified version - would need proper Twitter API v2 integration
            # For demo purposes, returning simulated trends
            simulated_trends = [
                {"name": "#AI", "volume": 125000, "sentiment": "positive"},
                {"name": "#Technology", "volume": 98000, "sentiment": "neutral"},
                {"name": "#ContentCreation", "volume": 65000, "sentiment": "positive"},
                {"name": "#DigitalMarketing", "volume": 54000, "sentiment": "positive"},
                {"name": "#SocialMedia", "volume": 87000, "sentiment": "neutral"},
            ]
            
            for trend in simulated_trends:
                trends.append({
                    "topic": trend["name"],
                    "volume": trend["volume"],
                    "source": "twitter",
                    "sentiment": trend["sentiment"],
                    "timestamp": datetime.now()
                })
                
            logger.info(f"Retrieved {len(trends)} trends from Twitter")
            
        except Exception as e:
            logger.error(f"Error fetching Twitter trends: {e}")
        
        return trends
    
    def _get_google_trends(self) -> List[Dict[str, Any]]:
        """Fetch trending topics from Google Trends"""
        trends = []
        
        try:
            # Simulated Google Trends data for demo
            simulated_trends = [
                {"query": "AI tools", "value": 100000, "growth": "+150%"},
                {"query": "viral content", "value": 75000, "growth": "+80%"},
                {"query": "social media marketing", "value": 90000, "growth": "+45%"},
                {"query": "content automation", "value": 60000, "growth": "+200%"},
            ]
            
            for trend in simulated_trends:
                trends.append({
                    "topic": trend["query"],
                    "volume": trend["value"],
                    "source": "google",
                    "growth_rate": trend["growth"],
                    "timestamp": datetime.now()
                })
                
            logger.info(f"Retrieved {len(trends)} trends from Google")
            
        except Exception as e:
            logger.error(f"Error fetching Google trends: {e}")
        
        return trends
    
    def _score_trends(self, trends: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Score and rank trends based on multiple factors
        """
        scored_trends = []
        
        for trend in trends:
            score = 0.0
            
            # Volume score (normalized)
            volume = trend.get("volume", 0)
            volume_score = min(volume / 100000, 1.0) * 40
            
            # Growth rate score
            growth_rate = trend.get("growth_rate", "0%")
            growth_value = float(re.sub(r'[^\d.]', '', growth_rate)) if growth_rate else 0
            growth_score = min(growth_value / 100, 1.0) * 30
            
            # Sentiment score
            sentiment = trend.get("sentiment", "neutral")
            sentiment_score = 20 if sentiment == "positive" else (10 if sentiment == "neutral" else 5)
            
            # Recency score
            recency_score = 10
            
            # Calculate total score
            score = volume_score + growth_score + sentiment_score + recency_score
            
            scored_trends.append({
                **trend,
                "score": round(score, 2),
                "viability": "high" if score > 70 else ("medium" if score > 50 else "low")
            })
        
        # Sort by score descending
        scored_trends.sort(key=lambda x: x["score"], reverse=True)
        
        return scored_trends
    
    def get_top_trends(self, n: int = 10) -> List[Dict[str, Any]]:
        """Get top N trending topics"""
        if not self.trends_cache or self._is_cache_stale():
            self.analyze_trends()
        
        return self.trends_cache[:n]
    
    def _is_cache_stale(self) -> bool:
        """Check if trend cache needs refresh"""
        if not self.last_update:
            return True
        
        stale_threshold = timedelta(minutes=self.config.TREND_ANALYSIS_INTERVAL_MINUTES)
        return datetime.now() - self.last_update > stale_threshold
    
    def get_trend_keywords(self, trend: Dict[str, Any]) -> List[str]:
        """Extract keywords from a trend for content generation"""
        topic = trend.get("topic", "")
        
        # Remove hashtags and special characters
        cleaned = re.sub(r'[#@]', '', topic)
        
        # Split into words
        keywords = cleaned.lower().split()
        
        # Add related keywords based on context
        related_keywords = {
            "ai": ["artificial intelligence", "machine learning", "automation"],
            "technology": ["tech", "innovation", "digital"],
            "content": ["creation", "strategy", "marketing"],
            "social": ["media", "engagement", "viral"],
        }
        
        expanded_keywords = keywords.copy()
        for keyword in keywords:
            if keyword in related_keywords:
                expanded_keywords.extend(related_keywords[keyword])
        
        return list(set(expanded_keywords))
