#!/bin/bash
# Build script for Render deployment

echo "🚀 Starting build process for RK Ventures..."

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate --noinput

# Create a default superuser if it doesn't exist
echo "👤 Setting up admin user..."
python manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@rkventures.com', 'admin123')
    print("✅ Admin user created: admin/admin123")
else:
    print("✅ Admin user already exists")
EOF

echo "✅ Build completed successfully!"
