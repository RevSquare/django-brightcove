from django.conf import settings

from brightcove.api import Brightcove

from .models import BrightcoveItems


class BrightcoveApi():
    """Class managing communication with the Brightcove API though the brightcove app."""
    token = ''
    connector = None

    def __init__(self, token=''):
        if token:
            self.token = token
        if not self.token:
            self.token = getattr(settings, 'BRIGHTCOVE_TOKEN', None)

        self.connector = Brightcove(self.token)

    def get_by_id(self, brightcove_id):
        video = self.connector.find_video_by_id(brightcove_id)
        if video:
            return self._save_item(video)
        return None

    def _get_list(self):
        return self.connector.find_all_videos()

    def synchronize_list(self):
        """Synchronizes the list of videos form a brightcove account with the BrightcoveItem model."""
        items = self._get_list()
        existing_ids = []
        for item in items.items:
            self._save_item(item)
            existing_ids.append(item.id)
        BrightcoveItems.objects.exclude(brightcove_id__in=existing_ids).delete()

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
        return brightcove_item
