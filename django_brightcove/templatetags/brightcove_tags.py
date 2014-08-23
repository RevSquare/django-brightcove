from django import template
from django.cong import settings


register = template.Library()


@register.inclusion_tag('tags/brightcove_player.html',
                        takes_context=True)
def brightcove(context, player_id, *args, **kwargs):
    """
    This tags generate the brightcove object code. It required the BRIGHTCOVE_PLAYER constant to be properly setup in
    the django settings.
    """
    if not settings.BRIGHTCOVE_PLAYER:
        raise Exception('BRIGHTCOVE_PLAYER constant is missing from your settings.')
    player = kwargs.get('player', settings.BRIGHTCOVE_PLAYER.keys()[0])

    try:
        context['player'] = settings.BRIGHTCOVE_PLAYER[player]
    except:
        raise KeyError('%s player type is missing from the BRIGHTCOVE_PLAYER constant') % player

    if not context['player'].PLAYERID or not context['player'].PLAYERKEY:
        raise KeyError('%s player type from the BRIGHTCOVE_PLAYER constant is not properly configured') % player

    context['width'] = kwargs.get('width', 480)
    context['height'] = kwargs.get('height', 270)
    context['bgcolor'] = kwargs.get('bgcolor', '#FFFFFF')
    context['isVid'] = kwargs.get('isVid', True)
    context['isUI'] = kwargs.get('isUI', True)
    context['dynamicStreaming'] = kwargs.get('dynamicStreaming', True)
    context['player_id'] = player_id
    return context
