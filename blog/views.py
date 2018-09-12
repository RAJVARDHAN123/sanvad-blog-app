from django.shortcuts import render,redirect, get_object_or_404
from .models import Post
from .forms import PostFormCreate, CommentForm
from django.contrib.auth.decorators import login_required

@login_required
def post_create(request):
	template_name = 'blog/post_create.html'
	form  = PostFormCreate(request.POST or None)
	if request.method=="POST":
		if form.is_valid():
			form.save()
			return redirect('post_list')

	context = {
		'form':form,
	}
	return render(request, template_name, context )

def post_detail(request,id):
	template_name = 'blog/post_detail.html'
	post = get_object_or_404(Post,id=id)

	context = {
		'post':post,
	}
	return render(request, template_name, context )

def post_list(request):
	template_name = 'blog/post_list.html'
	posts = Post.objects.all()

	context = {
		'posts':posts,
	}
	return render(request, template_name, context )
	
@login_required
def post_update(request,id):
	template_name = 'blog/post_update.html'
	post = get_object_or_404(Post, id=id)
	form  = PostFormCreate(request.POST or None,instance=post)
	if request.method == "POST":
		if form.is_valid():
			form.save()
		return redirect('post_detail', id=post.id)

	context = {
		'form':form,
		'post':post,
	}
	return render(request, template_name, context )

@login_required	
def post_delete(request,id):
	template_name = 'blog/post_delete.html'
	post = get_object_or_404(Post,id=id)
	if request.method == "POST":
		post.delete()
		return redirect('post_list')
	context = {
		'post':post,
	}
	return render(request, template_name, context )

def add_comment_to_post(request, id):
	template_name = 'blog/add_comment_to_post.html'
	post = get_object_or_404(Post, id=id)
	form = CommentForm(request.POST or None)
	if request.method == "POST":
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('post_detail', id=post.id)  
		else:
			form = CommentForm()

	context = {
		'form':form,
	}

	return render(request, template_name, context)

