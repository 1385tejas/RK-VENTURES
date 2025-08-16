#!/bin/bash
# Build script for Railway deployment

echo "🚀 Starting build process..."

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

echo "✅ Build completed successfully!"
