from .models import Category

def Main(request):
    links=Category.objects.all()
    return dict(links=links)
