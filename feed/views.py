from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from account.models import UserModel

# 로그인한 사용자들의 피드가 최신순으로 조회되어야 한다.
# 모든 비로그인 방문자들도 메인 피드를 구경할 수 있어야 한다.


def home(request):
    if request.method == 'GET':
        all_feed = Post.objects.all().order_by('-created_at')
        return render(request, 'feed/feed.html', {'feed': all_feed})


# 메인 피드에 전체 게시글을 보여준다. : GET
def feed(request):
    if request.method == 'GET':
        user = request.user.is_authenticated###### 이부분 바뀜.
        if user:    ##########이부분
            all_feed = Post.objects.all().order_by('-created_at')
            return render(request, 'feed/feed.html', {'feed': all_feed})

# 로그인 사용자들이 피드 업로드 시 저장해주는 함수. : POST
# @login_required
def upload_feed(request):
    if request.method == 'GET':
        return render(request, 'feed/feed_upload.html')
    if request.method == 'POST':
        print("1번")
        # user = request.user
        my_post = Post()
        # my_post.author = user
        print("2번")
        # request.POST.get('html의 각각의 태그 name이 여기에 적힙니다','')
        my_post.user = request.user #### 포스트 유저에 요청한 유저가 저장됨!
        my_post.post_title = request.POST.get('subject', None)
        my_post.post_content = request.POST.get('contents', None)
        my_post.post_image = request.POST.get('imageUrl', None) 
        
        my_post.save()
        
        id = my_post.id # 객체 생성 후(save이후) 객체 id 저장해 상세보기 페이지로.
        return redirect('/feed/detail/'+str(id))


# 로그인한 사용자들이 자신의 피드를 삭제할 함수.
@login_required
def delete_feed(request, id):
    my_feed = Post.objects.get(id=id)
    user = request.user###### 이부분 바뀜.
    if user == my_feed.user:
        my_feed.delete()
    return redirect('/feed')

# @login_required ####### pagenotfound떠서 삭제함
def modify_feed(request, id):
    if request.method == 'GET':
        my_post = Post.objects.get(id=id)
        return render(request, 'feed/feed_modify.html', {'post':my_post, 'id':id})
    if request.method == 'POST':
        my_post = Post.objects.get(id=id)
        my_post.post_title = request.POST.get('subject', None)
        my_post.post_content = request.POST.get('contents', None)
        my_post.post_image = request.POST.get('imageUrl', None)
        my_post.save()
        # render(request, 'feed/feed_detail.html', {'post':my_post, 'id':id})
        return redirect('/feed/detail/'+str(id))
    # 서경 : 게시물 수정하고나면 그위치에서 그대로 적용되도록 수정
    
def view_feed(request, id):
    if request.method == 'GET':
        my_post = Post.objects.get(id=id)
        return render(request, 'feed/feed_detail.html', {'post':my_post, 'id':id})
    if request.method == 'POST':
        my_post = Post.objects.get(id=id)
        my_post.post_title = request.POST.get('subject', None)
        my_post.post_content = request.POST.get('contents', None)
        my_post.post_image = request.POST.get('imageUrl', None)
        my_post.save()
        return render(request, 'feed/feed_detail.html', {'post':my_post, 'id':id})

    # detail보는 함수.

    

