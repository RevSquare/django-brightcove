from django.core import exceptions
from django.forms import IntegerField, NumberInput
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from .models import BrightcoveItems
from .utils import BrightcoveApi


class BrightcoveNumberInput(NumberInput):
    """
    Overwrites the default Select widget to add the brightcove specific magic.
    """
    choices = []

    def render(self, name, value, attrs=None):
        item = None
        if value:
            try:
                item = BrightcoveItems.objects.get(pk=value)
            except BrightcoveItems.DoesNotExist:
                pass

        context = {'select': self.render_input(name, value, attrs), 'pk': value, 'item': item}
        return render_to_string('select_widget.html', context)

    class Media:
        css = {
            'all': ('brightcove/css/brightcove.css',
                    '//maxcdn.bootstrapcdn.com/font-awesome/4.1.0/css/font-awesome.min.css',)
        }
        js = ('brightcove/js/brightcove.js', '//admin.brightcove.com/js/BrightcoveExperiences.js',)

    def render_input(self, name, value, attrs=None):
        return super(BrightcoveNumberInput, self).render(name, value, attrs)


class BrightcoveIntegerField(IntegerField):
    """
    Overwrites the default IntegerField widget to force the custom widget to be displayed.
    """
    widget = BrightcoveNumberInput

    def clean(self, value):
        value = super(BrightcoveIntegerField, self).clean(value)
        if not self._has_changed(self.initial, value):
            return value
        api = BrightcoveApi()
        try:
            api.get_by_id(value)
        except:
            raise exceptions.ValidationError(_("The id you have passed doesn't seem to exist in the Brightcove \
                database."))
        return value
