from django.core.management import BaseCommand
from recipe_webapp.models import Recipe, Category, RecipeCategory
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Fill database with data'

    def add_arguments(self, parser, **kwargs):
        parser.add_argument('num_records', type=int, help='Number of records to create')

    def handle(self, *args, **kwargs):
        fake = Faker()
        num_records = kwargs['num_records']

        for _ in range(num_records):  # Создаем 10 случайных рецептов
            author = fake.name()
            recipe = Recipe.objects.create(
                title=fake.sentence(nb_words=3),
                description=fake.paragraph(),
                preparation_steps=fake.paragraph(),
                cooking_time=random.randint(10, 120),
                ingredients=fake.words(nb=random.randint(1, 10)),
                author=author,
                weight=random.randint(50, 1000)
            )
            category = Category.objects.create(name=fake.word())
            RecipeCategory.objects.create(recipe=recipe, category=category)