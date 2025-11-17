"""
Niche Identification Module
Identifies profitable niches based on trend analysis and market data
"""

import logging
from typing import List, Dict, Any
from datetime import datetime
import numpy as np

logger = logging.getLogger(__name__)


class NicheIdentifier:
    """Identifies profitable niches for content creation"""
    
    def __init__(self, config):
        self.config = config
        self.identified_niches = []
        
    def identify_niches(self, trends: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Analyze trends and identify profitable niches
        """
        logger.info("Starting niche identification...")
        niches = []
        
        # Group trends by category
        categorized_trends = self._categorize_trends(trends)
        
        # Analyze each category for profitability
        for category, category_trends in categorized_trends.items():
            niche_data = self._analyze_niche_profitability(category, category_trends)
            if niche_data["profitability_score"] >= 60:
                niches.append(niche_data)
        
        # Sort by profitability
        niches.sort(key=lambda x: x["profitability_score"], reverse=True)
        
        self.identified_niches = niches
        logger.info(f"Identified {len(niches)} profitable niches")
        
        return niches
    
    def _categorize_trends(self, trends: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """Categorize trends into niche areas"""
        categories = {
            "Technology & AI": [],
            "Digital Marketing": [],
            "Content Creation": [],
            "Business & Entrepreneurship": [],
            "Lifestyle & Wellness": [],
            "Education & Learning": [],
            "Entertainment": [],
            "Finance & Investing": [],
        }
        
        # Keywords for each category
        category_keywords = {
            "Technology & AI": ["ai", "tech", "software", "automation", "machine learning"],
            "Digital Marketing": ["marketing", "seo", "social media", "advertising", "branding"],
            "Content Creation": ["content", "creation", "video", "creator", "influencer"],
            "Business & Entrepreneurship": ["business", "startup", "entrepreneurship", "ecommerce"],
            "Lifestyle & Wellness": ["lifestyle", "wellness", "health", "fitness", "mindfulness"],
            "Education & Learning": ["education", "learning", "course", "training", "tutorial"],
            "Entertainment": ["entertainment", "gaming", "music", "movie", "celebrity"],
            "Finance & Investing": ["finance", "investing", "crypto", "stocks", "money"],
        }
        
        for trend in trends:
            topic = trend.get("topic", "").lower()
            
            # Match to categories
            matched = False
            for category, keywords in category_keywords.items():
                if any(keyword in topic for keyword in keywords):
                    categories[category].append(trend)
                    matched = True
                    break
            
            # If no match, add to most general category
            if not matched:
                categories["Entertainment"].append(trend)
        
        # Remove empty categories
        return {k: v for k, v in categories.items() if v}
    
    def _analyze_niche_profitability(
        self, 
        category: str, 
        trends: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Analyze profitability of a niche based on multiple factors
        """
        # Calculate average metrics
        avg_volume = np.mean([t.get("volume", 0) for t in trends])
        avg_score = np.mean([t.get("score", 0) for t in trends])
        
        # Competition analysis (simulated)
        competition_level = self._assess_competition(category)
        
        # Monetization potential
        monetization_potential = self._assess_monetization(category)
        
        # Calculate profitability score
        profitability_score = (
            (avg_score * 0.3) +
            (min(avg_volume / 100000, 1.0) * 100 * 0.2) +
            ((100 - competition_level) * 0.2) +
            (monetization_potential * 0.3)
        )
        
        return {
            "niche": category,
            "trend_count": len(trends),
            "average_volume": int(avg_volume),
            "average_trend_score": round(avg_score, 2),
            "competition_level": competition_level,
            "monetization_potential": monetization_potential,
            "profitability_score": round(profitability_score, 2),
            "top_trends": trends[:3],
            "recommended_action": self._get_recommendation(profitability_score),
            "timestamp": datetime.now()
        }
    
    def _assess_competition(self, category: str) -> int:
        """
        Assess competition level in a niche (0-100)
        Lower is better
        """
        # Simulated competition levels based on category
        competition_map = {
            "Technology & AI": 70,
            "Digital Marketing": 85,
            "Content Creation": 80,
            "Business & Entrepreneurship": 75,
            "Lifestyle & Wellness": 65,
            "Education & Learning": 60,
            "Entertainment": 90,
            "Finance & Investing": 80,
        }
        
        return competition_map.get(category, 70)
    
    def _assess_monetization(self, category: str) -> int:
        """
        Assess monetization potential (0-100)
        Higher is better
        """
        # Simulated monetization potential based on category
        monetization_map = {
            "Technology & AI": 85,
            "Digital Marketing": 90,
            "Content Creation": 75,
            "Business & Entrepreneurship": 95,
            "Lifestyle & Wellness": 70,
            "Education & Learning": 80,
            "Entertainment": 65,
            "Finance & Investing": 95,
        }
        
        return monetization_map.get(category, 70)
    
    def _get_recommendation(self, profitability_score: float) -> str:
        """Get action recommendation based on profitability score"""
        if profitability_score >= 80:
            return "Highly recommended - Focus content creation here"
        elif profitability_score >= 60:
            return "Recommended - Good opportunity for growth"
        elif profitability_score >= 40:
            return "Moderate potential - Test with limited content"
        else:
            return "Low priority - Focus on other niches"
    
    def get_top_niches(self, n: int = 5) -> List[Dict[str, Any]]:
        """Get top N most profitable niches"""
        return self.identified_niches[:n]
    
    def get_niche_content_strategy(self, niche: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate content strategy for a specific niche
        """
        return {
            "niche": niche["niche"],
            "target_audience": self._identify_target_audience(niche),
            "content_types": self._recommend_content_types(niche),
            "posting_frequency": self._recommend_posting_frequency(niche),
            "best_platforms": self._identify_best_platforms(niche),
            "keywords": self._extract_niche_keywords(niche),
        }
    
    def _identify_target_audience(self, niche: Dict[str, Any]) -> str:
        """Identify target audience for niche"""
        audience_map = {
            "Technology & AI": "Tech professionals, developers, early adopters (25-45)",
            "Digital Marketing": "Business owners, marketers, entrepreneurs (25-50)",
            "Content Creation": "Creators, influencers, artists (18-35)",
            "Business & Entrepreneurship": "Entrepreneurs, business professionals (30-55)",
            "Lifestyle & Wellness": "Health-conscious individuals (25-45)",
            "Education & Learning": "Students, professionals, lifelong learners (18-65)",
            "Entertainment": "General audience, entertainment seekers (18-40)",
            "Finance & Investing": "Investors, professionals (25-60)",
        }
        
        return audience_map.get(niche["niche"], "General audience")
    
    def _recommend_content_types(self, niche: Dict[str, Any]) -> List[str]:
        """Recommend content types for niche"""
        content_types_map = {
            "Technology & AI": ["tutorials", "demos", "news", "reviews"],
            "Digital Marketing": ["tips", "case studies", "strategies", "tools"],
            "Content Creation": ["behind-the-scenes", "tutorials", "showcases"],
            "Business & Entrepreneurship": ["advice", "success stories", "strategies"],
            "Lifestyle & Wellness": ["tips", "routines", "inspiration"],
            "Education & Learning": ["tutorials", "courses", "tips"],
            "Entertainment": ["viral content", "memes", "challenges"],
            "Finance & Investing": ["analysis", "tips", "news"],
        }
        
        return content_types_map.get(niche["niche"], ["general content"])
    
    def _recommend_posting_frequency(self, niche: Dict[str, Any]) -> str:
        """Recommend posting frequency based on niche and engagement"""
        score = niche.get("profitability_score", 0)
        
        if score >= 80:
            return "2-3 posts per day"
        elif score >= 60:
            return "1-2 posts per day"
        else:
            return "3-5 posts per week"
    
    def _identify_best_platforms(self, niche: Dict[str, Any]) -> List[str]:
        """Identify best social media platforms for niche"""
        platform_map = {
            "Technology & AI": ["Twitter", "LinkedIn", "YouTube"],
            "Digital Marketing": ["LinkedIn", "Twitter", "Instagram"],
            "Content Creation": ["Instagram", "TikTok", "YouTube"],
            "Business & Entrepreneurship": ["LinkedIn", "Twitter", "YouTube"],
            "Lifestyle & Wellness": ["Instagram", "TikTok", "Pinterest"],
            "Education & Learning": ["YouTube", "LinkedIn", "Twitter"],
            "Entertainment": ["TikTok", "Instagram", "YouTube"],
            "Finance & Investing": ["Twitter", "LinkedIn", "YouTube"],
        }
        
        return platform_map.get(niche["niche"], ["Twitter", "Instagram"])
    
    def _extract_niche_keywords(self, niche: Dict[str, Any]) -> List[str]:
        """Extract keywords from niche trends"""
        keywords = set()
        
        for trend in niche.get("top_trends", []):
            topic = trend.get("topic", "").lower()
            # Remove special characters and split
            words = topic.replace("#", "").replace("@", "").split()
            keywords.update(words)
        
        return list(keywords)
