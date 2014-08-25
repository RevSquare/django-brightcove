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
        js = ('brightcove/js/brightcove.js', '//admin.brightcove.com/js/BrightcoveExperiences.js',)

    def render_select(self, name, value, attrs=None, choices=()):
        return super(BrightcoveSelect, self).render(name, value, attrs=None, choices=())


class BrightcoveModelChoiceField(ModelChoiceField):
    """
    Overwrites the default ModelChoiceField widget to force the custom BrightcoveSelect widget and re-order the
    queryset by name.
    """
    widget = BrightcoveSelect

    def __init__(self, queryset, empty_label="---------", cache_choices=False,
                 required=True, widget=None, label=None, initial=None,
                 help_text='', to_field_name=None, *args, **kwargs):
        if 'ORDER BY' not in queryset.query.__str__():
            queryset = queryset.order_by('name')
        super(BrightcoveModelChoiceField, self).__init__(queryset, empty_label, cache_choices, required,
                                                         widget, label, initial, help_text, to_field_name,
                                                         *args, **kwargs)
