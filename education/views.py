from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from education.models import Article


def show(request):
    articles = Article.objects.order_by('publication_date')
    t = get_template('education/articles-all.html')
    html = t.render(Context({'articles': articles}))
    return HttpResponse(html)


def article(request, article_id):
    article_item = Article.objects.get(id=article_id)
    t = get_template('education/article.html')
    html = t.render(Context({'article_item': article_item}))
    return HttpResponse(html)