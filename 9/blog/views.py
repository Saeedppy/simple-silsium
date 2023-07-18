from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from .models import Article , Category,Comment
from .forms import CommentForm
#from django.http import HttpResponse,JsonResponse

def home(request,page=1):
    article_list=Article.objects.published()    
    paginator=Paginator(article_list,6)
    articles= paginator.get_page(page)
    context={
        "articles":articles,
    }
    return render(request,"blog/home.html",context)

def detail(request,slug):
    article = get_object_or_404(Article.objects.published(),slug=slug)
    comments = article.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.article = article
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    context={
        'article': article,
        'new_comment': new_comment,
        'comments': comments,
        'comment_form': comment_form,

    }
    return render(request,"blog/detail.html",context)
 
def category(request,slug,page=1):
    category= get_object_or_404(Category,slug=slug,status="True")
    articles_list=category.articles.published()
    paginator=Paginator(articles_list,6)
    articles=paginator.get_page(page)
    context={
        "category":category,
        "articles":articles,
    }
    return render (request,"blog/category.html",context)




  
    