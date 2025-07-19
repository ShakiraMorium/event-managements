from events.models import Category, Participant, Event
from django.db import IntegrityError, DatabaseError
from django.utils import timezone
from faker import Faker
from datetime import timedelta
import random
import traceback

fake = Faker()

def populate():
    print("Starting data population…")
    try:
        category_names = ['Music', 'Drama', 'Conference', 'Workshop', 'Technology', 'Sports']
        categories = []
        for name in category_names:
            cat, created = Category.objects.get_or_create(name=name)
            categories.append(cat)
        print(f"Created/fetched {len(categories)} categories")
        
        participants = []
        for _ in range(20):
            try:
                p = Participant.objects.create(
                    full_name=fake.name(),
                    email=fake.unique.email()
                )
                participants.append(p)
            except IntegrityError as e:
                print(f"Participant skipped due to integrity error: {e}")
        print(f"Created {len(participants)} participants")
        
        event_count = 0
        for _ in range(10):
            try:
                start = fake.date_time_between(start_date='-30d', end_date='+30d', tzinfo=timezone.get_current_timezone())
                end = start + timedelta(hours=random.randint(1, 5))
                evt = Event.objects.create(
                    title=fake.sentence(nb_words=4),
                    description=fake.text(max_nb_chars=200),
                    category=random.choice(categories),
                    start_datetime=start,
                    end_datetime=end
                )
                evt.participants.set(random.sample(participants, k=random.randint(2, min(6, len(participants)))))
                event_count += 1
            except (IntegrityError, DatabaseError) as e:
                print(f"Event skipped due to DB error: {e}")
        print(f" Created {event_count} events")

    except Exception:
        print(" Unexpected error during population:")
        traceback.print_exc()
    else:
        print(" Data population complete.")

if __name__ == "__main__":
    populate()




# from django.core.management.base import BaseCommand
# from events.models import Category, Participant, Event
# from django.db import IntegrityError, DatabaseError
# from django.utils import timezone
# from faker import Faker
# from datetime import timedelta
# import random
# import traceback

# fake = Faker()

# class Command(BaseCommand):
#     help = "Populate the database with sample categories, participants, and events"

#     def handle(self, *args, **kwargs):
#         print("Starting data population…")
#         try:
#             category_names = ['Music', 'Drama', 'Conference', 'Workshop', 'Technology', 'Sports']
#             categories = []
#             for name in category_names:
#                 cat, created = Category.objects.get_or_create(name=name)
#                 categories.append(cat)
#             self.stdout.write(f"Created/fetched {len(categories)} categories")
            
#             participants = []
#             for _ in range(20):
#                 try:
#                     p = Participant.objects.create(
#                         full_name=fake.name(),
#                         email=fake.unique.email()
#                     )
#                     participants.append(p)
#                 except IntegrityError as e:
#                     self.stdout.write(f"Participant skipped due to integrity error: {e}")
#             self.stdout.write(f"Created {len(participants)} participants")
            
#             event_count = 0
#             for _ in range(10):
#                 try:
#                     start = fake.date_time_between(start_date='-30d', end_date='+30d', tzinfo=timezone.get_current_timezone())
#                     end = start + timedelta(hours=random.randint(1, 5))
#                     evt = Event.objects.create(
#                         title=fake.sentence(nb_words=4),
#                         description=fake.text(max_nb_chars=200),
#                         category=random.choice(categories),
#                         start_datetime=start,
#                         end_datetime=end
#                     )
#                     evt.participants.set(random.sample(participants, k=random.randint(2, min(6, len(participants)))))
#                     event_count += 1
#                 except (IntegrityError, DatabaseError) as e:
#                     self.stdout.write(f"Event skipped due to DB error: {e}")
#             self.stdout.write(f"Created {event_count} events")

#         except Exception:
#             self.stdout.write("Unexpected error during population:")
#             traceback.print_exc()
#         else:
#             self.stdout.write("Data population complete.")
