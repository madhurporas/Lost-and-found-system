from django.apps import AppConfig
import threading, time
from django.utils import timezone
from datetime import timedelta


class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        from report_found.models import Item_Found
        from report_lost.models import Item_Lost

        def auto_delete_scheduler():
            while True:
                now = timezone.now()
                if now.hour == 0 and now.minute == 0:
                    cutoff = now.date() - timedelta(days=7)
                    Item_Found.objects.filter(date_posted__lt=cutoff).delete()
                    Item_Lost.objects.filter(date_posted__lt=cutoff).delete()
                    print("Old items deleted successfully.")
                time.sleep(60)  # check every minute

        thread = threading.Thread(target=auto_delete_scheduler, daemon=True)
        thread.start()
