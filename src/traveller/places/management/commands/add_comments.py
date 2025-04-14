import csv
import random

from django.core.management.base import BaseCommand
from django.conf import settings

from django.contrib.auth.models import User
from places.models import Comment, Place


class Command(BaseCommand):
    help = 'This command creates a new categories'
    def handle(self, *args, **options):
        
        Comment.objects.all().delete()
        
        print("Comments deleted successfully.")
        
        print("Importing comments...")
        file = open(settings.BASE_DIR / "place_comments.csv", encoding='utf-8')

        csv_reader = csv.reader(file)

        next(csv_reader)

        user = User.objects.create_user(
            username='john@example.com',
            password='john123',
            first_name='John Doe'
        )

        for row in csv_reader:
            comment = row[0]
            place = Place.objects.all()

            Comment.objects.create(comment=comment, user=user, place=random.choice(place))

        print("Comments imported successfully.")