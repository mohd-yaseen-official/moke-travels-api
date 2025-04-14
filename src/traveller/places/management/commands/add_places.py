import csv

from django.core.management.base import BaseCommand
from django.conf import settings

import requests
import wget

from places.models import Place, Category, Gallery


class Command(BaseCommand):
    help = 'This command creates a new places'

    def handle(self, *args, **options):
        Place.objects.all().delete()
        print("Places deleted successfully.")

        print("Importing places...")
        file_path = settings.BASE_DIR / "location.csv"
        with open(file_path, encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)

            for row in csv_reader:
                name = row[0]
                image_url = row[1]
                category_name = row[2]
                description = row[3]
                gallery = row[4]
                location = row[5]

                # Downloading featured image
                response = requests.get(url=image_url)
                if response.status_code == 200:
                    image_file_name = f'{name}_image.jpg'
                    image_full_path = f'{settings.BASE_DIR}/places/images/{image_file_name}'
                    wget.download(image_url, image_full_path)
                    image_file_django_path = f'places/images/{image_file_name}'
                else:
                    image_file_django_path = 'places/images/not_found.png'

                # Creating category
                category, created = Category.objects.get_or_create(name=category_name)

                # Creating place instance
                place_instance = Place.objects.create(
                    name=name,
                    description=description,
                    location=location,
                    featured_image=image_file_django_path,
                    category=category
                )

                # Downloading gallery images
                gallery_images = gallery.split('|')
                for i, image_url in enumerate(gallery_images):
                    response = requests.get(url=image_url)
                    if response.status_code == 200:
                        image_file_name = f'{name}_gallery_{i+1}.jpg'
                        image_full_path = f'{settings.BASE_DIR}/places/images/{image_file_name}'
                        wget.download(image_url, image_full_path)
                        image_file_django_path = f'places/images/{image_file_name}'
                        Gallery.objects.create(
                            place=place_instance,
                            image=image_file_django_path
                        )
        print("Places imported successfully.")
