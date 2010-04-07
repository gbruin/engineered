from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from engineered.comics.models import Strip
import random as rand

# Each of these view callback can do whatever we want, as long as a
# HttpResponse is returned or a Http404 is raised.

def latest(request):
    """Respond to page request for the front page: display the latest
    strip.
    """
    try:
        latest_strip = Strip.objects.order_by('pk').reverse()[0]
    except IndexError:
        raise Http404('No comic strip in the database.')

    return render_to_response('comics/strip.html', 
            _build_context(latest_strip),
            context_instance=RequestContext(request))

def strip(request, strip_id):
    """Respond to page request for a specific strip."""
    strip = get_object_or_404(Strip, pk=strip_id)

    return render_to_response('comics/strip.html',
            _build_context(strip),
            context_instance=RequestContext(request))

def random(request):
    """Respond by serving a random strip."""
    count = Strip.objects.count()
    which = int(rand.random() * count) + 1
    strip = get_object_or_404(Strip, pk=which)

    return render_to_response('comics/strip.html',
            _build_context(strip),
            context_instance=RequestContext(request))

def archive(request):
    """Serve a list of strip titles and links in the database."""
    strips = Strip.objects.order_by('id').reverse()

    return render_to_response('comics/archive.html',
            {'strips': strips},
            context_instance=RequestContext(request))

def contact(request):
    """A view that list contact information."""
##    raise Http404('Under construction'
    return render_to_response('comics/contact.html', {},
            context_instance=RequestContext(request))


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
