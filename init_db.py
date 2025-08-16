#!/usr/bin/env python3
"""
Database initialization script for RK Ventures
This script ensures all database tables are created
"""

import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rkventures_site.settings')
django.setup()

from django.core.management import execute_from_command_line

def init_database():
    """Initialize the database with all required tables"""
    print("🚀 Initializing RK Ventures Database...")
    
    try:
        # Make migrations for all apps
        print("📝 Creating migrations...")
        execute_from_command_line(['manage.py', 'makemigrations', '--noinput'])
        
        # Apply migrations
        print("🗄️ Applying migrations...")
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        
        # Create superuser if it doesn't exist
        print("👤 Setting up admin user...")
        from django.contrib.auth.models import User
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@rkventures.com', 'admin123')
            print("✅ Admin user created: admin/admin123")
        else:
            print("✅ Admin user already exists")
        
        print("🎉 Database initialization completed successfully!")
        
    except Exception as e:
        print(f"❌ Error during database initialization: {e}")
        raise

if __name__ == "__main__":
    init_database()
