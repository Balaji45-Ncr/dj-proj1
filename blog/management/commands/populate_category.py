from django.core.management.base import BaseCommand
from blog.models import Category
import random

class Command(BaseCommand):
    help='This command inserts category data'

    def handle(self, *args, **options):

        Category.objects.all().delete()

        categories=['Sports','Art','Technology','Food','Science']

        for catgeory_name in categories:
            Category.objects.create(name=catgeory_name)

        self.stdout.write(self.style.SUCCESS('Completed inserting data!'))