##from django.template import Context, loader
##from django.http import HttpResponse
##from django.http import Http404
from django.shortcuts import render_to_response, get_object_or_404
from engineered.comics.models import Strip

# Each of these view callback can do whatever we want, as long as a
# HttpResponse is returned or a Http404 is raised.

def index(request):
    """Respond to page request for the front page: display the latest
    strip.
    """
    latest_strip = Strip.objects.all().order_by('-sub_date')[:1]

##    template = loader.get_template('comics/index.html')
##    context = Context({
##        'latest_strip': latest_strip,
##    })

##    return HttpResponse(template.render(context))
    return render_to_response('comics/strip.html',
            {'strip': latest_strip})

def strip(request, strip_id):
    """Respond to page request for a specific strip."""
##    try:
##        strip = Strip.objects.get(pk=strip_id)
##    except Strip.DoesNotExist:
##        raise Http404
    strip = get_object_or_404(Strip, pk=strip_id)

    return render_to_response('comics/strip.html',
            {'strip': strip})
