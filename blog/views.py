from django.shortcuts import render
from django.core.paginator import Paginator
from .models import BlogPost
from .utils import get_user_country



def post_list(request):
    country = get_user_country(request=request)
    page = request.GET.get('page')
    posts = BlogPost.objects.all().order_by('-created_at')
    paginator = Paginator(posts, 12)
    page_obj = paginator.get_page(page)

    context = {
        'posts': page_obj.object_list,
        'page_obj': page_obj,
        'country': country, 
    }
    return render(request, 'blog/post_list.html', context)

