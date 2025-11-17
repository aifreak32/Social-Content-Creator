"""
Unit tests for Trend Analyzer module
"""

import pytest
from src.modules.trend_analyzer import TrendAnalyzer
from src.config import Config


class TestTrendAnalyzer:
    """Test cases for TrendAnalyzer"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.analyzer = TrendAnalyzer(Config)
    
    def test_analyzer_initialization(self):
        """Test that analyzer initializes correctly"""
        assert self.analyzer is not None
        assert self.analyzer.config == Config
        assert self.analyzer.trends_cache == []
        assert self.analyzer.last_update is None
    
    def test_analyze_trends_returns_list(self):
        """Test that analyze_trends returns a list"""
        trends = self.analyzer.analyze_trends()
        assert isinstance(trends, list)
        assert len(trends) > 0
    
    def test_trends_have_required_fields(self):
        """Test that trends contain required fields"""
        trends = self.analyzer.analyze_trends()
        
        required_fields = ['topic', 'volume', 'source', 'score', 'timestamp']
        
        for trend in trends:
            for field in required_fields:
                assert field in trend, f"Missing required field: {field}"
    
    def test_trends_are_scored(self):
        """Test that all trends have scores"""
        trends = self.analyzer.analyze_trends()
        
        for trend in trends:
            assert 'score' in trend
            assert isinstance(trend['score'], (int, float))
            assert 0 <= trend['score'] <= 100
    
    def test_trends_are_sorted_by_score(self):
        """Test that trends are sorted by score (descending)"""
        trends = self.analyzer.analyze_trends()
        
        if len(trends) > 1:
            scores = [t['score'] for t in trends]
            assert scores == sorted(scores, reverse=True)
    
    def test_get_top_trends(self):
        """Test getting top N trends"""
        self.analyzer.analyze_trends()
        top_5 = self.analyzer.get_top_trends(5)
        
        assert len(top_5) <= 5
        assert isinstance(top_5, list)
    
    def test_get_trend_keywords(self):
        """Test extracting keywords from trends"""
        trend = {
            'topic': '#AI technology',
            'volume': 10000,
            'score': 85
        }
        
        keywords = self.analyzer.get_trend_keywords(trend)
        
        assert isinstance(keywords, list)
        assert len(keywords) > 0
        assert 'ai' in keywords
    
    def test_cache_is_populated(self):
        """Test that trends are cached after analysis"""
        assert self.analyzer.trends_cache == []
        
        self.analyzer.analyze_trends()
        
        assert len(self.analyzer.trends_cache) > 0
        assert self.analyzer.last_update is not None
    
    def test_viability_classification(self):
        """Test that trends are classified by viability"""
        trends = self.analyzer.analyze_trends()
        
        for trend in trends:
            assert 'viability' in trend
            assert trend['viability'] in ['high', 'medium', 'low']


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
