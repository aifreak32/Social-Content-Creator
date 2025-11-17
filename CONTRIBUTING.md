# Contributing to Social Content Creator

Thank you for your interest in contributing to the Social Content Creator project! This document provides guidelines for contributions.

## 🤝 How to Contribute

### Reporting Bugs

If you find a bug, please open an issue with:
- Clear description of the bug
- Steps to reproduce
- Expected vs actual behavior
- Environment details (OS, Python version, etc.)

### Suggesting Enhancements

We welcome feature suggestions! Please open an issue with:
- Clear description of the proposed feature
- Use cases and benefits
- Potential implementation approach (if applicable)

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make your changes**
   - Follow the coding standards below
   - Add tests if applicable
   - Update documentation

4. **Test your changes**
   ```bash
   python -m pytest tests/
   python examples.py
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Open a Pull Request**

## 📝 Coding Standards

### Python Style
- Follow PEP 8 guidelines
- Use type hints where applicable
- Write docstrings for all public functions/classes
- Keep functions focused and under 50 lines when possible

### Code Structure
```python
def function_name(param: Type) -> ReturnType:
    """
    Brief description of what the function does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    # Implementation
    pass
```

### Naming Conventions
- Classes: `PascalCase`
- Functions/Methods: `snake_case`
- Constants: `UPPER_CASE`
- Private methods: `_leading_underscore`

### Imports
```python
# Standard library
import os
from typing import Dict, List

# Third-party
import pandas as pd
import numpy as np

# Local
from src.config import Config
from src.modules import TrendAnalyzer
```

## 🧪 Testing

### Running Tests
```bash
# Run all tests
python -m pytest

# Run specific test file
python -m pytest tests/test_trend_analyzer.py

# Run with coverage
python -m pytest --cov=src tests/
```

### Writing Tests
- Place tests in `tests/` directory
- Name test files `test_*.py`
- Use descriptive test names: `test_trend_analyzer_scores_high_volume_trends`
- Include edge cases and error conditions

Example:
```python
def test_trend_analyzer_returns_scored_trends():
    """Test that trend analyzer returns trends with scores."""
    analyzer = TrendAnalyzer(Config)
    trends = analyzer.analyze_trends()
    
    assert len(trends) > 0
    assert all('score' in trend for trend in trends)
    assert all(isinstance(trend['score'], float) for trend in trends)
```

## 📚 Documentation

### Code Documentation
- All public functions/classes must have docstrings
- Use Google-style docstrings
- Include examples in docstrings for complex functions

### README Updates
- Update README.md if adding new features
- Keep examples up to date
- Update configuration documentation

## 🔒 Security

- Never commit API keys or credentials
- Use environment variables for sensitive data
- Report security vulnerabilities privately to maintainers
- Follow secure coding practices

## 🌟 Areas for Contribution

We especially welcome contributions in:

### High Priority
- [ ] Real API integrations (Twitter, Instagram, etc.)
- [ ] Automated content publishing
- [ ] Advanced analytics dashboard
- [ ] A/B testing framework
- [ ] Multi-account management

### Medium Priority
- [ ] Additional content generation templates
- [ ] More social platform support
- [ ] Performance optimizations
- [ ] Enhanced error handling
- [ ] Internationalization (i18n)

### Nice to Have
- [ ] Web UI interface
- [ ] Mobile app companion
- [ ] Browser extension
- [ ] Slack/Discord integration
- [ ] Video generation automation

## 🎯 Development Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/aifreak32/Social-Content-Creator.git
   cd Social-Content-Creator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # If exists
   ```

4. **Setup environment**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

5. **Run tests**
   ```bash
   python -m pytest
   ```

## 📋 Commit Message Guidelines

Follow conventional commits format:

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(content): Add video script generation
fix(trend): Handle API rate limiting properly
docs(readme): Update installation instructions
```

## 🔄 Review Process

1. All PRs require at least one review
2. CI/CD checks must pass
3. Code coverage should not decrease
4. Documentation must be updated
5. Changes should include tests

## 💬 Getting Help

- **Issues**: Use GitHub issues for bugs and features
- **Discussions**: Use GitHub discussions for questions
- **Documentation**: Check README and code documentation

## 📄 License

By contributing, you agree that your contributions will be licensed under the MIT License.

## 🙏 Thank You!

Your contributions make this project better for everyone. We appreciate your time and effort!

---

**Questions?** Open an issue or start a discussion.
