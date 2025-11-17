"""
Content Generation Module
AI-powered content generation for social media (text, images, videos)
"""

import logging
from typing import Dict, Any, List, Optional
from datetime import datetime
from pathlib import Path
import json
import random

logger = logging.getLogger(__name__)


class ContentGenerator:
    """Generates viral content using AI"""
    
    def __init__(self, config):
        self.config = config
        self.generated_content = []
        
    def generate_content(
        self, 
        niche: Dict[str, Any],
        trends: List[Dict[str, Any]],
        content_type: str = "text"
    ) -> Dict[str, Any]:
        """
        Generate content based on niche and trends
        
        Args:
            niche: Niche information
            trends: Related trending topics
            content_type: Type of content (text, image, video)
        """
        logger.info(f"Generating {content_type} content for niche: {niche.get('niche')}")
        
        # Generate content based on type
        if content_type == "text":
            content = self._generate_text_content(niche, trends)
        elif content_type == "image" and self.config.IMAGE_GENERATION_ENABLED:
            content = self._generate_image_content(niche, trends)
        elif content_type == "video" and self.config.VIDEO_GENERATION_ENABLED:
            content = self._generate_video_content(niche, trends)
        else:
            content = self._generate_text_content(niche, trends)
        
        # Score content for viral potential
        content["viral_score"] = self._calculate_viral_score(content)
        content["timestamp"] = datetime.now()
        
        # Store generated content
        self.generated_content.append(content)
        
        return content
    
    def _generate_text_content(
        self, 
        niche: Dict[str, Any],
        trends: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate text-based content"""
        
        # Extract keywords
        keywords = self._extract_keywords(niche, trends)
        
        # Generate engaging hooks
        hooks = self._generate_hooks(niche, keywords)
        
        # Generate main content using AI patterns
        content_body = self._generate_content_body(niche, keywords, hooks)
        
        # Generate call-to-action
        cta = self._generate_cta(niche)
        
        # Generate hashtags
        hashtags = self._generate_hashtags(keywords, trends)
        
        return {
            "type": "text",
            "niche": niche.get("niche"),
            "hook": hooks[0],
            "body": content_body,
            "cta": cta,
            "hashtags": hashtags,
            "full_text": f"{hooks[0]}\n\n{content_body}\n\n{cta}\n\n{' '.join(hashtags)}",
            "platform_optimized": self._optimize_for_platforms(hooks[0], content_body, cta, hashtags)
        }
    
    def _generate_image_content(
        self, 
        niche: Dict[str, Any],
        trends: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate image content (returns prompt for AI image generation)"""
        
        keywords = self._extract_keywords(niche, trends)
        
        # Create image generation prompt
        image_prompt = self._create_image_prompt(niche, keywords)
        
        # Generate caption
        caption = self._generate_image_caption(niche, keywords)
        
        # Generate hashtags
        hashtags = self._generate_hashtags(keywords, trends)
        
        return {
            "type": "image",
            "niche": niche.get("niche"),
            "image_prompt": image_prompt,
            "caption": caption,
            "hashtags": hashtags,
            "style": self._determine_visual_style(niche),
            "dimensions": {"width": 1024, "height": 1024},
            "note": "Use image_prompt with DALL-E or Stable Diffusion"
        }
    
    def _generate_video_content(
        self, 
        niche: Dict[str, Any],
        trends: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Generate video content concept"""
        
        keywords = self._extract_keywords(niche, trends)
        
        # Create video script
        script = self._create_video_script(niche, keywords)
        
        # Generate hashtags
        hashtags = self._generate_hashtags(keywords, trends)
        
        return {
            "type": "video",
            "niche": niche.get("niche"),
            "script": script,
            "duration": "30-60 seconds",
            "style": self._determine_video_style(niche),
            "hashtags": hashtags,
            "music_mood": self._suggest_music_mood(niche),
            "note": "Use script with AI video generation tools"
        }
    
    def _extract_keywords(
        self, 
        niche: Dict[str, Any],
        trends: List[Dict[str, Any]]
    ) -> List[str]:
        """Extract relevant keywords from niche and trends"""
        keywords = set()
        
        # Add niche name
        keywords.add(niche.get("niche", ""))
        
        # Add trend topics
        for trend in trends[:5]:
            topic = trend.get("topic", "").replace("#", "").replace("@", "")
            keywords.update(topic.split())
        
        return list(keywords)
    
    def _generate_hooks(self, niche: Dict[str, Any], keywords: List[str]) -> List[str]:
        """Generate attention-grabbing hooks"""
        
        hook_templates = [
            f"🚀 The secret to success in {niche.get('niche')} that nobody talks about:",
            f"💡 This {niche.get('niche')} strategy increased engagement by 300%:",
            f"⚡ Stop doing {niche.get('niche')} wrong. Here's the right way:",
            f"🔥 Why everyone in {niche.get('niche')} is talking about this:",
            f"✨ The future of {niche.get('niche')} is here, and it's amazing:",
        ]
        
        return hook_templates
    
    def _generate_content_body(
        self, 
        niche: Dict[str, Any],
        keywords: List[str],
        hooks: List[str]
    ) -> str:
        """Generate main content body"""
        
        templates = [
            f"""Here's what changed everything:

1. Understanding the market trends
2. Leveraging AI and automation
3. Creating authentic, valuable content
4. Engaging with your audience consistently
5. Analyzing data and optimizing

The results speak for themselves.""",
            
            f"""I've tested this for months, and here are the results:

→ 10x increase in engagement
→ 5x more followers
→ 3x higher conversion rates

The strategy is simple but powerful.""",
            
            f"""Most people get this wrong. Here's what actually works:

✅ Focus on quality over quantity
✅ Use data to guide decisions
✅ Stay authentic and consistent
✅ Leverage trending topics wisely
✅ Optimize based on performance

Game-changing insights."""
        ]
        
        return random.choice(templates)
    
    def _generate_cta(self, niche: Dict[str, Any]) -> str:
        """Generate call-to-action"""
        
        ctas = [
            "💬 What's your experience? Share in the comments!",
            "🔔 Follow for more tips and strategies!",
            "💾 Save this for later and share with someone who needs it!",
            "👇 Drop a comment if this helped you!",
            "🚀 Ready to transform your strategy? Let's connect!",
        ]
        
        return random.choice(ctas)
    
    def _generate_hashtags(
        self, 
        keywords: List[str],
        trends: List[Dict[str, Any]]
    ) -> List[str]:
        """Generate relevant hashtags"""
        
        hashtags = []
        
        # Add trending hashtags
        for trend in trends[:3]:
            topic = trend.get("topic", "")
            if topic.startswith("#"):
                hashtags.append(topic)
        
        # Add keyword-based hashtags
        for keyword in keywords[:3]:
            if keyword and len(keyword) > 2:
                hashtags.append(f"#{keyword.replace(' ', '')}")
        
        # Add general engagement hashtags
        general_tags = ["#GrowthTips", "#ViralContent", "#SocialMedia", "#ContentCreator"]
        hashtags.extend(random.sample(general_tags, 2))
        
        return hashtags[:10]
    
    def _optimize_for_platforms(
        self, 
        hook: str, 
        body: str, 
        cta: str, 
        hashtags: List[str]
    ) -> Dict[str, str]:
        """Optimize content for different platforms"""
        
        return {
            "twitter": f"{hook}\n\n{body[:200]}...\n\n{' '.join(hashtags[:5])}",
            "instagram": f"{hook}\n\n{body}\n\n{cta}\n\n{' '.join(hashtags)}",
            "linkedin": f"{hook}\n\n{body}\n\n{cta}",
            "tiktok": f"{hook}\n\n{body}\n\n{' '.join(hashtags[:5])}",
        }
    
    def _create_image_prompt(self, niche: Dict[str, Any], keywords: List[str]) -> str:
        """Create prompt for AI image generation"""
        
        style_map = {
            "Technology & AI": "futuristic, high-tech, clean design, blue and purple colors",
            "Digital Marketing": "modern, professional, vibrant colors, infographic style",
            "Content Creation": "creative, artistic, colorful, inspiring",
            "Business & Entrepreneurship": "professional, sophisticated, corporate colors",
            "Lifestyle & Wellness": "calm, natural, warm tones, minimalist",
            "Education & Learning": "clear, educational, friendly, organized",
            "Entertainment": "fun, vibrant, dynamic, eye-catching",
            "Finance & Investing": "professional, trustworthy, green and gold tones",
        }
        
        niche_name = niche.get("niche", "general")
        style = style_map.get(niche_name, "modern, professional")
        
        prompt = f"Create a {style} image representing {niche_name}, " \
                f"featuring elements related to {', '.join(keywords[:3])}, " \
                f"optimized for social media, high quality, visually appealing"
        
        return prompt
    
    def _generate_image_caption(self, niche: Dict[str, Any], keywords: List[str]) -> str:
        """Generate caption for image post"""
        
        captions = [
            f"🎨 Visual inspiration for {niche.get('niche')} lovers!",
            f"✨ This is what success in {niche.get('niche')} looks like",
            f"💫 Transform your {niche.get('niche')} game with this perspective",
        ]
        
        return random.choice(captions)
    
    def _determine_visual_style(self, niche: Dict[str, Any]) -> str:
        """Determine visual style for content"""
        
        style_map = {
            "Technology & AI": "minimalist-modern",
            "Digital Marketing": "infographic",
            "Content Creation": "creative-artistic",
            "Business & Entrepreneurship": "professional-clean",
            "Lifestyle & Wellness": "natural-organic",
            "Education & Learning": "educational-friendly",
            "Entertainment": "vibrant-dynamic",
            "Finance & Investing": "corporate-trustworthy",
        }
        
        return style_map.get(niche.get("niche"), "modern-professional")
    
    def _create_video_script(self, niche: Dict[str, Any], keywords: List[str]) -> Dict[str, str]:
        """Create video script structure"""
        
        return {
            "hook": f"Wait, you need to see this about {niche.get('niche')}! (0-3s)",
            "introduction": f"Here's what changed my entire approach to {niche.get('niche')}... (3-10s)",
            "main_content": "Share the key insight or tip with visual examples (10-45s)",
            "call_to_action": "Follow for more tips! What do you think? Comment below! (45-60s)"
        }
    
    def _determine_video_style(self, niche: Dict[str, Any]) -> str:
        """Determine video style"""
        
        style_map = {
            "Technology & AI": "fast-paced with tech visuals",
            "Digital Marketing": "tutorial/educational style",
            "Content Creation": "behind-the-scenes, creative",
            "Business & Entrepreneurship": "professional talking head",
            "Lifestyle & Wellness": "calm, aesthetic b-roll",
            "Education & Learning": "clear, step-by-step tutorial",
            "Entertainment": "trending format, viral style",
            "Finance & Investing": "professional analysis style",
        }
        
        return style_map.get(niche.get("niche"), "engaging, professional")
    
    def _suggest_music_mood(self, niche: Dict[str, Any]) -> str:
        """Suggest music mood for video"""
        
        mood_map = {
            "Technology & AI": "electronic, upbeat",
            "Digital Marketing": "motivational, uplifting",
            "Content Creation": "creative, inspiring",
            "Business & Entrepreneurship": "ambitious, powerful",
            "Lifestyle & Wellness": "calm, peaceful",
            "Education & Learning": "light, friendly",
            "Entertainment": "trending, catchy",
            "Finance & Investing": "confident, professional",
        }
        
        return mood_map.get(niche.get("niche"), "upbeat, positive")
    
    def _calculate_viral_score(self, content: Dict[str, Any]) -> float:
        """Calculate potential viral score for content"""
        
        score = 0.0
        
        # Hook quality (30 points)
        hook = content.get("hook", "")
        if any(emoji in hook for emoji in ["🚀", "💡", "⚡", "🔥", "✨"]):
            score += 10
        if len(hook) > 20 and len(hook) < 100:
            score += 10
        if "?" in hook or "!" in hook:
            score += 10
        
        # Hashtag relevance (20 points)
        hashtags = content.get("hashtags", [])
        if len(hashtags) >= 5:
            score += 10
        if len(hashtags) <= 10:
            score += 10
        
        # Content structure (30 points)
        body = content.get("body", "")
        if len(body) > 100:
            score += 15
        if any(bullet in body for bullet in ["→", "✅", "1.", "2."]):
            score += 15
        
        # Platform optimization (20 points)
        if content.get("platform_optimized"):
            score += 20
        
        return round(min(score, 100), 2)
    
    def get_high_score_content(self, min_score: float = None) -> List[Dict[str, Any]]:
        """Get content with high viral scores"""
        
        if min_score is None:
            min_score = self.config.MIN_ENGAGEMENT_SCORE
        
        return [c for c in self.generated_content if c.get("viral_score", 0) >= min_score]
