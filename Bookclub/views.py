from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import Http404
from django.contrib.flatpages.models import FlatPage

@login_required(login_url='/admin/login/')
def custom_flatpage(request, *args, **kwargs):
    url = kwargs.get('url', None)

    try:
        flatpage = FlatPage.objects.get(url=url)
    except FlatPage.DoesNotExist:
        raise Http404("FlatPage not found")

    context = {'flatpage': flatpage}
    return render(request, 'bookclub/meetings_calendar.html', context)
