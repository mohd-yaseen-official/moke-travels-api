import csv
import wget

from django.core.management.base import BaseCommand
from django.conf import settings

from places.models import Category


class Command(BaseCommand):
    help = 'This command creates a new categories'
    def handle(self, *args, **options):
        
        Category.objects.all().delete()
        
        print("Categories deleted successfully.")
        
        print("Importing categories...")
        file = open(settings.BASE_DIR / "categories.csv", encoding='utf-8')

        csv_reader = csv.reader(file)

        next(csv_reader)

        for row in csv_reader:
            name = row[0]
            image_url = row[1]

            image_file_name = f'{name}_image.jpg'
            image_full_path = f'{settings.BASE_DIR}/categories/images/{image_file_name}'
            wget.download(image_url, image_full_path)

            image_file_django_path = f'categories/images/{image_file_name}'


            print(f"Downloaded and saved")
            category = Category.objects.create(
                name=name,
                image=image_file_django_path
            )
        
        print("Categories imported successfully.")