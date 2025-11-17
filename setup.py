#!/usr/bin/env python3
"""
Setup script for Social Content Creator
"""

import os
import sys
from pathlib import Path


def create_directories():
    """Create necessary directories"""
    directories = [
        'generated_content',
        'generated_content/images',
        'generated_content/videos',
        'logs',
        'results',
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ Created directory: {directory}")


def check_env_file():
    """Check if .env file exists, if not copy from .env.example"""
    env_file = Path('.env')
    env_example = Path('.env.example')
    
    if not env_file.exists():
        if env_example.exists():
            import shutil
            shutil.copy(env_example, env_file)
            print("✓ Created .env file from .env.example")
            print("⚠️  Please edit .env file with your API keys and configuration")
            return False
        else:
            print("❌ .env.example not found")
            return False
    else:
        print("✓ .env file exists")
        return True


def check_dependencies():
    """Check if required packages are installed"""
    required_packages = [
        'python-dotenv',
        'requests',
        'pandas',
        'numpy',
    ]
    
    missing = []
    for package in required_packages:
        try:
            __import__(package.replace('-', '_'))
            print(f"✓ {package} is installed")
        except ImportError:
            missing.append(package)
            print(f"❌ {package} is NOT installed")
    
    if missing:
        print(f"\n⚠️  Missing packages: {', '.join(missing)}")
        print("Run: pip install -r requirements.txt")
        return False
    
    return True


def main():
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║     🤖 SOCIAL CONTENT CREATOR - SETUP WIZARD 🤖          ║
    ║                                                           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    print("\n📁 Creating directories...")
    create_directories()
    
    print("\n🔧 Checking environment configuration...")
    env_ok = check_env_file()
    
    print("\n📦 Checking dependencies...")
    deps_ok = check_dependencies()
    
    print("\n" + "=" * 60)
    
    if env_ok and deps_ok:
        print("✅ Setup complete! You're ready to run the agent.")
        print("\nNext steps:")
        print("  1. Edit .env file with your API keys (if needed)")
        print("  2. Run: python cli.py run --once")
        print("  3. Check the results/ directory for output")
    else:
        print("⚠️  Setup incomplete. Please fix the issues above.")
        
        if not deps_ok:
            print("\n➡️  Run: pip install -r requirements.txt")
        
        if not env_ok:
            print("➡️  Edit .env file with your API keys")
    
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
