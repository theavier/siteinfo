from django.core.management.base import BaseCommand, CommandError
from api.scansites import scansites

class Command(BaseCommand):
    print('Running scanner..."')
    help = 'Runs sitescan tool'
    def handle(self, *args, **kwargs):
        scansites()







