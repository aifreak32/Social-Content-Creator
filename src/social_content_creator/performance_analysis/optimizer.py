"""
Real-time Optimization Engine
"""
from typing import Dict, Any, List
from datetime import datetime

from ..models import ContentAsset, PerformanceMetrics, Platform
from .metrics import MetricsTracker


class OptimizationEngine:
    """Real-time content optimization based on performance data"""
    
    def __init__(self):
        self.metrics_tracker = MetricsTracker()
        self.optimization_rules = self._initialize_rules()
    
    def _initialize_rules(self) -> Dict[str, Any]:
        """Initialize optimization rules"""
        return {
            'low_engagement_threshold': 0.03,
            'high_engagement_threshold': 0.08,
            'viral_threshold': 0.10,
            'min_views_for_analysis': 1000
        }
    
    async def analyze_and_optimize(
        self,
        content: ContentAsset,
        metrics: PerformanceMetrics
    ) -> Dict[str, Any]:
        """Analyze performance and suggest optimizations"""
        
        analysis = {
            'content_id': content.id,
            'platform': content.platform,
            'performance_level': self._categorize_performance(metrics),
            'issues': [],
            'recommendations': [],
            'action_items': []
        }
        
        # Check engagement rate
        if metrics.engagement_rate < self.optimization_rules['low_engagement_threshold']:
            analysis['issues'].append('Low engagement rate')
            analysis['recommendations'].extend(
                self._get_engagement_recommendations(content, metrics)
            )
        
        # Check views
        if metrics.views < self.optimization_rules['min_views_for_analysis']:
            analysis['issues'].append('Low reach')
            analysis['recommendations'].extend(
                self._get_reach_recommendations(content, metrics)
            )
        
        # Check shares (virality indicator)
        if metrics.shares < (metrics.views * 0.01):
            analysis['issues'].append('Low shareability')
            analysis['recommendations'].extend(
                self._get_virality_recommendations(content, metrics)
            )
        
        # Generate action items
        analysis['action_items'] = self._generate_action_items(analysis)
        
        return analysis
    
    def _categorize_performance(self, metrics: PerformanceMetrics) -> str:
        """Categorize content performance"""
        if metrics.engagement_rate >= self.optimization_rules['viral_threshold']:
            return 'viral'
        elif metrics.engagement_rate >= self.optimization_rules['high_engagement_threshold']:
            return 'high'
        elif metrics.engagement_rate >= self.optimization_rules['low_engagement_threshold']:
            return 'medium'
        else:
            return 'low'
    
    def _get_engagement_recommendations(
        self,
        content: ContentAsset,
        metrics: PerformanceMetrics
    ) -> List[str]:
        """Get recommendations for improving engagement"""
        recommendations = []
        
        recommendations.append("Optimize hook - first 3 seconds are critical")
        recommendations.append("Add stronger call-to-action")
        recommendations.append("Use trending sounds/music")
        
        if metrics.comments < 50:
            recommendations.append("Ask engaging questions to drive comments")
        
        if metrics.shares < 100:
            recommendations.append("Create more shareable content - educational or entertaining")
        
        return recommendations
    
    def _get_reach_recommendations(
        self,
        content: ContentAsset,
        metrics: PerformanceMetrics
    ) -> List[str]:
        """Get recommendations for improving reach"""
        recommendations = []
        
        recommendations.append("Use trending hashtags for better discoverability")
        recommendations.append("Post during peak hours for your audience")
        recommendations.append("Engage with comments in first hour")
        
        if content.platform == Platform.TIKTOK:
            recommendations.append("Use trending sounds and participate in challenges")
        elif content.platform == Platform.INSTAGRAM:
            recommendations.append("Share to Stories and use location tags")
        
        return recommendations
    
    def _get_virality_recommendations(
        self,
        content: ContentAsset,
        metrics: PerformanceMetrics
    ) -> List[str]:
        """Get recommendations for improving virality"""
        recommendations = []
        
        recommendations.append("Create content that triggers emotional response")
        recommendations.append("Make content easily shareable (relatable, funny, or valuable)")
        recommendations.append("Use pattern interrupts to grab attention")
        recommendations.append("Create content series to build anticipation")
        
        return recommendations
    
    def _generate_action_items(self, analysis: Dict[str, Any]) -> List[str]:
        """Generate specific action items from analysis"""
        action_items = []
        
        # Take top 3 most important recommendations
        for rec in analysis['recommendations'][:3]:
            action_items.append(f"TODO: {rec}")
        
        return action_items
    
    async def optimize_posting_schedule(
        self,
        platform: Platform,
        historical_metrics: List[PerformanceMetrics]
    ) -> Dict[str, Any]:
        """Optimize posting schedule based on historical performance"""
        
        # Analyze performance by time of day
        time_performance = {}
        
        for metrics in historical_metrics:
            hour = metrics.timestamp.hour
            if hour not in time_performance:
                time_performance[hour] = {
                    'total_engagement': 0,
                    'count': 0
                }
            
            time_performance[hour]['total_engagement'] += metrics.engagement_rate
            time_performance[hour]['count'] += 1
        
        # Calculate average engagement by hour
        best_hours = []
        for hour, data in time_performance.items():
            avg_engagement = data['total_engagement'] / data['count']
            best_hours.append({
                'hour': hour,
                'avg_engagement': avg_engagement
            })
        
        # Sort by engagement
        best_hours.sort(key=lambda x: x['avg_engagement'], reverse=True)
        
        return {
            'platform': platform,
            'best_posting_times': [
                f"{h['hour']:02d}:00" for h in best_hours[:3]
            ],
            'worst_posting_times': [
                f"{h['hour']:02d}:00" for h in best_hours[-3:]
            ],
            'recommendation': f"Post during {best_hours[0]['hour']:02d}:00-{(best_hours[0]['hour']+2)%24:02d}:00 for best results"
        }
    
    async def calibrate_strategy(
        self,
        platform: Platform,
        recent_performance: List[PerformanceMetrics]
    ) -> Dict[str, Any]:
        """Calibrate content strategy based on recent performance"""
        
        if not recent_performance:
            return {'message': 'Insufficient data for calibration'}
        
        # Calculate average metrics
        avg_engagement = sum(m.engagement_rate for m in recent_performance) / len(recent_performance)
        avg_views = sum(m.views for m in recent_performance) / len(recent_performance)
        
        strategy = {
            'platform': platform,
            'current_avg_engagement': avg_engagement,
            'current_avg_views': avg_views,
            'status': 'healthy' if avg_engagement > 0.05 else 'needs_improvement',
            'adjustments': []
        }
        
        # Suggest strategy adjustments
        if avg_engagement < 0.03:
            strategy['adjustments'].append('Focus on quality over quantity')
            strategy['adjustments'].append('Analyze top performing competitors')
            strategy['adjustments'].append('Experiment with different content formats')
        elif avg_engagement > 0.08:
            strategy['adjustments'].append('Scale up posting frequency')
            strategy['adjustments'].append('Double down on winning content types')
            strategy['adjustments'].append('Consider monetization opportunities')
        
        return strategy
