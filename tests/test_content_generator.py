"""
Unit tests for Content Generator module
"""

import pytest
from src.modules.content_generator import ContentGenerator
from src.config import Config


class TestContentGenerator:
    """Test cases for ContentGenerator"""
    
    def setup_method(self):
        """Setup test fixtures"""
        self.generator = ContentGenerator(Config)
        self.sample_niche = {
            'niche': 'Technology & AI',
            'profitability_score': 75.0
        }
        self.sample_trends = [
            {'topic': '#AI', 'volume': 10000, 'score': 85},
            {'topic': 'machine learning', 'volume': 8000, 'score': 80}
        ]
    
    def test_generator_initialization(self):
        """Test that generator initializes correctly"""
        assert self.generator is not None
        assert self.generator.config == Config
        assert self.generator.generated_content == []
    
    def test_generate_text_content(self):
        """Test text content generation"""
        content = self.generator.generate_content(
            self.sample_niche,
            self.sample_trends,
            "text"
        )
        
        assert content is not None
        assert content['type'] == 'text'
        assert 'hook' in content
        assert 'body' in content
        assert 'cta' in content
        assert 'hashtags' in content
        assert 'viral_score' in content
    
    def test_generate_image_content(self):
        """Test image content generation"""
        content = self.generator.generate_content(
            self.sample_niche,
            self.sample_trends,
            "image"
        )
        
        assert content is not None
        assert content['type'] == 'image'
        assert 'image_prompt' in content
        assert 'caption' in content
        assert 'style' in content
    
    def test_viral_score_calculation(self):
        """Test that viral score is calculated"""
        content = self.generator.generate_content(
            self.sample_niche,
            self.sample_trends,
            "text"
        )
        
        assert 'viral_score' in content
        assert isinstance(content['viral_score'], float)
        assert 0 <= content['viral_score'] <= 100
    
    def test_platform_optimization(self):
        """Test that content is optimized for platforms"""
        content = self.generator.generate_content(
            self.sample_niche,
            self.sample_trends,
            "text"
        )
        
        assert 'platform_optimized' in content
        platforms = content['platform_optimized']
        
        assert 'twitter' in platforms
        assert 'instagram' in platforms
        assert 'linkedin' in platforms
    
    def test_hashtag_generation(self):
        """Test that hashtags are generated"""
        content = self.generator.generate_content(
            self.sample_niche,
            self.sample_trends,
            "text"
        )
        
        assert 'hashtags' in content
        assert isinstance(content['hashtags'], list)
        assert len(content['hashtags']) > 0
        
        # All hashtags should start with #
        for tag in content['hashtags']:
            assert tag.startswith('#')
    
    def test_get_high_score_content(self):
        """Test filtering content by viral score"""
        # Generate some content
        for _ in range(3):
            self.generator.generate_content(
                self.sample_niche,
                self.sample_trends,
                "text"
            )
        
        high_score = self.generator.get_high_score_content(min_score=70)
        
        assert isinstance(high_score, list)
        
        # All returned content should have score >= 70
        for content in high_score:
            assert content['viral_score'] >= 70


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
