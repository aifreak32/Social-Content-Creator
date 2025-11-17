# Architecture Documentation

## System Overview

The Social Content Creator is a comprehensive AI-powered system designed to automate the entire social media content creation workflow. It operates through a modular architecture with clear separation of concerns.

## High-Level Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    CLI Interface                         │
│                  (cli.py, __main__.py)                   │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│                Main Orchestrator                         │
│                  (orchestrator.py)                       │
│         Coordinates 5-Phase Workflow                     │
└──┬────────┬────────┬────────┬────────┬─────────────────┘
   │        │        │        │        │
   ▼        ▼        ▼        ▼        ▼
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│Phase1│ │Phase2│ │Phase3│ │Phase4│ │Phase5│
└──────┘ └──────┘ └──────┘ └──────┘ └──────┘
```

## Module Structure

### 1. Trend Analysis (`trend_analysis/`)

**Purpose:** Monitor and analyze social media trends across platforms

**Components:**
- `base.py` - Abstract base class for platform analyzers
- `tiktok.py` - TikTok trend monitoring
- `instagram.py` - Instagram trend analysis
- `twitter.py` - Twitter/X trend tracking
- `youtube.py` - YouTube trend detection
- `aggregator.py` - Cross-platform pattern identification

**Key Features:**
- Real-time trend fetching (with API integration)
- Engagement score calculation
- Growth rate prediction
- Cross-platform pattern detection
- Viral trend prediction

**Data Flow:**
```
Platform APIs → Platform Analyzers → Aggregator → Trend Report
```

### 2. Research & Scouting (`research_scouting/`)

**Purpose:** Discover viral content and market opportunities

**Components:**
- `scanner.py` - Viral content identification
- `market_gap.py` - Market opportunity analysis

**Key Features:**
- Viral content scanning
- Engagement metrics analysis
- Market gap identification
- Niche saturation analysis
- Emerging niche detection

**Data Flow:**
```
Viral Content → Pattern Analysis → Gap Identification → Opportunities
```

### 3. Niche Strategy (`niche_strategy/`)

**Purpose:** Evaluate niche profitability and create monetization strategies

**Components:**
- `profitability.py` - Niche profitability analyzer

**Key Features:**
- Profitability scoring
- Competition analysis
- Saturation evaluation
- Target audience identification
- Monetization strategy planning
- Growth roadmap creation

**Data Flow:**
```
Niche Data → Analysis Engine → Profitability Score → Strategy
```

### 4. Content Creation (`content_creation/`)

**Purpose:** Generate AI-powered multimedia content

**Components:**
- `video_generator.py` - AI video creation
- `image_generator.py` - AI image generation
- `copywriter.py` - Viral copywriting

**Key Features:**
- Text-to-video generation
- Image/carousel creation
- Meme generation
- Hook creation
- Caption optimization
- Hashtag strategy
- Call-to-action generation

**Data Flow:**
```
Prompts → AI APIs → Content Assets → File Storage
```

### 5. Performance Analysis (`performance_analysis/`)

**Purpose:** Track, analyze, and optimize content performance

**Components:**
- `metrics.py` - Performance tracking
- `ab_testing.py` - A/B testing framework
- `optimizer.py` - Real-time optimization

**Key Features:**
- Metrics tracking (views, engagement, etc.)
- Viral score calculation
- A/B test management
- Performance optimization
- Strategy calibration
- Posting time optimization

**Data Flow:**
```
Content → Metrics → Analysis → Optimization → Recommendations
```

## Core Components

### Configuration (`config.py`)

Centralized configuration management:
- API credentials
- Application settings
- Output directory management
- Environment variable loading

### Models (`models.py`)

Pydantic data models for type safety:
- `Trend` - Trend data structure
- `ViralContent` - Viral content metadata
- `NicheAnalysis` - Niche evaluation results
- `ContentAsset` - Generated content
- `PerformanceMetrics` - Performance data
- `CreationCycle` - Complete cycle output

### Orchestrator (`orchestrator.py`)

Main workflow coordinator that executes the 5-phase process:

#### Phase 1: SCANNING
- Fetch trends from all platforms
- Identify cross-platform patterns
- Predict emerging trends

#### Phase 2: IDENTIFICATION
- Scan viral content
- Identify market gaps
- Analyze niche profitability

#### Phase 3: CREATION
- Generate videos
- Create images
- Write viral copy

#### Phase 4: PUBLISHING
- Optimize posting times
- Create publishing schedule
- Plan platform strategy

#### Phase 5: ANALYSIS
- Create growth strategy
- Plan monetization
- Set up performance tracking

## Data Models

### Trend Model
```python
{
  "id": "uuid",
  "platform": "tiktok|instagram|twitter|youtube",
  "type": "sound|hashtag|format|topic|content",
  "name": "trend name",
  "engagement_score": 0-100,
  "growth_rate": float,
  "timestamp": datetime,
  "metadata": {...}
}
```

### Content Asset Model
```python
{
  "id": "uuid",
  "type": "video|image|carousel",
  "platform": "tiktok|instagram|twitter|youtube",
  "file_path": "path/to/file",
  "caption": "text",
  "hashtags": ["tag1", "tag2"],
  "call_to_action": "text",
  "metadata": {...}
}
```

### Creation Cycle Model
```python
{
  "cycle_id": "uuid",
  "trend_report": [Trend],
  "niche_recommendations": [NicheAnalysis],
  "video_assets": [ContentAsset],
  "image_assets": [ContentAsset],
  "copywriting": {platform: text},
  "publishing_plan": {...},
  "growth_strategy": {...}
}
```

## API Integration Points

### Current State (Mock Implementation)
- All platform analyzers use mock data
- Content generators create placeholder files
- System fully functional without external APIs

### Production Integration
Replace mock implementations with:
- **TikTok:** TikTok API / Unofficial APIs
- **Instagram:** Instagram Graph API / instagrapi
- **Twitter:** Twitter API v2
- **YouTube:** YouTube Data API v3
- **AI Content:** OpenAI DALL-E, GPT-4, video generation APIs
- **Storage:** Cloud storage for generated assets

## Extensibility

### Adding New Platforms

1. Create platform analyzer in `trend_analysis/`:
```python
class NewPlatformAnalyzer(BaseTrendAnalyzer):
    def __init__(self):
        super().__init__(Platform.NEW_PLATFORM)
    
    async def fetch_trending_topics(self, limit=10):
        # Implementation
```

2. Add to aggregator
3. Update models if needed

### Adding New Content Types

1. Create generator in `content_creation/`:
```python
class NewContentGenerator:
    async def generate(self, prompt, platform):
        # Implementation
```

2. Update ContentType enum
3. Integrate in orchestrator

### Adding New Analysis Methods

1. Add analyzer in `performance_analysis/`:
```python
class NewAnalyzer:
    async def analyze(self, data):
        # Implementation
```

2. Integrate in optimizer

## Error Handling

- Graceful degradation on API failures
- Exception catching at module boundaries
- Fallback to mock data when APIs unavailable
- Comprehensive logging throughout

## Performance Considerations

- Async/await for concurrent operations
- Parallel platform trend fetching
- Efficient data structures (Pydantic models)
- File-based caching for generated content
- Batch processing for content generation

## Security Considerations

- API keys stored in environment variables
- No secrets in code
- Input validation via Pydantic
- Safe file operations
- No security vulnerabilities detected by CodeQL

## Testing Strategy

### Current Testing
- Manual CLI testing
- Example script validation
- Syntax verification
- Security scanning (CodeQL)

### Recommended Additional Testing
- Unit tests for each module
- Integration tests for workflows
- API integration tests
- Performance benchmarks
- Content quality evaluation

## Deployment Options

### Local Development
```bash
pip install -e .
python -m social_content_creator
```

### Production Deployment
- Docker containerization
- Cloud deployment (AWS, GCP, Azure)
- CI/CD pipeline integration
- Scheduled execution (cron, Cloud Functions)
- API service wrapper

## Future Enhancements

1. **Real API Integration**
   - Live social media data fetching
   - Actual AI content generation

2. **Database Integration**
   - PostgreSQL for metrics storage
   - Redis for caching
   - MongoDB for content metadata

3. **Web Interface**
   - Dashboard for visualization
   - Content preview and editing
   - Scheduling interface

4. **Advanced Analytics**
   - ML-based trend prediction
   - Sentiment analysis
   - Competitor tracking

5. **Automation**
   - Auto-posting to platforms
   - Automated A/B testing
   - Self-optimizing strategies

## Contributing

When contributing, maintain:
- Modular architecture
- Type hints and Pydantic models
- Async/await patterns
- Comprehensive docstrings
- Separation of concerns

---

This architecture supports scalability, maintainability, and extensibility while keeping the codebase clean and well-organized.
