from django.db import models
from django.utils.translation import ugettext_lazy as _

from .models import BrightcoveItems
from .widgets import BrightcoveIntegerField


class BrightcoveField(models.ForeignKey):
    """
    Custom manager that inherits form the ForeignKey default django field, used to easily set a field up in order to
    relate a Model the the BrightCoveItems model and widget.

    i.e.::

        class MyModel(Model):
            my_field = BrightcoveField()
    """
    def __init__(self, null=True, blank=True, **kwargs):
        """Overwites default settings to setup the relationship with the BrightcoveItems model"""
        kwargs['verbose_name'] = kwargs.get('verbose_name', _("Brightcove"))
        kwargs['null'] = null
        kwargs['blank'] = blank
        # If null is set to True we can't use SET_NULL as default
        if null:
            default_on_delete =  models.PROTECT
        else:
            default_on_delete = models.SET_NULL
        kwargs['on_delete'] = kwargs.get('on_delete', default_on_delete)
        to_field = kwargs.pop('to_field', 'brightcove_id')
        rel_class = models.ManyToOneRel
        db_constraint = True
        to = kwargs.pop('to', BrightcoveItems)
        super(BrightcoveField, self).__init__(to, to_field, rel_class, db_constraint, **kwargs)

    def save_form_data(self, instance, data):
        #when data is u'' and form allow te be null, we need to make sure
        #it will not blow up the page
        if data:
            video = BrightcoveItems.objects.get(pk=data)
        else:
            video = None
        super(BrightcoveField, self).save_form_data(instance, video)

    def formfield(self, **kwargs):
        """Overwites default formfield to trigger the custom Brightcove choicefield widget"""
        defaults = {
            'form_class': BrightcoveIntegerField,
        }
        defaults.update(kwargs)
        return super(models.ForeignKey, self).formfield(**defaults)

    def south_field_triple(self):
        """Provide a suitable description of this field for South."""
        from south.modelsinspector import introspector
        args, kwargs = introspector(self)
        return 'django.db.models.fields.related.ForeignKey', args, kwargs
