from django.db import models
from django.utils.translation import ugettext_lazy as _

from .models import BrightcoveItems
from .widgets import BrightcoveModelChoiceField


class BrightcoveManager(models.ForeignKey):
    """
    Custom manager that inherits form the ForeignKey default django field, used to easily set a field up in order to
    relate a Model the the BrightCoveItems model and widget.

    i.e.::

        class MyModel(Model):
            my_field = BrightcoveManager()
    """
    def __init__(self, null=True, blank=True, **kwargs):
        """Overwites default settings to setup the relationship with the BrightcoveItems model"""
        kwargs['verbose_name'] = kwargs.get('verbose_name', _("Brightcove"))
        kwargs['null'] = kwargs.get('null', True)
        kwargs['blank'] = kwargs.get('blank', True)
        to_field = 'brightcove_id'
        rel_class = models.ManyToOneRel
        db_constraint = True
        super(BrightcoveManager, self).__init__(BrightcoveItems, to_field, rel_class, db_constraint, **kwargs)

    def formfield(self, **kwargs):
        """Overwites default formfield to trigger the custom Brightcove choicefield widget"""
        defaults = {
            'form_class': BrightcoveModelChoiceField,
        }
        return super(BrightcoveManager, self).formfield(**defaults)

    def south_field_triple(self):
        """Provide a suitable description of this field for South."""
        from south.modelsinspector import introspector
        args, kwargs = introspector(self)
        return 'django.db.models.fields.related.ForeignKey', args, kwargs
