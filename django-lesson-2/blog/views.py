from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def blog(request, article_id):
    if request.method == "GET":
        # get the specific article
        pass
    elif request.method == "POST":
        # create a new article with this id
        pass
    elif request.method == "PUT":
        # update the article
        pass
    elif request.method == "DELETE":
        # delete this article
        pass
    return HttpResponse(f"<h1>Blog {article_id}</h1>")