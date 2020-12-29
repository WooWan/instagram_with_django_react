from django.shortcuts import render, redirect, get_object_or_404

@login_required
def post_new(request):
  if request.method=="POST"
    form =PostForm(request.POST, request.FILES)
    if form.is_valid():
      post=form.save(commit=False)
      post.author=request.user
      post.save()
      post.tag_set.add(*post.extract_tag_list())
      mesagges.success(request, "포스팅을 저장하였습니다.")
      return redirect('/')
  else:
    form=PostForm()


