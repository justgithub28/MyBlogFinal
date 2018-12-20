from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.views.generic import(DeleteView,UpdateView,TemplateView,CreateView,ListView,DetailView)
from blog.models import Comment,Post
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import CommentForm,PostForm,UserForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
# Create your views here.

class AboutView(TemplateView):
    template_name='blog/about.html'

class PostListView(ListView):
    model=Post
    template_name='blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()) #.order_by('-published_date')

class PostDetailView(DetailView):
    model=Post
    template_name='blog/post_detail.html'



class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    model=Post
    redirect_field_name='blog/post_detail.html'

    form_class=PostForm

    def form_valid(self,form):
        self.object =form.save(commit=False)
        self.object.author=self.request.user
        self.object.save()
        return super().form_valid(form)







class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    model=Post
    #redirect_field_name='blog/post_detail.html'
    form_class=PostForm

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')


@login_required
def draftListView(request,*args,**kwargs):
    email=kwargs['email']
    values=Post.objects.filter(author__email__exact = email,published_date__isnull=True)
    return render(request,'blog/post_draft_list.html',{'posts':values})

@login_required
def alluserpost(request,*args,**kwargs):
    email=kwargs['email']
    values=Post.objects.filter(author__email__exact = email,published_date__lte=timezone.now())
    return render(request,'blog/post_draft_list.html',{'posts':values})





##################################################
##################################################
@login_required
def add_comments_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.author=request.user
            comment.post=post
            comment.save()
            return redirect('blog:post_detail',pk=post.pk)
        else:
            form=CommentForm()
        return render(request,'blog/comment_form.html',{'form':form})
    else:
        form=CommentForm()
        return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('blog:post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('blog:post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post=get_object_or_404(Post,pk=pk)
    post.publish()
    return redirect('blog:post_detail',pk=pk)
