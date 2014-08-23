from django.http import HttpResponse, Http404

from .models import BrightcoveItems
from .utils import BrightcoveApi
from .widgets import BrightcoveModelChoiceField, BrightcoveSelect


def refresh_item_list(request, pk):
    """Updates the select of brightcove items in a form"""
    if not request.is_ajax():
        raise Http404
    api = BrightcoveApi()
    api.synchronize_list()
    items = BrightcoveItems.objects.all().order_by('name')
    choices = BrightcoveModelChoiceField(items)
    widget = BrightcoveSelect()
    return HttpResponse(widget.render_options(choices.choices, [pk]))
