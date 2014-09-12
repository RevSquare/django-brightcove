from django.http import HttpResponse, Http404


def refresh_item_list(request, pk):
    """Updates the select of brightcove items in a form"""
    if not request.is_ajax():
        raise Http404
    return HttpResponse(pk)
