from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
def blog_post(request, article_id):

    blog_posts = [
        {'id': 1,'title': '1st Blog Post Title', 'author': 'Obed Ehoneah', 'content': 'This is a summary of the first blog post...', 'date': "January 2, 2024"},
        {'id': 2,'title': '2nd Blog Post Title', 'author': 'Msthur Isac', 'content': 'This is a summary of the second blog post...', 'date': "January 4, 2024"},
        {'id': 3,'title': '3rd Blog Post Title', 'author': 'Alex Johnson', 'content': 'This is a much longer summary of the third blog post that will exceed fifty characters to demonstrate truncation.', 'date': "January 6, 2024"}
    ]

    selected_post = None

    for post in blog_posts:
        if article_id == post['id']:
            selected_post = post
            break

    if selected_post == None:
        raise Http404("No blog post found")

    return render(request, 'blog/post.html', selected_post)

def blog_archive(request):
    # get all the blog posts from the database
    # put them in a list
    blog_posts = [
        {'id': 1,'title': '1st Blog Post Title', 'author': 'Obed Ehoneah', 'content': 'This is a summary of the first blog post...', 'date': "January 2, 2024"},
        {'id': 2,'title': '2nd Blog Post Title', 'author': 'Msthur Isac', 'content': 'This is a summary of the second blog post...', 'date': "January 4, 2024"},
        {'id': 3,'title': '3rd Blog Post Title', 'author': 'Alex Johnson', 'content': 'This is a much longer summary of the third blog post that will exceed fifty characters to demonstrate truncation.', 'date': "January 6, 2024"}
    ]

    context = {"list_of_posts": blog_posts}

    return render(request, 'blog/index.html', context)