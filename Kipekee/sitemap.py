from django.contrib.sitemaps import Sitemap
from administrator.models import Item

class ItemSitemap(Sitemap):
    changefreq='daily'
    priority=0.6
    def items(self):
        return Item.objects.filter(outofstalk='False')