##from django.template import Context, loader
##from django.http import HttpResponse
##from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from engineered.comics.models import Strip
import random as rand

# Each of these view callback can do whatever we want, as long as a
# HttpResponse is returned or a Http404 is raised.

def latest(request):
    """Respond to page request for the front page: display the latest
    strip.
    """
    latest_strip = Strip.objects.latest()

##    template = loader.get_template('comics/index.html')
##    context = Context({
##        'latest_strip': latest_strip,
##    })

##    return HttpResponse(template.render(context))
    return render_to_response('comics/strip.html', 
            _build_context(latest_strip))

def strip(request, strip_id):
    """Respond to page request for a specific strip."""
##    try:
##        strip = Strip.objects.get(pk=strip_id)
##    except Strip.DoesNotExist:
##        raise Http404
    strip = get_object_or_404(Strip, pk=strip_id)

    return render_to_response('comics/strip.html', _build_context(strip))

def random(request):
    """Respond by serving a random strip."""
    count = Strip.objects.count()
    which = int(rand.random() * count) + 1
    strip = get_object_or_404(Strip, pk=which)

    return render_to_response('comics/strip.html', _build_context(strip))


# *** UTILITY FUNCTIONS ***

def _build_context(strip):
    """Build the context to template from a strip.

    This involves identifying prev, next, etc.
    """
    context = {'strip': strip}

    try:
        prev_id = strip.id - 1
        prev = Strip.objects.get(id=prev_id)
    except Strip.DoesNotExist:
        prev = strip
    context['prev'] = prev

    try:
        next_id = strip.id + 1
        next = Strip.objects.get(id=next_id)
    except Strip.DoesNotExist:
        next = strip
    context['next'] = next

    return context
