"""
Command Line Interface for Social Content Creator
"""
import asyncio
import argparse
import sys
from typing import Optional

from .orchestrator import SocialContentCreator
from .models import Platform


async def run_full_cycle(
    niches: Optional[str] = None,
    videos: int = 5,
    images: int = 10
):
    """Run full content creation cycle"""
    
    creator = SocialContentCreator()
    
    target_niches = None
    if niches:
        target_niches = [n.strip() for n in niches.split(',')]
    
    cycle = await creator.execute_full_cycle(
        target_niches=target_niches,
        video_count=videos,
        image_count=images
    )
    
    print("\n" + "="*60)
    print("📊 CYCLE SUMMARY")
    print("="*60)
    print(f"Cycle ID: {cycle.cycle_id}")
    print(f"\n📈 Trends Analyzed: {len(cycle.trend_report)}")
    print(f"🎯 Niches Recommended: {len(cycle.niche_recommendations)}")
    
    if cycle.niche_recommendations:
        print("\nTop Niches:")
        for i, niche in enumerate(cycle.niche_recommendations[:3], 1):
            print(f"  {i}. {niche.niche_name} (Potential: {niche.potential_score:.1f}/100)")
    
    print(f"\n🎥 Videos Created: {len(cycle.video_assets)}")
    print(f"📸 Images Created: {len(cycle.image_assets)}")
    print(f"✍️  Copy for {len(cycle.copywriting)} platforms")
    
    print("\n" + "="*60)


async def run_quick_analysis():
    """Run quick trend analysis"""
    
    creator = SocialContentCreator()
    results = await creator.quick_analysis()
    
    print("\n" + "="*60)
    print("🔍 QUICK TREND ANALYSIS")
    print("="*60)
    
    print(f"\n📊 Top Trends ({len(results['trends'])} total):")
    for i, trend in enumerate(results['trends'][:5], 1):
        print(f"  {i}. [{trend.platform.value.upper()}] {trend.name}")
        print(f"     Engagement: {trend.engagement_score:.1f}/100 | Growth: +{trend.growth_rate*100:.1f}%")
    
    print(f"\n🎯 Recommended Niches ({len(results['recommended_niches'])} total):")
    for i, niche in enumerate(results['recommended_niches'], 1):
        print(f"  {i}. {niche.niche_name}")
        print(f"     Potential: {niche.potential_score:.1f}/100")
        print(f"     Monetization: {', '.join(niche.monetization_opportunities[:3])}")
    
    print("\n" + "="*60)


def main():
    """Main CLI entry point"""
    
    parser = argparse.ArgumentParser(
        description='Social Content Creator - AI-Powered Social Media Content Generation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run full content creation cycle
  python -m social_content_creator --full-cycle
  
  # Run with specific niches
  python -m social_content_creator --full-cycle --niches "fitness,cooking,tech"
  
  # Run quick trend analysis only
  python -m social_content_creator --quick-analysis
  
  # Customize content generation
  python -m social_content_creator --full-cycle --videos 10 --images 20
        """
    )
    
    parser.add_argument(
        '--full-cycle',
        action='store_true',
        help='Execute full content creation cycle'
    )
    
    parser.add_argument(
        '--quick-analysis',
        action='store_true',
        help='Run quick trend analysis without content generation'
    )
    
    parser.add_argument(
        '--niches',
        type=str,
        help='Comma-separated list of target niches (e.g., "fitness,cooking,tech")'
    )
    
    parser.add_argument(
        '--videos',
        type=int,
        default=5,
        help='Number of videos to generate (default: 5)'
    )
    
    parser.add_argument(
        '--images',
        type=int,
        default=10,
        help='Number of images to generate (default: 10)'
    )
    
    args = parser.parse_args()
    
    # Show help if no action specified
    if not (args.full_cycle or args.quick_analysis):
        parser.print_help()
        sys.exit(0)
    
    try:
        if args.full_cycle:
            asyncio.run(run_full_cycle(
                niches=args.niches,
                videos=args.videos,
                images=args.images
            ))
        elif args.quick_analysis:
            asyncio.run(run_quick_analysis())
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
