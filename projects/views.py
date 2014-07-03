from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from projects.models import Project


def show(request):
    projects = Project.objects.order_by('publication_date')
    t = get_template('projects/projects.html')
    html = t.render(Context({'projects': projects}))
    return HttpResponse(html)
