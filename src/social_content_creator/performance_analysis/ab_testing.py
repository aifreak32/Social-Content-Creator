"""
A/B Testing Framework
"""
from typing import List, Dict, Any, Optional
from datetime import datetime
import uuid

from ..models import ContentAsset, PerformanceMetrics


class ABTestManager:
    """Manage A/B testing for content optimization"""
    
    def __init__(self):
        self.active_tests = {}
        self.completed_tests = {}
    
    def create_test(
        self,
        test_name: str,
        variants: List[ContentAsset],
        test_duration_hours: int = 24,
        success_metric: str = 'engagement_rate'
    ) -> str:
        """Create new A/B test"""
        test_id = str(uuid.uuid4())
        
        test = {
            'test_id': test_id,
            'test_name': test_name,
            'variants': variants,
            'variant_performance': {v.id: None for v in variants},
            'start_time': datetime.now(),
            'duration_hours': test_duration_hours,
            'success_metric': success_metric,
            'status': 'active',
            'winner': None
        }
        
        self.active_tests[test_id] = test
        return test_id
    
    async def update_test_metrics(
        self,
        test_id: str,
        variant_id: str,
        metrics: PerformanceMetrics
    ):
        """Update metrics for a test variant"""
        if test_id in self.active_tests:
            test = self.active_tests[test_id]
            test['variant_performance'][variant_id] = metrics
    
    async def analyze_test_results(
        self,
        test_id: str
    ) -> Dict[str, Any]:
        """Analyze A/B test results"""
        if test_id not in self.active_tests:
            return {'error': 'Test not found'}
        
        test = self.active_tests[test_id]
        success_metric = test['success_metric']
        
        results = {
            'test_id': test_id,
            'test_name': test['test_name'],
            'variants': [],
            'winner': None,
            'improvement': 0,
            'confidence': 0
        }
        
        best_score = 0
        winner_variant = None
        
        for variant in test['variants']:
            metrics = test['variant_performance'].get(variant.id)
            if metrics:
                score = getattr(metrics, success_metric, 0)
                
                variant_result = {
                    'variant_id': variant.id,
                    'caption': variant.caption[:50],
                    'metrics': metrics,
                    'score': score
                }
                results['variants'].append(variant_result)
                
                if score > best_score:
                    best_score = score
                    winner_variant = variant.id
        
        if winner_variant and results['variants']:
            results['winner'] = winner_variant
            
            # Calculate improvement over baseline (first variant)
            baseline_score = results['variants'][0]['score']
            if baseline_score > 0:
                results['improvement'] = ((best_score - baseline_score) / baseline_score) * 100
            
            # Mock confidence calculation
            results['confidence'] = 0.85  # 85% confidence
        
        return results
    
    async def complete_test(self, test_id: str) -> Dict[str, Any]:
        """Mark test as complete and determine winner"""
        results = await self.analyze_test_results(test_id)
        
        if test_id in self.active_tests:
            test = self.active_tests[test_id]
            test['status'] = 'completed'
            test['winner'] = results['winner']
            test['completion_time'] = datetime.now()
            
            # Move to completed tests
            self.completed_tests[test_id] = test
            del self.active_tests[test_id]
        
        return results
    
    def get_test_recommendations(
        self,
        test_results: Dict[str, Any]
    ) -> List[str]:
        """Generate recommendations based on test results"""
        recommendations = []
        
        if test_results.get('winner'):
            winner_id = test_results['winner']
            winner_data = next(
                (v for v in test_results['variants'] if v['variant_id'] == winner_id),
                None
            )
            
            if winner_data:
                recommendations.append(
                    f"Use variant '{winner_data['caption'][:30]}...' - performed {test_results['improvement']:.1f}% better"
                )
                
                # Analyze what made it better
                if winner_data.get('metrics'):
                    metrics = winner_data['metrics']
                    if metrics.engagement_rate > 0.08:
                        recommendations.append("High engagement rate - replicate this content style")
                    if metrics.shares > 500:
                        recommendations.append("High shareability - content is highly viral")
        
        return recommendations
    
    async def suggest_test_variants(
        self,
        original_content: ContentAsset,
        test_dimension: str = 'caption'
    ) -> List[ContentAsset]:
        """Suggest variants to test"""
        # TODO: Use AI to generate test variants
        
        variants = [original_content]  # Include original
        
        # Mock variant generation
        if test_dimension == 'caption':
            # Generate caption variants
            pass
        elif test_dimension == 'hashtags':
            # Generate hashtag variants
            pass
        elif test_dimension == 'hook':
            # Generate hook variants
            pass
        
        return variants
