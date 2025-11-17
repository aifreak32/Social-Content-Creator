"""
Autonomous Agent
Main orchestrator for the Social Content Creator AI agent
Coordinates all modules and runs autonomously
"""

import logging
import time
from datetime import datetime
from typing import Dict, Any, List
import json
from pathlib import Path

from src.config import Config
from src.modules.trend_analyzer import TrendAnalyzer
from src.modules.niche_identifier import NicheIdentifier
from src.modules.content_generator import ContentGenerator
from src.modules.strategy_optimizer import StrategyOptimizer

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOGS_DIR / 'agent.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)


class AutonomousAgent:
    """
    Main autonomous AI agent for social media content creation
    Operates fully automatically with data-driven decisions
    """
    
    def __init__(self):
        """Initialize the autonomous agent"""
        logger.info("Initializing Autonomous Social Content Creator Agent...")
        
        # Validate configuration
        config_errors = Config.validate()
        if config_errors:
            logger.warning(f"Configuration warnings: {config_errors}")
        
        # Initialize modules
        self.trend_analyzer = TrendAnalyzer(Config)
        self.niche_identifier = NicheIdentifier(Config)
        self.content_generator = ContentGenerator(Config)
        self.strategy_optimizer = StrategyOptimizer(Config)
        
        # Agent state
        self.is_running = False
        self.cycle_count = 0
        self.generated_posts = []
        
        logger.info("Agent initialized successfully!")
    
    def run_autonomous_cycle(self) -> Dict[str, Any]:
        """
        Execute one complete autonomous cycle:
        1. Analyze trends
        2. Identify niches
        3. Generate content
        4. Optimize strategy
        5. Schedule posts
        """
        logger.info(f"\n{'='*60}")
        logger.info(f"Starting Autonomous Cycle #{self.cycle_count + 1}")
        logger.info(f"{'='*60}\n")
        
        cycle_results = {
            "cycle_number": self.cycle_count + 1,
            "timestamp": datetime.now(),
            "steps": {}
        }
        
        try:
            # Step 1: Analyze trends
            logger.info("Step 1: Analyzing trends...")
            trends = self.trend_analyzer.analyze_trends()
            top_trends = self.trend_analyzer.get_top_trends(10)
            cycle_results["steps"]["trend_analysis"] = {
                "total_trends": len(trends),
                "top_trends": top_trends[:5]
            }
            logger.info(f"✓ Analyzed {len(trends)} trends")
            
            # Step 2: Identify profitable niches
            logger.info("\nStep 2: Identifying profitable niches...")
            niches = self.niche_identifier.identify_niches(trends)
            top_niches = self.niche_identifier.get_top_niches(3)
            cycle_results["steps"]["niche_identification"] = {
                "total_niches": len(niches),
                "top_niches": top_niches
            }
            logger.info(f"✓ Identified {len(niches)} profitable niches")
            
            # Step 3: Generate content for top niches
            logger.info("\nStep 3: Generating viral content...")
            generated_content = []
            
            for niche in top_niches:
                # Get niche strategy
                strategy = self.niche_identifier.get_niche_content_strategy(niche)
                
                # Generate different types of content
                content_types = ["text", "image"]
                if Config.VIDEO_GENERATION_ENABLED:
                    content_types.append("video")
                
                for content_type in content_types[:2]:  # Generate 2 types per niche
                    content = self.content_generator.generate_content(
                        niche,
                        top_trends[:5],
                        content_type
                    )
                    
                    if content.get("viral_score", 0) >= Config.MIN_ENGAGEMENT_SCORE:
                        generated_content.append(content)
                        self.generated_posts.append(content)
                        logger.info(
                            f"  ✓ Generated {content_type} content for {niche['niche']} "
                            f"(viral score: {content['viral_score']})"
                        )
            
            cycle_results["steps"]["content_generation"] = {
                "total_generated": len(generated_content),
                "high_score_content": len([c for c in generated_content 
                                          if c.get("viral_score", 0) >= 80])
            }
            logger.info(f"✓ Generated {len(generated_content)} pieces of content")
            
            # Step 4: Analyze performance and optimize strategy
            logger.info("\nStep 4: Optimizing strategy...")
            if self.generated_posts:
                performance_analysis = self.strategy_optimizer.analyze_performance(
                    self.generated_posts
                )
                
                # Generate optimized schedule
                if top_niches:
                    optimized_schedule = self.strategy_optimizer.optimize_posting_schedule(
                        top_niches[0],
                        performance_analysis
                    )
                    
                    # Check monetization readiness
                    monetization_status = self.strategy_optimizer.calculate_monetization_readiness(
                        performance_analysis.get("metrics", {})
                    )
                    
                    cycle_results["steps"]["strategy_optimization"] = {
                        "performance_metrics": performance_analysis.get("metrics"),
                        "recommendations": performance_analysis.get("recommendations"),
                        "optimized_schedule": optimized_schedule,
                        "monetization_status": monetization_status
                    }
                    
                    logger.info("✓ Strategy optimized")
                    logger.info(f"\nRecommendations:")
                    for rec in performance_analysis.get("recommendations", [])[:3]:
                        logger.info(f"  • {rec}")
            else:
                logger.info("⚠ Skipping optimization - no content generated yet")
            
            # Step 5: Save results
            self._save_cycle_results(cycle_results)
            
            self.cycle_count += 1
            logger.info(f"\n{'='*60}")
            logger.info(f"Cycle #{self.cycle_count} completed successfully!")
            logger.info(f"{'='*60}\n")
            
            return cycle_results
            
        except Exception as e:
            logger.error(f"Error in autonomous cycle: {e}", exc_info=True)
            cycle_results["error"] = str(e)
            return cycle_results
    
    def run_continuous(self, max_cycles: int = None):
        """
        Run the agent continuously in autonomous mode
        
        Args:
            max_cycles: Maximum number of cycles to run (None for infinite)
        """
        logger.info("Starting continuous autonomous operation...")
        logger.info(f"Max cycles: {max_cycles if max_cycles else 'Unlimited'}")
        
        self.is_running = True
        
        try:
            while self.is_running:
                # Run one cycle
                self.run_autonomous_cycle()
                
                # Check if we've reached max cycles
                if max_cycles and self.cycle_count >= max_cycles:
                    logger.info(f"Reached maximum cycles ({max_cycles}). Stopping...")
                    break
                
                # Wait before next cycle (configurable interval)
                wait_time = Config.CONTENT_GENERATION_INTERVAL_HOURS * 3600
                logger.info(f"Waiting {Config.CONTENT_GENERATION_INTERVAL_HOURS} hours before next cycle...")
                time.sleep(wait_time)
                
        except KeyboardInterrupt:
            logger.info("\nReceived interrupt signal. Shutting down gracefully...")
            self.is_running = False
        except Exception as e:
            logger.error(f"Fatal error in continuous operation: {e}", exc_info=True)
            self.is_running = False
    
    def run_single_cycle(self) -> Dict[str, Any]:
        """Run a single autonomous cycle and return results"""
        return self.run_autonomous_cycle()
    
    def _save_cycle_results(self, results: Dict[str, Any]):
        """Save cycle results to file"""
        try:
            results_dir = Config.BASE_DIR / "results"
            results_dir.mkdir(exist_ok=True)
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = results_dir / f"cycle_{results['cycle_number']}_{timestamp}.json"
            
            # Convert datetime objects to strings for JSON serialization
            serializable_results = self._make_serializable(results)
            
            with open(filename, 'w') as f:
                json.dump(serializable_results, f, indent=2)
            
            logger.info(f"✓ Results saved to {filename}")
            
        except Exception as e:
            logger.error(f"Error saving results: {e}")
    
    def _make_serializable(self, obj):
        """Convert objects to JSON serializable format"""
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, dict):
            return {k: self._make_serializable(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self._make_serializable(item) for item in obj]
        elif isinstance(obj, bool):
            return obj
        elif isinstance(obj, (int, float, str, type(None))):
            return obj
        else:
            return str(obj)
    
    def get_status(self) -> Dict[str, Any]:
        """Get current agent status"""
        return {
            "is_running": self.is_running,
            "cycle_count": self.cycle_count,
            "total_posts_generated": len(self.generated_posts),
            "high_score_posts": len([p for p in self.generated_posts 
                                    if p.get("viral_score", 0) >= 80]),
            "config": {
                "trend_analysis_interval": Config.TREND_ANALYSIS_INTERVAL_MINUTES,
                "content_generation_interval": Config.CONTENT_GENERATION_INTERVAL_HOURS,
                "max_posts_per_day": Config.MAX_POSTS_PER_DAY,
            }
        }
    
    def get_generated_content(self, min_score: float = None) -> List[Dict[str, Any]]:
        """Get all generated content, optionally filtered by minimum score"""
        if min_score:
            return [p for p in self.generated_posts if p.get("viral_score", 0) >= min_score]
        return self.generated_posts


def main():
    """Main entry point for the autonomous agent"""
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     🤖 AUTONOMOUS SOCIAL CONTENT CREATOR AGENT 🤖        ║
    ║                                                           ║
    ║  AI-Powered | Data-Driven | Fully Automatic              ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Initialize agent
    agent = AutonomousAgent()
    
    # Run single cycle for demonstration
    logger.info("Running demonstration cycle...")
    results = agent.run_single_cycle()
    
    # Display summary
    print("\n" + "="*60)
    print("CYCLE SUMMARY")
    print("="*60)
    
    if "error" not in results:
        steps = results.get("steps", {})
        
        print(f"\n✓ Trends Analyzed: {steps.get('trend_analysis', {}).get('total_trends', 0)}")
        print(f"✓ Niches Identified: {steps.get('niche_identification', {}).get('total_niches', 0)}")
        print(f"✓ Content Generated: {steps.get('content_generation', {}).get('total_generated', 0)}")
        print(f"✓ High Score Content: {steps.get('content_generation', {}).get('high_score_content', 0)}")
        
        if "strategy_optimization" in steps:
            opt = steps["strategy_optimization"]
            metrics = opt.get("performance_metrics", {})
            print(f"\n📊 Average Engagement: {metrics.get('average_engagement_rate', 0):.2%}")
            print(f"📊 Average Viral Score: {metrics.get('average_viral_score', 0):.2f}")
            
            monetization = opt.get("monetization_status", {})
            if monetization.get("ready_for_monetization"):
                print(f"\n💰 MONETIZATION READY! Score: {monetization.get('readiness_score', 0)}/100")
            else:
                print(f"\n📈 Monetization Progress: {monetization.get('readiness_score', 0)}/100")
    
    print("\n" + "="*60)
    print(f"Status: {'SUCCESS' if 'error' not in results else 'ERROR'}")
    print("="*60 + "\n")
    
    # Show agent status
    status = agent.get_status()
    print(f"Agent Status: {json.dumps(status, indent=2)}")
    
    print("\n💡 To run continuously, use: agent.run_continuous(max_cycles=10)")
    print("💡 Check the 'results' and 'logs' directories for detailed output\n")


if __name__ == "__main__":
    main()
