from django.conf import settings

from brightcove.api import Brightcove

from .models import BrightcoveItems


class BrightcoveApi():
    token = ''
    connector = None

    def __init__(self, token=''):
        if token:
            self.token = token
        if not self.token:
            self.token = getattr(settings, 'BRIGHTCOVE_TOKEN', None)

        self.connector = Brightcove(self.token)

    def _get_list(self):
        return self.connector.find_all_videos()

    def synchronize_list(self):
        BrightcoveItems.objects.all().delete()
        items = self._get_list()
        for item in items.items:
            self._save_item(item)

    def _save_item(self, item):
        brightcove_item, created = BrightcoveItems.objects.get_or_create(brightcove_id=item.id)
        brightcove_item.name = item.name
        brightcove_item.video_still_URL = item.videoStillURL
        brightcove_item.thumbnail_URL = item.thumbnailURL
        brightcove_item.short_description = item.shortDescription
        brightcove_item.long_description = item.longDescription
        brightcove_item.length = item.length
        brightcove_item.link_URL = item.linkURL
        brightcove_item.plays_total = item.playsTotal
        brightcove_item.creation_date = item.creationDate
        brightcove_item.published_date = item.publishedDate
        brightcove_item.save()
