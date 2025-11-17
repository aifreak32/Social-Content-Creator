"""
Performance Metrics Tracker
"""
from typing import Dict, List, Any
from datetime import datetime, timedelta
from ..models import PerformanceMetrics, Platform, ContentAsset


class MetricsTracker:
    """Track and analyze content performance metrics"""
    
    def __init__(self):
        self.metrics_history = {}
    
    async def track_content_performance(
        self,
        content: ContentAsset,
        platform: Platform
    ) -> PerformanceMetrics:
        """Track performance metrics for specific content"""
        # TODO: Integrate with platform APIs to fetch real metrics
        
        # Mock metrics tracking
        metrics = PerformanceMetrics(
            content_id=content.id,
            platform=platform,
            views=50000,
            likes=4000,
            comments=200,
            shares=500,
            engagement_rate=0.096,
            reach=75000,
            impressions=100000,
            timestamp=datetime.now()
        )
        
        # Store in history
        self.metrics_history[content.id] = metrics
        
        return metrics
    
    async def get_performance_trend(
        self,
        content_id: str,
        timeframe_days: int = 7
    ) -> List[PerformanceMetrics]:
        """Get performance trend over time"""
        # TODO: Fetch historical metrics from database
        
        trend = []
        start_date = datetime.now() - timedelta(days=timeframe_days)
        
        # Mock trend data
        for i in range(timeframe_days):
            date = start_date + timedelta(days=i)
            metrics = PerformanceMetrics(
                content_id=content_id,
                platform=Platform.TIKTOK,
                views=10000 * (i + 1),
                likes=800 * (i + 1),
                comments=40 * (i + 1),
                shares=100 * (i + 1),
                engagement_rate=0.08 + (i * 0.01),
                reach=15000 * (i + 1),
                impressions=20000 * (i + 1),
                timestamp=date
            )
            trend.append(metrics)
        
        return trend
    
    def calculate_engagement_rate(self, metrics: PerformanceMetrics) -> float:
        """Calculate engagement rate"""
        if metrics.views == 0:
            return 0.0
        
        total_engagement = metrics.likes + metrics.comments + metrics.shares
        return total_engagement / metrics.views
    
    def calculate_viral_score(self, metrics: PerformanceMetrics) -> float:
        """Calculate virality score (0-100)"""
        # Weighted scoring based on different metrics
        view_score = min(metrics.views / 100000 * 30, 30)
        engagement_score = metrics.engagement_rate * 100 * 0.4
        share_score = min(metrics.shares / 1000 * 30, 30)
        
        viral_score = view_score + engagement_score + share_score
        return min(viral_score, 100)
    
    async def compare_content_performance(
        self,
        content_ids: List[str]
    ) -> Dict[str, Any]:
        """Compare performance across multiple pieces of content"""
        comparison = {
            'contents': [],
            'best_performing': None,
            'average_metrics': {}
        }
        
        total_views = 0
        total_engagement = 0
        best_score = 0
        
        for content_id in content_ids:
            if content_id in self.metrics_history:
                metrics = self.metrics_history[content_id]
                viral_score = self.calculate_viral_score(metrics)
                
                comparison['contents'].append({
                    'content_id': content_id,
                    'metrics': metrics,
                    'viral_score': viral_score
                })
                
                total_views += metrics.views
                total_engagement += self.calculate_engagement_rate(metrics)
                
                if viral_score > best_score:
                    best_score = viral_score
                    comparison['best_performing'] = content_id
        
        if content_ids:
            comparison['average_metrics'] = {
                'avg_views': total_views / len(content_ids),
                'avg_engagement_rate': total_engagement / len(content_ids)
            }
        
        return comparison
    
    async def identify_best_performing_content(
        self,
        platform: Platform,
        metric: str = 'engagement_rate',
        limit: int = 10
    ) -> List[Dict[str, Any]]:
        """Identify top performing content by metric"""
        # TODO: Query database for best performing content
        
        performing_content = []
        
        for content_id, metrics in self.metrics_history.items():
            if metrics.platform == platform:
                performing_content.append({
                    'content_id': content_id,
                    'metrics': metrics,
                    metric: getattr(metrics, metric, 0)
                })
        
        # Sort by specified metric
        performing_content.sort(key=lambda x: x[metric], reverse=True)
        
        return performing_content[:limit]
