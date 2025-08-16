#!/usr/bin/env python3
"""
Deployment Helper Script for RK Ventures
This script helps prepare your Django project for deployment
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return None

def main():
    print("🚀 RK Ventures Deployment Helper")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists('manage.py'):
        print("❌ Error: Please run this script from your Django project root directory")
        sys.exit(1)
    
    print("📋 Preparing your project for deployment...")
    
    # Install production dependencies
    print("\n📦 Installing production dependencies...")
    run_command("pip install -r requirements.txt", "Installing requirements")
    
    # Collect static files
    print("\n📁 Collecting static files...")
    run_command("python manage.py collectstatic --noinput", "Collecting static files")
    
    # Check if .env file exists
    if not os.path.exists('.env'):
        print("\n🔐 Creating .env file for environment variables...")
        env_content = """# Production Environment Variables
DEBUG=False
SECRET_KEY=your-secret-key-here
SITE_DOMAIN=https://your-app-name.railway.app
DATABASE_URL=your-database-url-here
"""
        with open('.env', 'w') as f:
            f.write(env_content)
        print("✅ .env file created")
        print("⚠️  Remember to update the values in .env file!")
    
    print("\n🎉 Deployment preparation completed!")
    print("\n📝 Next steps:")
    print("1. Push your code to GitHub")
    print("2. Go to Railway.app or Render.com")
    print("3. Connect your repository")
    print("4. Deploy!")
    print("\n🌐 Your website will be accessible worldwide!")

if __name__ == "__main__":
    main()
