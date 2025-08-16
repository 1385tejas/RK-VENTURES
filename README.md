# RK Ventures - Property Auction Website

A comprehensive property auction platform built with Django, featuring user registration, property listings, auction management, and real-time notifications.

## Features

- **User Management**: Registration, login, and profile management
- **Property Listings**: Browse and search properties with detailed information
- **Auction Management**: Track auction dates and property details
- **Advanced Filtering**: Filter properties by location, price, and auction date
- **Sorting Options**: Sort by price, auction date (oldest/newest first), and more
- **Responsive Design**: Works on all devices (desktop, tablet, mobile)
- **Admin Panel**: Comprehensive admin interface for property and user management
- **Excel Export**: Export user registration data to Excel format

## Technology Stack

- **Backend**: Django 5.2.1
- **Database**: SQLite (development) / PostgreSQL (production)
- **Frontend**: HTML, CSS, JavaScript
- **Real-time**: Django Channels
- **Deployment**: Railway/Render ready

## Quick Start (Development)

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd rkventures
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the website**
   - Main site: http://127.0.0.1:8000
   - Admin panel: http://127.0.0.1:8000/admin

## Deployment to Railway (Recommended)

### Step 1: Prepare Your Project
Your project is already configured for deployment with the necessary files:
- `requirements.txt` - Dependencies
- `Procfile` - Railway deployment configuration
- `runtime.txt` - Python version
- Updated `settings.py` - Production-ready settings

### Step 2: Deploy to Railway

1. **Install Railway CLI** (optional but recommended)
   ```bash
   npm install -g @railway/cli
   ```

2. **Go to [Railway.app](https://railway.app)**
   - Sign up with your GitHub account
   - Click "New Project"
   - Select "Deploy from GitHub repo"

3. **Connect Your Repository**
   - Select your GitHub repository
   - Railway will automatically detect it's a Django app

4. **Configure Environment Variables**
   Add these in Railway dashboard:
   ```
   DEBUG=False
   SECRET_KEY=your-secret-key-here
   SITE_DOMAIN=https://your-app-name.railway.app
   ```

5. **Deploy**
   - Railway will automatically build and deploy your app
   - Wait for the build to complete

6. **Access Your Live Website**
   - Your website will be available at: `https://your-app-name.railway.app`
   - Share this link with users worldwide!

## Alternative Deployment: Render

1. **Go to [Render.com](https://render.com)**
2. **Create a new Web Service**
3. **Connect your GitHub repository**
4. **Configure build settings**:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn rkventures_site.wsgi:application`
5. **Deploy and get your live URL**

## Environment Variables

For production, set these environment variables:

```bash
DEBUG=False
SECRET_KEY=your-secure-secret-key
SITE_DOMAIN=https://your-domain.com
DATABASE_URL=your-database-connection-string
```

## Database Migration

After deployment, run migrations on the production database:

```bash
python manage.py migrate
python manage.py collectstatic
```

## Custom Domain (Optional)

1. **Buy a domain** (e.g., from GoDaddy, Namecheap)
2. **Configure DNS** to point to your Railway/Render URL
3. **Update SITE_DOMAIN** environment variable
4. **Add custom domain** in Railway/Render dashboard

## Features for Global Users

- **Responsive Design**: Works on all screen sizes
- **Mobile-First**: Optimized for mobile devices
- **Fast Loading**: Optimized static files and database queries
- **SEO Ready**: Clean URLs and meta tags
- **Multi-Device Support**: Desktop, tablet, mobile, and all browsers

## Support

For deployment issues or questions:
1. Check Railway/Render documentation
2. Review Django deployment checklist
3. Check server logs in your hosting dashboard

## License

This project is proprietary to RK Ventures.

---

**Your website will be accessible to users worldwide on any device once deployed!**
