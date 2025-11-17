# Quick Start Guide

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/aifreak32/Social-Content-Creator.git
cd Social-Content-Creator
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
# Or install in development mode:
pip install -e .
```

3. **Configure API keys:**
```bash
cp .env.example .env
# Edit .env and add your API keys
```

## Basic Usage

### Option 1: Quick Trend Analysis (No API Keys Required)

Get instant insights into current social media trends:

```bash
python -m social_content_creator --quick-analysis
```

**Output:**
- Top trends across all platforms
- Cross-platform viral patterns
- Recommended niches with profitability scores
- Market opportunities

### Option 2: Full Content Creation Cycle

Generate complete content packages:

```bash
# Basic usage
python -m social_content_creator --full-cycle

# With specific niches
python -m social_content_creator --full-cycle --niches "fitness,cooking"

# Custom content count
python -m social_content_creator --full-cycle --videos 10 --images 20
```

**Output:**
- Trend analysis report
- Niche recommendations
- 3-5 ready-to-post videos
- 5-10 graphic assets
- Optimized captions and hashtags
- Publishing schedule
- Growth strategy

### Option 3: Programmatic Usage

Use the system in your own Python code:

```python
import asyncio
from social_content_creator import SocialContentCreator

async def main():
    creator = SocialContentCreator()
    
    # Quick analysis
    analysis = await creator.quick_analysis()
    print(f"Found {len(analysis['trends'])} trends")
    
    # Full cycle
    cycle = await creator.execute_full_cycle(
        target_niches=['tech', 'fitness'],
        video_count=5,
        image_count=10
    )
    print(f"Created {len(cycle.video_assets)} videos")

asyncio.run(main())
```

## Understanding the Output

All generated content is saved in the `output/` directory:

```
output/
├── videos/          # Generated video files (.mp4)
├── images/          # Generated images and carousels (.png)
└── reports/         # JSON reports with complete analysis
```

### Sample Report Structure

```json
{
  "cycle_id": "abc-123",
  "summary": {
    "trends_analyzed": 20,
    "niches_recommended": 3,
    "videos_created": 5,
    "images_created": 10
  },
  "trend_report": [...],
  "niche_recommendations": [...],
  "publishing_plan": {...},
  "growth_strategy": {...}
}
```

## Configuration

### Environment Variables

Essential configurations in `.env`:

```env
# AI Services (Optional - uses mock data if not provided)
OPENAI_API_KEY=sk-...
ANTHROPIC_API_KEY=sk-...

# Social Media APIs (Optional)
TIKTOK_SESSION_ID=...
INSTAGRAM_USERNAME=...
INSTAGRAM_PASSWORD=...
TWITTER_API_KEY=...
YOUTUBE_API_KEY=...

# App Settings
LOG_LEVEL=INFO
OUTPUT_DIR=./output
LANGUAGE=ITA
```

## Workflow Phases

The system executes 5 phases automatically:

1. **SCANNING** - Analyzes trends across TikTok, Instagram, Twitter/X, YouTube
2. **IDENTIFICATION** - Identifies profitable niches and market gaps
3. **CREATION** - Generates videos, images, and viral copy
4. **PUBLISHING** - Creates optimized posting schedule
5. **ANALYSIS** - Develops growth and monetization strategy

## Tips for Best Results

### 1. Choose Your Niches Wisely
- Use `--quick-analysis` first to discover trending niches
- Combine broad and specific niches (e.g., "fitness, yoga")
- Focus on 2-3 niches for best results

### 2. Optimize Content Generation
- Start with fewer assets (3 videos, 5 images) to test
- Increase counts once you validate the output quality
- Review generated content and iterate

### 3. Leverage the Reports
- Check `output/reports/` for detailed insights
- Use trend data to inform content strategy
- Follow the growth strategy recommendations

### 4. API Integration
- System works without API keys (uses mock data)
- Add real API keys for production use
- Start with free tiers to test integration

## Common Use Cases

### For Content Creators
```bash
# Generate a week's worth of content
python -m social_content_creator --full-cycle --videos 14 --images 28 --niches "your-niche"
```

### For Social Media Managers
```bash
# Quick competitive analysis
python -m social_content_creator --quick-analysis

# Generate client content
python -m social_content_creator --full-cycle --niches "client-industry"
```

### For Influencers
```bash
# Stay on top of trends
python -m social_content_creator --quick-analysis

# Generate viral content ideas
python -m social_content_creator --full-cycle --videos 5
```

## Troubleshooting

### Issue: Command not found
**Solution:** Make sure you're in the project directory and have installed dependencies:
```bash
cd Social-Content-Creator
pip install -e .
```

### Issue: Import errors
**Solution:** Install all required dependencies:
```bash
pip install -r requirements.txt
```

### Issue: API errors
**Solution:** The system works without API keys using mock data. Add real keys in `.env` for production.

## Next Steps

1. Run a quick analysis to explore the system
2. Generate a small content batch (3 videos, 5 images)
3. Review the output in `output/` directory
4. Integrate with your workflow
5. Scale up content generation

## Support

- Check the main README.md for detailed documentation
- Review example.py for code examples
- Explore the `src/` directory for module documentation

---

Happy content creating! 🚀
