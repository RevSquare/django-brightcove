from django.forms import ModelChoiceField, Select
from django.template.loader import render_to_string

from .models import BrightcoveItems


class BrightcoveSelect(Select):
    """
    Overwrites the default Select widget to add the brightcove specific magic.
    """
    def render(self, name, value, attrs=None, choices=()):
        item = None
        if value is None:
            value = 0
        else:
            item = BrightcoveItems.objects.get(pk=value)
        context = {'select': self.render_select(name, value, attrs=None, choices=()), 'pk': value, 'item': item}
        return render_to_string('select_widget.html', context)

    class Media:
        css = {
            'all': ('brightcove/css/brightcove.css',
                    '//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css',)
        }
        js = ('brightcove/js/brightcove.js',)

    def render_select(self, name, value, attrs=None, choices=()):
        return super(BrightcoveSelect, self).render(name, value, attrs=None, choices=())


class BrightcoveModelChoiceField(ModelChoiceField):
    widget = BrightcoveSelect
