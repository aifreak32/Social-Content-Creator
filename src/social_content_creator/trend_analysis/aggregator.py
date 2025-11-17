"""
Cross-Platform Trend Aggregator and Pattern Identifier
"""
import asyncio
from typing import List, Dict, Any
from collections import defaultdict
from datetime import datetime

from .tiktok import TikTokAnalyzer
from .instagram import InstagramAnalyzer
from .twitter import TwitterAnalyzer
from .youtube import YouTubeAnalyzer
from ..models import Trend, Platform


class CrossPlatformAnalyzer:
    """Aggregate and analyze trends across all platforms"""
    
    def __init__(self, config):
        self.tiktok = TikTokAnalyzer(config.api.tiktok_session_id)
        self.instagram = InstagramAnalyzer(
            config.api.instagram_username, 
            config.api.instagram_password
        )
        self.twitter = TwitterAnalyzer(
            config.api.twitter_api_key,
            config.api.twitter_api_secret,
            config.api.twitter_access_token,
            config.api.twitter_access_secret
        )
        self.youtube = YouTubeAnalyzer(config.api.youtube_api_key)
    
    async def fetch_all_trends(self, limit_per_platform: int = 10) -> Dict[Platform, List[Trend]]:
        """Fetch trends from all platforms"""
        results = {}
        
        # Fetch from all platforms in parallel
        tasks = [
            self._fetch_platform_trends(self.tiktok, Platform.TIKTOK, limit_per_platform),
            self._fetch_platform_trends(self.instagram, Platform.INSTAGRAM, limit_per_platform),
            self._fetch_platform_trends(self.twitter, Platform.TWITTER, limit_per_platform),
            self._fetch_platform_trends(self.youtube, Platform.YOUTUBE, limit_per_platform),
        ]
        
        platform_trends = await asyncio.gather(*tasks, return_exceptions=True)
        
        for platform, trends in zip([Platform.TIKTOK, Platform.INSTAGRAM, Platform.TWITTER, Platform.YOUTUBE], platform_trends):
            if not isinstance(trends, Exception):
                results[platform] = trends
            else:
                results[platform] = []
                print(f"Error fetching trends from {platform}: {trends}")
        
        return results
    
    async def _fetch_platform_trends(self, analyzer, platform: Platform, limit: int) -> List[Trend]:
        """Fetch trends from a specific platform"""
        topics = await analyzer.fetch_trending_topics(limit)
        hashtags = await analyzer.fetch_trending_hashtags(limit)
        return topics + hashtags
    
    def identify_cross_platform_patterns(self, all_trends: Dict[Platform, List[Trend]]) -> List[Dict[str, Any]]:
        """Identify viral patterns appearing across multiple platforms"""
        patterns = []
        
        # Group trends by similar keywords
        keyword_groups = defaultdict(list)
        
        for platform, trends in all_trends.items():
            for trend in trends:
                # Extract keywords from trend name
                keywords = self._extract_keywords(trend.name)
                for keyword in keywords:
                    keyword_groups[keyword].append({
                        'platform': platform,
                        'trend': trend
                    })
        
        # Identify cross-platform patterns (appear on 2+ platforms)
        for keyword, trend_list in keyword_groups.items():
            platforms = set(t['platform'] for t in trend_list)
            if len(platforms) >= 2:
                avg_engagement = sum(t['trend'].engagement_score for t in trend_list) / len(trend_list)
                avg_growth = sum(t['trend'].growth_rate for t in trend_list) / len(trend_list)
                
                patterns.append({
                    'keyword': keyword,
                    'platforms': list(platforms),
                    'platform_count': len(platforms),
                    'avg_engagement_score': avg_engagement,
                    'avg_growth_rate': avg_growth,
                    'virality_score': len(platforms) * avg_engagement * (1 + avg_growth),
                    'trends': trend_list
                })
        
        # Sort by virality score
        patterns.sort(key=lambda x: x['virality_score'], reverse=True)
        
        return patterns
    
    def _extract_keywords(self, text: str) -> List[str]:
        """Extract keywords from text"""
        # Simple keyword extraction (can be enhanced with NLP)
        words = text.lower().replace('#', '').split()
        # Filter out common words
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for'}
        keywords = [w for w in words if w not in stop_words and len(w) > 3]
        return keywords
    
    def predict_emerging_trends(self, all_trends: Dict[Platform, List[Trend]]) -> List[Dict[str, Any]]:
        """Predict which trends are likely to go viral"""
        predictions = []
        
        for platform, trends in all_trends.items():
            for trend in trends:
                # Calculate prediction score based on engagement and growth
                prediction_score = (
                    trend.engagement_score * 0.4 +
                    trend.growth_rate * 100 * 0.6
                )
                
                if prediction_score > 50:  # Threshold for emerging trends
                    predictions.append({
                        'trend': trend,
                        'platform': platform,
                        'prediction_score': prediction_score,
                        'confidence': min(prediction_score / 100, 1.0),
                        'estimated_peak_days': int(10 / (trend.growth_rate + 0.01))
                    })
        
        # Sort by prediction score
        predictions.sort(key=lambda x: x['prediction_score'], reverse=True)
        
        return predictions
