"""
Example: Running a complete content creation cycle
"""
import asyncio
from src.social_content_creator.orchestrator import SocialContentCreator


async def main():
    """Example usage of Social Content Creator"""
    
    print("🚀 Social Content Creator - Example Usage\n")
    
    # Initialize the creator
    creator = SocialContentCreator()
    
    # Example 1: Quick trend analysis
    print("Example 1: Quick Trend Analysis")
    print("-" * 50)
    analysis = await creator.quick_analysis()
    
    print(f"Found {len(analysis['trends'])} trends")
    print(f"Recommended {len(analysis['recommended_niches'])} niches")
    
    if analysis['recommended_niches']:
        top_niche = analysis['recommended_niches'][0]
        print(f"\nTop recommended niche: {top_niche.niche_name}")
        print(f"Potential score: {top_niche.potential_score:.1f}/100")
        print(f"Monetization: {', '.join(top_niche.monetization_opportunities[:3])}")
    
    print("\n" + "=" * 50 + "\n")
    
    # Example 2: Full content creation cycle
    print("Example 2: Full Content Creation Cycle")
    print("-" * 50)
    
    cycle = await creator.execute_full_cycle(
        target_niches=['fitness', 'tech'],
        video_count=3,
        image_count=5
    )
    
    print("\n📊 Cycle Results:")
    print(f"  - Cycle ID: {cycle.cycle_id}")
    print(f"  - Trends analyzed: {len(cycle.trend_report)}")
    print(f"  - Niches evaluated: {len(cycle.niche_recommendations)}")
    print(f"  - Videos created: {len(cycle.video_assets)}")
    print(f"  - Images created: {len(cycle.image_assets)}")
    
    print("\n🎯 Top 3 Recommended Niches:")
    for i, niche in enumerate(cycle.niche_recommendations[:3], 1):
        print(f"  {i}. {niche.niche_name}")
        print(f"     - Potential: {niche.potential_score:.1f}/100")
        print(f"     - Competition: {niche.competition_level:.1f}/100")
        print(f"     - Platforms: {', '.join([p.value for p in niche.recommended_platforms])}")
    
    print("\n🎥 Video Assets:")
    for i, video in enumerate(cycle.video_assets[:3], 1):
        print(f"  {i}. Platform: {video.platform.value}")
        print(f"     Caption: {video.caption[:60]}...")
        print(f"     Hashtags: {', '.join(video.hashtags[:5])}")
    
    print("\n📸 Image Assets:")
    for i, image in enumerate(cycle.image_assets[:3], 1):
        print(f"  {i}. Type: {image.type.value}")
        print(f"     Platform: {image.platform.value}")
        print(f"     Caption: {image.caption[:60]}...")
    
    print("\n📅 Publishing Plan:")
    if cycle.publishing_plan.get('best_posting_times'):
        for platform, times in cycle.publishing_plan['best_posting_times'].items():
            print(f"  {platform}: {', '.join(times)}")
    
    print("\n📈 Growth Strategy:")
    if 'short_term' in cycle.growth_strategy:
        short_term = cycle.growth_strategy['short_term']
        print(f"  Short-term ({short_term['duration']}):")
        if 'goals' in short_term:
            print(f"    Goals: {', '.join(short_term['goals'][:2])}")
        if 'tactics' in short_term:
            print("    Tactics:")
            for tactic in short_term['tactics'][:3]:
                print(f"      - {tactic}")
    
    print("\n✅ Example completed successfully!")


if __name__ == '__main__':
    asyncio.run(main())
