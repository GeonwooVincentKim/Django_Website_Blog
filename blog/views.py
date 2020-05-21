from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.conf.urls import url

from django.core.urlresolvers import reverse_lazy, reverse
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.translation import ugettext as _
from django.views.decorators.cache import cache_page
from django.views.generic import FormView

from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    qs = Post.objects.all()
    posts = qs.filter(published_date__lte=timezone.now())
    qs = posts.order_by('published_date')

    # return render(request,
    #               'blog/base.html',
    #               {
    #                   'post': qs,
    #               })
    return render(request, 'blog/post_list.html', {
            'post_list': qs,
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


# @login_required is when visitors
# who is not users of this website
# cannot post new post that they want.
# and also cannot read posts
# if they don't being member of this website.

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm()

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {
        'form': form,
    })


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.delete()
            return redirect('/')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_delete.html', {
        'form': form,
    })


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            print('changed')
            messages.add_message(request, messages.INFO, 'Welcome')
            return redirect('change_password')
        else:
            print('not changed')
            messages.error(request, _('Please correct the error below.'))
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password_details.html', {
        'form': form
    })


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
