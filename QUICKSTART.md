# 🚀 Quick Start Guide

Get started with the Social Content Creator in 5 minutes!

## 📋 Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- API keys for AI services (OpenAI or Anthropic)

## ⚡ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/aifreak32/Social-Content-Creator.git
cd Social-Content-Creator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
nano .env  # or use your preferred editor
```

**Minimum required configuration:**
```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run Setup Wizard

```bash
python setup.py
```

This will:
- Create necessary directories
- Verify dependencies
- Check configuration

## 🎯 First Run

### Option 1: Run a Single Cycle

The quickest way to see the agent in action:

```bash
python -m src.agent
```

This will:
1. ✓ Analyze 9+ trending topics
2. ✓ Identify 3+ profitable niches
3. ✓ Generate 6+ pieces of content
4. ✓ Provide strategy recommendations
5. ✓ Calculate monetization readiness

**Output:** Check `results/` directory for detailed JSON output

### Option 2: Use the CLI

```bash
# Run a single cycle
python cli.py run --once

# View configuration
python cli.py config

# Check agent status
python cli.py status
```

## 📊 Understanding the Output

After running, you'll find:

### 1. Generated Content (`results/cycle_*.json`)
```json
{
  "cycle_number": 1,
  "steps": {
    "trend_analysis": {...},
    "niche_identification": {...},
    "content_generation": {...},
    "strategy_optimization": {...}
  }
}
```

### 2. Agent Logs (`logs/agent.log`)
Detailed operation logs for debugging and monitoring

### 3. Console Output
Summary showing:
- Trends analyzed
- Niches identified
- Content generated
- Performance metrics
- Recommendations

## 🎨 Example Generated Content

**Text Post:**
```
Hook: 🚀 The secret to success in Technology & AI that nobody talks about:

Body: Here's what changed everything:
1. Understanding the market trends
2. Leveraging AI and automation
3. Creating authentic, valuable content
...

CTA: 💬 What's your experience? Share in the comments!

Hashtags: #AI #Technology #ContentCreator #ViralContent
```

**Image Prompt:**
```
Create a futuristic, high-tech, clean design image representing 
Technology & AI, featuring elements related to AI, tech, software, 
optimized for social media, high quality, visually appealing
```

## 📚 Next Steps

### Learn More
```bash
# Run examples
python examples.py

# View all CLI commands
python cli.py --help

# Run tests
python -m pytest tests/
```

### Customize Configuration

Edit `.env` to adjust:
- Trend analysis frequency
- Content generation settings
- Posting schedules
- Monetization thresholds

### Run Continuously

```python
from src.agent import AutonomousAgent

agent = AutonomousAgent()

# Run for 5 cycles
agent.run_continuous(max_cycles=5)

# Or run indefinitely (Ctrl+C to stop)
agent.run_continuous()
```

## 🔧 Troubleshooting

### Missing Dependencies
```bash
pip install -r requirements.txt
```

### API Key Issues
- Ensure `.env` file exists in project root
- Check that API keys are valid
- At least one AI API key (OpenAI or Anthropic) required

### Permission Errors
```bash
chmod +x cli.py setup.py
```

## 💡 Tips

1. **Start Simple**: Run a single cycle first to understand the output
2. **Check Logs**: Look at `logs/agent.log` for detailed information
3. **Review Content**: Examine generated content in `results/` directory
4. **Iterate**: Adjust configuration based on results
5. **Test**: Run the examples to explore different features

## 🆘 Getting Help

- 📖 Read the full [README.md](README.md)
- 🐛 Report issues on [GitHub Issues](https://github.com/aifreak32/Social-Content-Creator/issues)
- 💬 Ask questions in [GitHub Discussions](https://github.com/aifreak32/Social-Content-Creator/discussions)

## ✅ Verify Installation

Run this command to verify everything is working:

```bash
python -c "from src.agent import AutonomousAgent; agent = AutonomousAgent(); print('✅ Installation successful!')"
```

If you see "✅ Installation successful!", you're ready to go!

---

**🎉 Congratulations!** You're now ready to create viral content with AI!

For more advanced usage, check out:
- [Full Documentation](README.md)
- [Examples](examples.py)
- [Contributing Guide](CONTRIBUTING.md)
