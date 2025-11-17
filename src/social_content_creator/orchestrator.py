"""
Main Orchestrator - Complete Workflow Management
"""
import asyncio
import json
import os
from typing import Dict, Any, List, Optional
from datetime import datetime
import uuid

from .config import config
from .models import CreationCycle, Platform, Trend, ContentAsset
from .trend_analysis.aggregator import CrossPlatformAnalyzer
from .research_scouting.scanner import ViralContentScanner
from .research_scouting.market_gap import MarketGapAnalyzer
from .niche_strategy.profitability import NicheProfitabilityAnalyzer
from .content_creation.video_generator import AIVideoGenerator
from .content_creation.image_generator import AIImageGenerator
from .content_creation.copywriter import ViralCopywriter
from .performance_analysis.metrics import MetricsTracker
from .performance_analysis.optimizer import OptimizationEngine


class SocialContentCreator:
    """
    Main orchestrator for the complete content creation workflow
    
    Workflow:
    PHASE 1: SCANNING → Analisi trend cross-platform
    PHASE 2: IDENTIFICAZIONE → Selezione nicchie/opportunità
    PHASE 3: CREAZIONE → Generazione contenuti multimediali
    PHASE 4: PUBBLICAZIONE → Posting ottimizzato
    PHASE 5: ANALISI → Monitoraggio e ottimizzazione
    """
    
    def __init__(self):
        self.config = config
        
        # Initialize all components
        self.trend_analyzer = CrossPlatformAnalyzer(config)
        self.viral_scanner = ViralContentScanner()
        self.market_analyzer = MarketGapAnalyzer()
        self.niche_analyzer = NicheProfitabilityAnalyzer()
        self.video_generator = AIVideoGenerator()
        self.image_generator = AIImageGenerator()
        self.copywriter = ViralCopywriter()
        self.metrics_tracker = MetricsTracker()
        self.optimizer = OptimizationEngine()
    
    async def execute_full_cycle(
        self,
        target_niches: Optional[List[str]] = None,
        video_count: int = 5,
        image_count: int = 10
    ) -> CreationCycle:
        """
        Execute complete content creation cycle
        
        Returns: CreationCycle with all generated assets and strategies
        """
        cycle_id = str(uuid.uuid4())
        print(f"🚀 Starting Content Creation Cycle: {cycle_id}")
        
        # PHASE 1: SCANNING - Analisi trend cross-platform
        print("\n📊 PHASE 1: Scanning trends across platforms...")
        trend_report = await self._phase_1_scanning()
        
        # PHASE 2: IDENTIFICAZIONE - Selezione nicchie/opportunità  
        print("\n🎯 PHASE 2: Identifying niches and opportunities...")
        niche_recommendations = await self._phase_2_identification(
            trend_report, 
            target_niches
        )
        
        # PHASE 3: CREAZIONE - Generazione contenuti multimediali
        print("\n🎨 PHASE 3: Creating multimedia content...")
        video_assets, image_assets, copywriting = await self._phase_3_creation(
            trend_report,
            niche_recommendations,
            video_count,
            image_count
        )
        
        # PHASE 4: PUBBLICAZIONE - Piano publishing ottimizzato
        print("\n📅 PHASE 4: Creating publishing plan...")
        publishing_plan = await self._phase_4_publishing(
            video_assets,
            image_assets
        )
        
        # PHASE 5: ANALISI - Strategia crescita
        print("\n📈 PHASE 5: Creating growth strategy...")
        growth_strategy = await self._phase_5_analysis(niche_recommendations)
        
        # Create complete cycle output
        cycle = CreationCycle(
            cycle_id=cycle_id,
            trend_report=trend_report,
            niche_recommendations=niche_recommendations,
            video_assets=video_assets,
            image_assets=image_assets,
            copywriting=copywriting,
            publishing_plan=publishing_plan,
            growth_strategy=growth_strategy
        )
        
        # Save cycle report
        await self._save_cycle_report(cycle)
        
        print(f"\n✅ Cycle {cycle_id} completed successfully!")
        return cycle
    
    async def _phase_1_scanning(self) -> List[Trend]:
        """Phase 1: Cross-platform trend analysis"""
        
        # Fetch trends from all platforms
        all_trends = await self.trend_analyzer.fetch_all_trends(limit_per_platform=10)
        
        # Identify cross-platform patterns
        patterns = self.trend_analyzer.identify_cross_platform_patterns(all_trends)
        
        # Predict emerging trends
        predictions = self.trend_analyzer.predict_emerging_trends(all_trends)
        
        # Compile trend report
        trend_report = []
        for platform, trends in all_trends.items():
            trend_report.extend(trends[:5])  # Top 5 from each platform
        
        print(f"  ✓ Found {len(trend_report)} trending topics")
        print(f"  ✓ Identified {len(patterns)} cross-platform patterns")
        print(f"  ✓ Predicted {len(predictions)} emerging trends")
        
        return trend_report
    
    async def _phase_2_identification(
        self,
        trends: List[Trend],
        target_niches: Optional[List[str]] = None
    ) -> List[Any]:
        """Phase 2: Niche and opportunity identification"""
        
        # Scan viral content
        viral_content = await self.viral_scanner.scan_all_platforms(timeframe_hours=24)
        
        # Identify viral patterns
        all_viral = []
        for platform, contents in viral_content.items():
            all_viral.extend(contents)
        
        viral_patterns = self.viral_scanner.identify_viral_patterns(all_viral)
        
        # Identify market gaps
        gaps = self.market_analyzer.identify_gaps(viral_patterns, [])
        
        # Analyze profitability for target niches
        if not target_niches:
            # Use identified gaps as target niches
            target_niches = [gap['niche'] for gap in gaps[:5]]
        
        niche_analyses = []
        for niche in target_niches:
            analysis = self.niche_analyzer.analyze_niche(niche)
            niche_analyses.append(analysis)
        
        # Sort by potential score
        niche_analyses.sort(key=lambda x: x.potential_score, reverse=True)
        
        print(f"  ✓ Analyzed {len(niche_analyses)} niches")
        print(f"  ✓ Top niche: {niche_analyses[0].niche_name if niche_analyses else 'N/A'}")
        
        return niche_analyses[:3]  # Return top 3 niches
    
    async def _phase_3_creation(
        self,
        trends: List[Trend],
        niches: List[Any],
        video_count: int = 5,
        image_count: int = 10
    ) -> tuple:
        """Phase 3: Multimedia content creation"""
        
        video_assets = []
        image_assets = []
        copywriting = {}
        
        # Generate videos
        print(f"  📹 Generating {video_count} videos...")
        for i in range(video_count):
            niche = niches[i % len(niches)] if niches else None
            trend = trends[i % len(trends)] if trends else None
            
            topic = niche.niche_name if niche else (trend.name if trend else "General Content")
            platform = Platform.TIKTOK if i % 2 == 0 else Platform.INSTAGRAM
            
            # Generate hook
            hook = await self.copywriter.generate_hook(topic, platform)
            
            # Generate video
            video = await self.video_generator.generate_reels_tiktok(
                topic=topic,
                hook=hook,
                platform=platform
            )
            
            video_assets.append(video)
        
        # Generate images
        print(f"  🖼️  Generating {image_count} images...")
        for i in range(image_count):
            niche = niches[i % len(niches)] if niches else None
            topic = niche.niche_name if niche else "Viral Content"
            
            platform = Platform.INSTAGRAM
            
            if i % 3 == 0:
                # Create carousel
                slides = [f"Tip {j+1}: {topic}" for j in range(5)]
                image = await self.image_generator.generate_carousel(
                    topic=topic,
                    slides=slides,
                    platform=platform
                )
            elif i % 3 == 1:
                # Create meme
                image = await self.image_generator.create_meme(
                    topic=topic,
                    platform=platform
                )
            else:
                # Create standard image
                image = await self.image_generator.generate_image_from_prompt(
                    prompt=f"Create engaging visual about {topic}",
                    platform=platform
                )
            
            image_assets.append(image)
        
        # Generate platform-specific copywriting
        print("  ✍️  Generating optimized copy...")
        for platform in [Platform.TIKTOK, Platform.INSTAGRAM, Platform.YOUTUBE, Platform.TWITTER]:
            topic = niches[0].niche_name if niches else "Trending Content"
            caption = await self.copywriter.generate_caption(
                topic=topic,
                platform=platform
            )
            copywriting[platform] = caption
        
        print(f"  ✓ Created {len(video_assets)} videos")
        print(f"  ✓ Created {len(image_assets)} images")
        print(f"  ✓ Generated copy for {len(copywriting)} platforms")
        
        return video_assets, image_assets, copywriting
    
    async def _phase_4_publishing(
        self,
        videos: List[ContentAsset],
        images: List[ContentAsset]
    ) -> Dict[str, Any]:
        """Phase 4: Publishing plan optimization"""
        
        publishing_plan = {
            'daily_schedule': [],
            'platform_strategy': {},
            'best_posting_times': {}
        }
        
        # Optimize posting times for each platform
        for platform in [Platform.TIKTOK, Platform.INSTAGRAM, Platform.YOUTUBE]:
            # Mock historical data for optimization
            publishing_plan['best_posting_times'][platform.value] = [
                "09:00-11:00",
                "12:00-14:00", 
                "18:00-20:00"
            ]
            
            publishing_plan['platform_strategy'][platform.value] = {
                'posting_frequency': '2-3x daily' if platform in [Platform.TIKTOK, Platform.INSTAGRAM] else '3-4x weekly',
                'content_mix': {
                    'video': 70,
                    'image': 30
                } if platform != Platform.YOUTUBE else {
                    'video': 100,
                    'image': 0
                }
            }
        
        # Create daily schedule
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        for day in days:
            publishing_plan['daily_schedule'].append({
                'day': day,
                'posts': 3 if day not in ['Saturday', 'Sunday'] else 2,
                'platforms': [Platform.TIKTOK.value, Platform.INSTAGRAM.value]
            })
        
        return publishing_plan
    
    async def _phase_5_analysis(
        self,
        niches: List[Any]
    ) -> Dict[str, Any]:
        """Phase 5: Growth strategy and optimization"""
        
        growth_strategy = {
            'short_term': {
                'duration': '0-30 days',
                'goals': [
                    'Post consistently (2-3x daily)',
                    'Reach 1,000 followers',
                    'Build content library',
                    'Engage with audience'
                ],
                'tactics': [
                    'Use trending sounds/hashtags',
                    'Optimize posting times',
                    'Respond to all comments',
                    'Create hook-driven content'
                ]
            },
            'mid_term': {
                'duration': '1-3 months',
                'goals': [
                    'Reach 10,000 followers',
                    'Achieve consistent 5%+ engagement',
                    'Start monetization planning',
                    'Build brand identity'
                ],
                'tactics': [
                    'Start content series',
                    'Collaborate with creators',
                    'Cross-platform promotion',
                    'Build email list'
                ]
            },
            'long_term': {
                'duration': '3-12 months',
                'goals': [
                    'Reach 100,000+ followers',
                    'Generate revenue streams',
                    'Become niche authority',
                    'Scale operations'
                ],
                'tactics': [
                    'Launch digital products',
                    'Secure brand partnerships',
                    'Build team/automation',
                    'Expand to new platforms'
                ]
            }
        }
        
        if niches:
            top_niche = niches[0]
            growth_strategy['niche_specific'] = top_niche.growth_strategy
            growth_strategy['monetization'] = {
                'opportunities': top_niche.monetization_opportunities,
                'priority': top_niche.monetization_opportunities[0] if top_niche.monetization_opportunities else None
            }
        
        return growth_strategy
    
    async def _save_cycle_report(self, cycle: CreationCycle):
        """Save cycle report to file"""
        
        report_dir = os.path.join(self.config.app.output_dir, "reports")
        os.makedirs(report_dir, exist_ok=True)
        
        report_file = os.path.join(
            report_dir,
            f"cycle_{cycle.cycle_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )
        
        # Convert to dict for JSON serialization
        report_data = {
            'cycle_id': cycle.cycle_id,
            'created_at': cycle.created_at.isoformat(),
            'summary': {
                'trends_analyzed': len(cycle.trend_report),
                'niches_recommended': len(cycle.niche_recommendations),
                'videos_created': len(cycle.video_assets),
                'images_created': len(cycle.image_assets),
                'platforms_covered': list(cycle.copywriting.keys())
            },
            'trend_report': [
                {
                    'name': t.name,
                    'platform': t.platform.value,
                    'engagement_score': t.engagement_score
                } for t in cycle.trend_report
            ],
            'niche_recommendations': [
                {
                    'niche': n.niche_name,
                    'potential_score': n.potential_score,
                    'profitability_score': n.profitability_score
                } for n in cycle.niche_recommendations
            ],
            'publishing_plan': cycle.publishing_plan,
            'growth_strategy': cycle.growth_strategy
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📄 Report saved: {report_file}")
    
    async def quick_analysis(self) -> Dict[str, Any]:
        """Quick trend analysis without full content generation"""
        
        print("🔍 Running quick trend analysis...")
        
        trends = await self._phase_1_scanning()
        niches = await self._phase_2_identification(trends)
        
        return {
            'trends': trends,
            'recommended_niches': niches,
            'timestamp': datetime.now().isoformat()
        }
