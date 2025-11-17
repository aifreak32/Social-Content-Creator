#!/usr/bin/env python3
"""
Command Line Interface for Social Content Creator Agent
"""

import argparse
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src.agent import AutonomousAgent
from src.config import Config
import json


def main():
    parser = argparse.ArgumentParser(
        description="Autonomous Social Content Creator AI Agent",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run a single autonomous cycle
  python cli.py run --once
  
  # Run continuously for 5 cycles
  python cli.py run --cycles 5
  
  # Run indefinitely
  python cli.py run
  
  # Check agent status
  python cli.py status
  
  # View generated content
  python cli.py content --min-score 80
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Run command
    run_parser = subparsers.add_parser('run', help='Run the autonomous agent')
    run_parser.add_argument('--once', action='store_true', help='Run only one cycle')
    run_parser.add_argument('--cycles', type=int, help='Maximum number of cycles to run')
    
    # Status command
    subparsers.add_parser('status', help='Show agent status')
    
    # Content command
    content_parser = subparsers.add_parser('content', help='View generated content')
    content_parser.add_argument('--min-score', type=float, default=0, 
                               help='Minimum viral score filter')
    content_parser.add_argument('--type', choices=['text', 'image', 'video', 'all'],
                               default='all', help='Content type filter')
    
    # Config command
    subparsers.add_parser('config', help='Show current configuration')
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        return
    
    # Initialize agent
    agent = AutonomousAgent()
    
    if args.command == 'run':
        print("\n🚀 Starting Autonomous Agent...\n")
        
        if args.once:
            print("Mode: Single Cycle\n")
            results = agent.run_single_cycle()
            print(f"\n✅ Cycle completed! Check results/ directory for details.")
        else:
            max_cycles = args.cycles
            print(f"Mode: Continuous ({max_cycles if max_cycles else 'unlimited'} cycles)\n")
            agent.run_continuous(max_cycles=max_cycles)
    
    elif args.command == 'status':
        status = agent.get_status()
        print("\n📊 Agent Status")
        print("=" * 50)
        print(json.dumps(status, indent=2))
        print()
    
    elif args.command == 'content':
        content = agent.get_generated_content(min_score=args.min_score)
        
        if args.type != 'all':
            content = [c for c in content if c.get('type') == args.type]
        
        print(f"\n📝 Generated Content ({len(content)} items)")
        print("=" * 50)
        
        for i, item in enumerate(content[:10], 1):
            print(f"\n{i}. {item.get('type', 'unknown').upper()} - Score: {item.get('viral_score', 0)}")
            print(f"   Niche: {item.get('niche', 'N/A')}")
            
            if item.get('type') == 'text':
                print(f"   Preview: {item.get('hook', 'N/A')[:80]}...")
            elif item.get('type') == 'image':
                print(f"   Prompt: {item.get('image_prompt', 'N/A')[:80]}...")
            
        if len(content) > 10:
            print(f"\n... and {len(content) - 10} more items")
        
        print()
    
    elif args.command == 'config':
        print("\n⚙️  Current Configuration")
        print("=" * 50)
        print(f"Trend Analysis Interval: {Config.TREND_ANALYSIS_INTERVAL_MINUTES} minutes")
        print(f"Content Generation Interval: {Config.CONTENT_GENERATION_INTERVAL_HOURS} hours")
        print(f"Max Posts Per Day: {Config.MAX_POSTS_PER_DAY}")
        print(f"Min Engagement Score: {Config.MIN_ENGAGEMENT_SCORE}")
        print(f"Video Generation: {'Enabled' if Config.VIDEO_GENERATION_ENABLED else 'Disabled'}")
        print(f"Image Generation: {'Enabled' if Config.IMAGE_GENERATION_ENABLED else 'Disabled'}")
        print(f"\nMonetization Settings:")
        print(f"Min Followers: {Config.MIN_FOLLOWERS_FOR_MONETIZATION:,}")
        print(f"Target Engagement Rate: {Config.TARGET_ENGAGEMENT_RATE:.1%}")
        print()


if __name__ == "__main__":
    main()
