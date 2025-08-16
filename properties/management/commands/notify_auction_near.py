from django.core.management.base import BaseCommand
from properties.models import Property
from properties.views import create_notification_for_all_users
from datetime import datetime, timedelta
import pytz
import os, json

NOTIFY_CACHE_FILE = 'auction_notify_cache.json'

class Command(BaseCommand):
    help = 'Notify users about auctions that are within 3 days.'

    def handle(self, *args, **options):
        now = datetime.now(pytz.UTC)
        soon = now + timedelta(days=3)
        today_str = now.strftime('%Y-%m-%d')
        notified = set()
        # Load cache
        if os.path.exists(NOTIFY_CACHE_FILE):
            try:
                with open(NOTIFY_CACHE_FILE, 'r') as f:
                    notified = set(json.load(f))
            except Exception:
                notified = set()
        new_notified = set()
        for prop in Property.objects.all():
            auction_date = prop.extra_data.get('auction_date')
            if not auction_date:
                continue
            try:
                # Try parsing as ISO, then as date only
                try:
                    adt = datetime.fromisoformat(auction_date)
                except Exception:
                    adt = datetime.strptime(auction_date, '%Y-%m-%d')
                if adt.tzinfo is None:
                    adt = pytz.UTC.localize(adt)
            except Exception:
                continue
            if now <= adt <= soon:
                days_left = (adt.date() - now.date()).days
                msg = f'Auction for "{prop.title or "Untitled"}" is on {adt.strftime("%Y-%m-%d")}. ({days_left} day(s) left!)'
                cache_key = f'{prop.id}:{today_str}'
                new_notified.add(cache_key)
                if cache_key not in notified:
                    create_notification_for_all_users('Auction Date Approaching', msg, prop, send_email=True)
                    self.stdout.write(self.style.SUCCESS(f'Notification sent for property {prop.id}'))
        # Save updated cache
        with open(NOTIFY_CACHE_FILE, 'w') as f:
            json.dump(list(new_notified), f) 