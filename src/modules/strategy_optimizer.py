"""
Strategy Optimization Module
Data-driven optimization of content strategy and posting schedule
"""

import logging
from typing import Dict, Any, List
from datetime import datetime, timedelta
import numpy as np
from collections import defaultdict

logger = logging.getLogger(__name__)


class StrategyOptimizer:
    """Optimizes content strategy based on performance data"""
    
    def __init__(self, config):
        self.config = config
        self.performance_history = []
        self.optimization_insights = []
        
    def analyze_performance(
        self, 
        content_posts: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Analyze performance of published content
        """
        logger.info("Analyzing content performance...")
        
        if not content_posts:
            return {
                "status": "insufficient_data",
                "message": "Need at least one post to analyze"
            }
        
        # Calculate key metrics
        metrics = self._calculate_metrics(content_posts)
        
        # Identify best performing content
        best_performers = self._identify_best_performers(content_posts)
        
        # Analyze posting patterns
        posting_insights = self._analyze_posting_patterns(content_posts)
        
        # Generate optimization recommendations
        recommendations = self._generate_recommendations(metrics, best_performers, posting_insights)
        
        analysis = {
            "metrics": metrics,
            "best_performers": best_performers,
            "posting_insights": posting_insights,
            "recommendations": recommendations,
            "timestamp": datetime.now()
        }
        
        self.performance_history.append(analysis)
        
        return analysis
    
    def _calculate_metrics(self, posts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Calculate performance metrics"""
        
        total_posts = len(posts)
        
        # Simulated engagement metrics (in real implementation, fetch from APIs)
        engagement_rates = [self._simulate_engagement() for _ in posts]
        avg_engagement = np.mean(engagement_rates)
        
        # Calculate other metrics
        viral_scores = [p.get("viral_score", 0) for p in posts]
        avg_viral_score = np.mean(viral_scores) if viral_scores else 0
        
        # Growth metrics
        follower_growth = self._calculate_follower_growth(posts)
        
        return {
            "total_posts": total_posts,
            "average_engagement_rate": round(avg_engagement, 4),
            "average_viral_score": round(avg_viral_score, 2),
            "follower_growth_rate": round(follower_growth, 4),
            "best_engagement_rate": round(max(engagement_rates) if engagement_rates else 0, 4),
            "consistency_score": self._calculate_consistency_score(posts)
        }
    
    def _simulate_engagement(self) -> float:
        """Simulate engagement rate (replace with real API data)"""
        # Random engagement between 1% and 10%
        return np.random.uniform(0.01, 0.10)
    
    def _calculate_follower_growth(self, posts: List[Dict[str, Any]]) -> float:
        """Calculate follower growth rate"""
        # Simulated growth rate
        return np.random.uniform(0.01, 0.05)
    
    def _calculate_consistency_score(self, posts: List[Dict[str, Any]]) -> float:
        """Calculate posting consistency score"""
        if len(posts) < 2:
            return 100.0
        
        # Calculate time gaps between posts
        timestamps = [p.get("timestamp", datetime.now()) for p in posts]
        timestamps.sort()
        
        gaps = [(timestamps[i+1] - timestamps[i]).total_seconds() / 3600 
                for i in range(len(timestamps)-1)]
        
        # Lower variance = higher consistency
        if gaps:
            variance = np.var(gaps)
            consistency = max(0, 100 - (variance / 10))
        else:
            consistency = 100
        
        return round(consistency, 2)
    
    def _identify_best_performers(
        self, 
        posts: List[Dict[str, Any]],
        top_n: int = 5
    ) -> List[Dict[str, Any]]:
        """Identify best performing content"""
        
        # Score posts based on multiple factors
        scored_posts = []
        for post in posts:
            score = (
                post.get("viral_score", 0) * 0.4 +
                self._simulate_engagement() * 1000 * 0.6
            )
            
            scored_posts.append({
                **post,
                "performance_score": round(score, 2)
            })
        
        # Sort by performance
        scored_posts.sort(key=lambda x: x["performance_score"], reverse=True)
        
        return scored_posts[:top_n]
    
    def _analyze_posting_patterns(self, posts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze posting patterns and timing"""
        
        if not posts:
            return {}
        
        # Analyze by time of day
        hour_performance = defaultdict(list)
        day_performance = defaultdict(list)
        
        for post in posts:
            timestamp = post.get("timestamp", datetime.now())
            hour = timestamp.hour
            day = timestamp.strftime("%A")
            
            engagement = self._simulate_engagement()
            hour_performance[hour].append(engagement)
            day_performance[day].append(engagement)
        
        # Find best times
        best_hours = sorted(
            [(h, np.mean(scores)) for h, scores in hour_performance.items()],
            key=lambda x: x[1],
            reverse=True
        )[:3]
        
        best_days = sorted(
            [(d, np.mean(scores)) for d, scores in day_performance.items()],
            key=lambda x: x[1],
            reverse=True
        )[:3]
        
        return {
            "best_hours": [f"{h:02d}:00" for h, _ in best_hours],
            "best_days": [d for d, _ in best_days],
            "posting_frequency": len(posts) / max(1, (datetime.now() - posts[0].get("timestamp", datetime.now())).days),
        }
    
    def _generate_recommendations(
        self,
        metrics: Dict[str, Any],
        best_performers: List[Dict[str, Any]],
        posting_insights: Dict[str, Any]
    ) -> List[str]:
        """Generate actionable recommendations"""
        
        recommendations = []
        
        # Engagement recommendations
        avg_engagement = metrics.get("average_engagement_rate", 0)
        if avg_engagement < self.config.TARGET_ENGAGEMENT_RATE:
            recommendations.append(
                f"📊 Increase engagement: Current rate ({avg_engagement:.2%}) is below target "
                f"({self.config.TARGET_ENGAGEMENT_RATE:.2%}). Focus on more interactive content."
            )
        else:
            recommendations.append(
                f"✅ Great engagement rate ({avg_engagement:.2%})! Keep up the good work."
            )
        
        # Viral score recommendations
        avg_viral = metrics.get("average_viral_score", 0)
        if avg_viral < self.config.MIN_ENGAGEMENT_SCORE:
            recommendations.append(
                f"🎯 Improve content quality: Average viral score ({avg_viral:.1f}) is below "
                f"threshold ({self.config.MIN_ENGAGEMENT_SCORE}). Use more engaging hooks and CTAs."
            )
        
        # Posting time recommendations
        if posting_insights.get("best_hours"):
            best_hours = ", ".join(posting_insights["best_hours"])
            recommendations.append(
                f"⏰ Optimal posting times: {best_hours}. Schedule more content during these hours."
            )
        
        # Posting frequency recommendations
        posting_freq = posting_insights.get("posting_frequency", 0)
        if posting_freq < 1:
            recommendations.append(
                "📅 Increase posting frequency: Aim for at least 1 post per day for better growth."
            )
        elif posting_freq > self.config.MAX_POSTS_PER_DAY:
            recommendations.append(
                f"⚠️ Reduce posting frequency: {posting_freq:.1f} posts/day may overwhelm audience. "
                f"Aim for {self.config.MAX_POSTS_PER_DAY} or fewer."
            )
        
        # Content type recommendations
        if best_performers:
            top_type = best_performers[0].get("type", "text")
            recommendations.append(
                f"🎨 Focus on {top_type} content: This type is performing best for your audience."
            )
        
        # Consistency recommendations
        consistency = metrics.get("consistency_score", 0)
        if consistency < 70:
            recommendations.append(
                "📊 Improve posting consistency: Maintain a regular schedule for better algorithm performance."
            )
        
        return recommendations
    
    def optimize_posting_schedule(
        self,
        niche: Dict[str, Any],
        performance_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Generate optimized posting schedule
        """
        logger.info("Generating optimized posting schedule...")
        
        # Get best posting times
        best_hours = performance_data.get("posting_insights", {}).get("best_hours", ["09:00", "12:00", "18:00"])
        best_days = performance_data.get("posting_insights", {}).get("best_days", ["Monday", "Wednesday", "Friday"])
        
        # Calculate optimal frequency
        target_engagement = self.config.TARGET_ENGAGEMENT_RATE
        current_engagement = performance_data.get("metrics", {}).get("average_engagement_rate", 0.03)
        
        if current_engagement >= target_engagement:
            posts_per_day = min(self.config.MAX_POSTS_PER_DAY, 3)
        else:
            posts_per_day = min(self.config.MAX_POSTS_PER_DAY, 2)
        
        # Generate schedule
        schedule = {
            "posts_per_day": posts_per_day,
            "best_hours": best_hours,
            "best_days": best_days,
            "recommended_schedule": self._create_weekly_schedule(posts_per_day, best_hours, best_days),
            "content_mix": self._recommend_content_mix(niche)
        }
        
        return schedule
    
    def _create_weekly_schedule(
        self,
        posts_per_day: int,
        best_hours: List[str],
        best_days: List[str]
    ) -> List[Dict[str, Any]]:
        """Create a weekly posting schedule"""
        
        schedule = []
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        
        for day in days_of_week:
            day_schedule = {
                "day": day,
                "priority": "high" if day in best_days else "normal",
                "posts": []
            }
            
            # Distribute posts throughout the day
            hours_to_use = best_hours[:posts_per_day]
            for i, hour in enumerate(hours_to_use):
                day_schedule["posts"].append({
                    "time": hour,
                    "content_type": self._assign_content_type(i, posts_per_day)
                })
            
            schedule.append(day_schedule)
        
        return schedule
    
    def _assign_content_type(self, post_index: int, total_posts: int) -> str:
        """Assign content type based on posting pattern"""
        
        content_types = ["text", "image", "video", "carousel"]
        
        # Vary content types throughout the day
        if total_posts == 1:
            return "image"  # Single post should be visual
        elif total_posts == 2:
            return "image" if post_index == 0 else "text"
        else:
            return content_types[post_index % len(content_types)]
    
    def _recommend_content_mix(self, niche: Dict[str, Any]) -> Dict[str, float]:
        """Recommend content type distribution"""
        
        # Base mix
        mix = {
            "text": 0.30,
            "image": 0.40,
            "video": 0.20,
            "carousel": 0.10
        }
        
        # Adjust based on niche
        niche_name = niche.get("niche", "")
        
        if "Technology" in niche_name or "AI" in niche_name:
            mix["video"] += 0.10
            mix["text"] -= 0.10
        elif "Lifestyle" in niche_name or "Wellness" in niche_name:
            mix["image"] += 0.10
            mix["text"] -= 0.10
        elif "Education" in niche_name:
            mix["carousel"] += 0.10
            mix["image"] -= 0.10
        
        return mix
    
    def calculate_monetization_readiness(
        self,
        metrics: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Calculate readiness for monetization
        """
        logger.info("Calculating monetization readiness...")
        
        # Simulated follower count (replace with real data)
        follower_count = np.random.randint(5000, 50000)
        
        engagement_rate = metrics.get("average_engagement_rate", 0)
        
        # Check criteria
        follower_ready = follower_count >= self.config.MIN_FOLLOWERS_FOR_MONETIZATION
        engagement_ready = engagement_rate >= self.config.TARGET_ENGAGEMENT_RATE
        
        readiness_score = 0
        if follower_ready:
            readiness_score += 50
        if engagement_ready:
            readiness_score += 50
        
        return {
            "ready_for_monetization": follower_ready and engagement_ready,
            "readiness_score": readiness_score,
            "follower_count": follower_count,
            "follower_requirement": self.config.MIN_FOLLOWERS_FOR_MONETIZATION,
            "engagement_rate": engagement_rate,
            "engagement_requirement": self.config.TARGET_ENGAGEMENT_RATE,
            "recommendations": self._get_monetization_recommendations(
                follower_ready, 
                engagement_ready,
                follower_count
            )
        }
    
    def _get_monetization_recommendations(
        self,
        follower_ready: bool,
        engagement_ready: bool,
        follower_count: int
    ) -> List[str]:
        """Get monetization recommendations"""
        
        recommendations = []
        
        if not follower_ready:
            gap = self.config.MIN_FOLLOWERS_FOR_MONETIZATION - follower_count
            recommendations.append(
                f"📈 Grow {gap:,} more followers to reach monetization threshold"
            )
        
        if not engagement_ready:
            recommendations.append(
                "💬 Increase engagement through more interactive content and community building"
            )
        
        if follower_ready and engagement_ready:
            recommendations.extend([
                "✅ Ready for brand partnerships and sponsorships",
                "💰 Consider affiliate marketing opportunities",
                "🎯 Explore platform monetization programs",
                "📊 Create exclusive content for monetization"
            ])
        
        return recommendations
