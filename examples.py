"""
Example Usage of Social Content Creator Agent
Demonstrates different ways to use the autonomous agent
"""

from src.agent import AutonomousAgent
from src.config import Config
import json


def example_single_cycle():
    """Example: Run a single autonomous cycle"""
    print("=" * 60)
    print("EXAMPLE 1: Single Cycle Execution")
    print("=" * 60)
    
    # Initialize agent
    agent = AutonomousAgent()
    
    # Run one cycle
    results = agent.run_single_cycle()
    
    # Display results
    print("\nCycle Results:")
    print(f"- Trends analyzed: {results['steps']['trend_analysis']['total_trends']}")
    print(f"- Niches identified: {results['steps']['niche_identification']['total_niches']}")
    print(f"- Content generated: {results['steps']['content_generation']['total_generated']}")
    
    return agent


def example_view_generated_content(agent):
    """Example: View generated content"""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: View Generated Content")
    print("=" * 60)
    
    # Get all content
    all_content = agent.get_generated_content()
    print(f"\nTotal content generated: {len(all_content)}")
    
    # Get high-scoring content only
    viral_content = agent.get_generated_content(min_score=80)
    print(f"High-scoring content (>80): {len(viral_content)}")
    
    # Display a sample
    if viral_content:
        sample = viral_content[0]
        print(f"\nSample High-Scoring Content:")
        print(f"Type: {sample.get('type')}")
        print(f"Niche: {sample.get('niche')}")
        print(f"Viral Score: {sample.get('viral_score')}")
        
        if sample.get('type') == 'text':
            print(f"\nHook: {sample.get('hook')}")
            print(f"Hashtags: {' '.join(sample.get('hashtags', [])[:5])}")


def example_niche_strategy():
    """Example: Get strategy for a specific niche"""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: Niche Content Strategy")
    print("=" * 60)
    
    from src.modules.niche_identifier import NicheIdentifier
    from src.modules.trend_analyzer import TrendAnalyzer
    
    # Analyze trends
    trend_analyzer = TrendAnalyzer(Config)
    trends = trend_analyzer.analyze_trends()
    
    # Identify niches
    niche_identifier = NicheIdentifier(Config)
    niches = niche_identifier.identify_niches(trends)
    
    if niches:
        top_niche = niches[0]
        print(f"\nTop Niche: {top_niche['niche']}")
        print(f"Profitability Score: {top_niche['profitability_score']}")
        
        # Get content strategy
        strategy = niche_identifier.get_niche_content_strategy(top_niche)
        
        print(f"\nTarget Audience: {strategy['target_audience']}")
        print(f"Content Types: {', '.join(strategy['content_types'])}")
        print(f"Posting Frequency: {strategy['posting_frequency']}")
        print(f"Best Platforms: {', '.join(strategy['best_platforms'])}")
        print(f"Keywords: {', '.join(strategy['keywords'][:5])}")


def example_performance_analysis():
    """Example: Analyze performance and get recommendations"""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: Performance Analysis")
    print("=" * 60)
    
    from src.modules.strategy_optimizer import StrategyOptimizer
    from src.modules.content_generator import ContentGenerator
    from src.modules.niche_identifier import NicheIdentifier
    from src.modules.trend_analyzer import TrendAnalyzer
    
    # Create some sample content
    trend_analyzer = TrendAnalyzer(Config)
    trends = trend_analyzer.analyze_trends()
    
    niche_identifier = NicheIdentifier(Config)
    niches = niche_identifier.identify_niches(trends)
    
    content_generator = ContentGenerator(Config)
    posts = []
    
    for niche in niches[:2]:
        post = content_generator.generate_content(niche, trends[:3], "text")
        posts.append(post)
    
    # Analyze performance
    optimizer = StrategyOptimizer(Config)
    analysis = optimizer.analyze_performance(posts)
    
    print("\nPerformance Metrics:")
    metrics = analysis['metrics']
    print(f"- Average Engagement Rate: {metrics['average_engagement_rate']:.2%}")
    print(f"- Average Viral Score: {metrics['average_viral_score']:.2f}")
    print(f"- Consistency Score: {metrics['consistency_score']:.2f}")
    
    print("\nRecommendations:")
    for i, rec in enumerate(analysis['recommendations'][:3], 1):
        print(f"{i}. {rec}")
    
    # Get optimized schedule
    if niches:
        schedule = optimizer.optimize_posting_schedule(niches[0], analysis)
        print(f"\nOptimized Posting Schedule:")
        print(f"- Posts per day: {schedule['posts_per_day']}")
        print(f"- Best hours: {', '.join(schedule['best_hours'])}")
        print(f"- Best days: {', '.join(schedule['best_days'])}")


def example_continuous_operation():
    """Example: Run continuously (commented out for safety)"""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: Continuous Operation")
    print("=" * 60)
    
    print("\nTo run the agent continuously:")
    print("```python")
    print("agent = AutonomousAgent()")
    print("agent.run_continuous(max_cycles=10)  # Run for 10 cycles")
    print("# or")
    print("agent.run_continuous()  # Run indefinitely")
    print("```")
    print("\nNote: Press Ctrl+C to stop gracefully")


def main():
    """Run all examples"""
    print("""
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║         SOCIAL CONTENT CREATOR - EXAMPLES                ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Example 1: Single cycle
    agent = example_single_cycle()
    
    # Example 2: View content
    example_view_generated_content(agent)
    
    # Example 3: Niche strategy
    example_niche_strategy()
    
    # Example 4: Performance analysis
    example_performance_analysis()
    
    # Example 5: Continuous operation (informational)
    example_continuous_operation()
    
    print("\n" + "=" * 60)
    print("Examples completed! Check logs/ and results/ directories")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
