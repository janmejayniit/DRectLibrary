from django_seed import Seed
from books.models import Book, Author, Genre, Language
import random
import datetime

# from django.utils.timezone import get_current_timezone, make_aware
# some_datetime = datetime.datetime(2023, 10, 1, 12, 0, 0)  # Example datetime
# make_aware(some_datetime, get_current_timezone(), is_dst=False)

def run():
    seeder = Seed.seeder()

    # Seed authors
    seeder.add_entity(Author, 10, {
        'first_name': lambda x: seeder.faker.first_name(),
        'last_name': lambda x: seeder.faker.last_name(),
    })

    # Seed genres and languages first manually (if not many)
    Genre.objects.get_or_create(name='Fiction')
    Language.objects.get_or_create(name='English')

    # Seed books
    seeder.add_entity(Book, 20, {
        'title': lambda x: seeder.faker.sentence(nb_words=4),
        'isbn': lambda x: seeder.faker.isbn13(),
        'genre': lambda x: Genre.objects.order_by('?').first(),
        'author': lambda x: Author.objects.order_by('?').first(),
        'language': lambda x: Language.objects.order_by('?').first(),
        'description': lambda x: seeder.faker.text(max_nb_chars=200),
        'publication_date': lambda x: seeder.faker.date_this_decade(),
        'cover_image': lambda x: seeder.faker.image_url(width=640, height=480),
        'publisher': lambda x: seeder.faker.company(),
        'total_copies': lambda x: random.randint(1, 20),
        'pages': lambda x: random.randint(100, 1000),
        'price': lambda x: random.uniform(10.0, 1000.0),
    })

    seeder.execute()
    