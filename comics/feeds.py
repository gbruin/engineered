from django.contrib.syndication.feeds import Feed
from models import Strip

class LatestEntries(Feed):
    title = 'Engineered Comic'
    link = '/engineered'
    description = 'Latest comic strips from engineeredcomic.com'

    def items(self):
        return Strip.objects.order_by('-sub_date')
