import csv
from django.core.management.base import BaseCommand, CommandError
from blog.models import BlogPost

class Command(BaseCommand):
    help = 'Import blog posts from a CSV file'

    def add_arguments(self, parser):
        """
            Add logic to add argument for passing the csv file
        """
        parser.add_argument('csv_file', type=str, help='Path to the CSV file containing blog posts')

    def handle(self, *args, **kwargs):
        """
            populate the database with the same data from data/blog_post.csv
            Style the output so that errors are shown in red and a successfull import is in green.
        """
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, mode='r', encoding='utf-8') as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    BlogPost.objects.create(
                        title=row['title'],
                        content=row['content'],
                        country=row['country'],
                    )
            self.stdout.write(self.style.SUCCESS(f'Successfully imported blog posts from {csv_file}'))
        except FileNotFoundError:
            raise CommandError(f'File {csv_file} not found') from None
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error importing blog posts: {e}'))
            
# run the command
# python manage.py import_blog_posts .\data\blog_posts.csv
