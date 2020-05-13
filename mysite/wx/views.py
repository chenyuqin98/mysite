from django.shortcuts import get_object_or_404, render, redirect
from .models import User, books, manager, upload_books, series, recommend_books, IMG, user_action
from django.db.models import Q
from django.core import serializers
from django.template import loader
from django.http import HttpResponse, JsonResponse, Http404


# user system
def wx_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        try:
            user = User.objects.get(userAccount=username)
            if user.userPasswd != passwd:
                return HttpResponse('用户名或密码错误')
        except User.DoesNotExist as e:
            return HttpResponse("用户名不存在")
        # 登录成功
        print(username)
        print(passwd)
        return HttpResponse("登录成功！")
    else:
        return HttpResponse("请求错误")


def wx_regist(request):
    if request.method == 'POST':
        user = User()
        user.userAccount = request.POST.get('name')
        user.userPasswd = request.POST.get('pwd')
        print(user.userAccount)
        print(user.userPasswd)
        user.save()
        return HttpResponse('注册成功！')


def wxapp(request):  # get data for test
    if request.method == 'GET':
        lists = books.objects.filter(website='libgen.lc')
        json_data = serializers.serialize("json", lists)
        print(json_data)
        # for list in lists:
        #     print(list.title)
        return JsonResponse(json_data, safe=False)


def search(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        lists = books.objects.filter(Q(title__icontains=q) | Q(author__icontains=q))
        json_data = serializers.serialize("json", lists)
        print(json_data)
        # for list in lists:
        #     print(list.title)
        return JsonResponse(json_data, safe=False)

def search_detail(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        detail = books.objects.filter(id=id)
        json_data = serializers.serialize("json", detail)
        print(json_data)
        return JsonResponse(json_data, safe=False)

def search_recommend_detail(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        detail = recommend_books.objects.filter(id=id)
        json_data = serializers.serialize("json", detail)
        print(json_data)
        return JsonResponse(json_data, safe=False)


def add_history(request):
    if request.method == 'POST':
        account = request.POST.get('user_id')
        user = User.objects.filter(userAccount=account)[0]
        user_id = user.id
        history = user_action(
            user_id=user_id,
            books_id=request.POST.get('book_id'),
            type=request.POST.get('type'),
            action='history'
        )
        history.save()
    return HttpResponse('成功！')
def add_favo(request):
    if request.method == 'POST':
        account = request.POST.get('user_id')
        user = User.objects.filter(userAccount=account)[0]
        user_id = user.id
        history=user_action(
            user_id=user_id,
            books_id=request.POST.get('book_id'),
            type=request.POST.get('type'),
            action='favo'
        )
        # print(request.POST.get('user_id'),request.POST.get('book_id'))
        history.save()
    return HttpResponse('成功！')
def show_history(request):
    if request.method=='GET':
        account = request.GET.get('user_id')
        user = User.objects.filter(userAccount=account)[0]
        user_id = user.id
        # user_id=request.GET.get('user_id')
        showed_history=user_action.objects.filter(Q(user_id=user_id) & Q(action='history'))
        json_data = serializers.serialize("json", showed_history)
        print(json_data)
        return JsonResponse(json_data, safe=False)
def show_favo(request):
    if request.method=='GET':
        account = request.GET.get('user_id')
        user = User.objects.filter(userAccount=account)[0]
        user_id = user.id
        # user_id=request.GET.get('user_id')
        showed_history=user_action.objects.filter(Q(user_id=user_id) & Q(action='favo'))
        json_data = serializers.serialize("json", showed_history)
        print(json_data)
        return JsonResponse(json_data, safe=False)
def user_upload(request):
    if request.method=='POST':
        account=request.POST.get('user_id')
        user = User.objects.filter(userAccount=account)[0]
        user_id=user.id
        upload_book=upload_books(
            uploader_id=user_id,
            title=request.POST.get('title'),
            type=request.POST.get('type'),
            website=request.POST.get('website'),
            author=request.POST.get('author'),
            publisher=request.POST.get('publisher'),
            year=request.POST.get('year'),
            url=request.POST.get('url'),
            cover=request.POST.get('cover'),
            introduce=request.POST.get('intro'),
            status='待审核'
        )
        upload_book.save()
    return HttpResponse('上传成功')
def show_upload(request):
    if request.method=='GET':
        account = request.GET.get('user_id')
        user = User.objects.filter(userAccount=account)[0]
        user_id = user.id
        # user_id=request.GET.get('user_id')
        showed_upload=upload_books.objects.filter(uploader_id=user_id)
        json_data = serializers.serialize("json", showed_upload)
        print(json_data)
        return JsonResponse(json_data, safe=False)
def level_up(user_id):
    user = User.objects.filter(user_id=user_id)
    exp =user.exp
    if exp<10:  # 升级所需经验指数递增
        level=1
    elif exp<30:
        level=2
    elif exp<70:
        level=3
    elif exp<150:
        level=4
    elif exp<310:
        level=5
    user.level=level
    user.save()
def add_exp(request):
    if request.method == 'POST':
        account = request.POST.get('user_id')
        user = User.objects.filter(userAccount=account)[0]
        user_id = user.id
        # user_id = request.GET.get('user_id')
        num = request.POST.get('num')
        user = User.objects.filter(user_id=user_id)
        exp = user.exp
        exp += num
        user.exp = exp
        user.save()
        level_up(user_id)
def add_scores(request):
    if request.method == 'POST':
        account = request.POST.get('user_id')
        user = User.objects.filter(userAccount=account)[0]
        user_id = user.id
        # user_id = request.POST.get('user_id')
        num = request.POST.get('num')
        user = User.objects.filter(user_id=user_id)
        scores = user.scores
        scores += num
        user.scores = scores
        user.save()
def show_user_info(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        detail = User.objects.filter(userAccount=user_id)
        json_data = serializers.serialize("json", detail)
        print(json_data)
        return JsonResponse(json_data, safe=False)
def show_all_recommend(request):
    if request.method == 'GET':
        books = recommend_books.objects.all()
        json_data = serializers.serialize("json", books)
        print(json_data)
        # for list in lists:
        #     print(list.title)
        return JsonResponse(json_data, safe=False)
def show_all_series(request):
    if request.method == 'GET':
        books = series.objects.all()
        json_data = serializers.serialize("json", books)
        print(json_data)
        # for list in lists:
        #     print(list.title)
        return JsonResponse(json_data, safe=False)
def show_one_recommend(request):
    if request.method == 'GET':
        series_id = request.GET.get('series_id')
        books = recommend_books.objects.filter(series_id=series_id)
        json_data = serializers.serialize("json", books)
        print(json_data)
        # for list in lists:
        #     print(list.title)
        return JsonResponse(json_data, safe=False)


# manager system
def manager_home(request):
    return render(request, 'home.html', )


def manager_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        passwd = request.POST.get('password')
        # print(username)
        # print(passwd)
        try:
            user = manager.objects.get(userAccount=username)
            if user.userPasswd != passwd:
                # return HttpResponse('用户名或密码错误')
                return render(request, 'result.html', {'result': '用户名或密码错误!'})
        except manager.DoesNotExist as e:
            return render(request, 'result.html', {'result': '用户名不存在!'})
            # return HttpResponse("用户名不存在")
        # 登录成功
        print(username)
        print(passwd)
        return redirect('/wx/index/')
        # return redirect('/wx/login/')
    else:
        return render(request, 'result.html', {'result': '请求错误!'})
        # return HttpResponse("请求错误")


def index(request):
    UploadBooks = upload_books.objects.order_by('id')
    Series = series.objects.order_by('id')
    RecommendBooks = recommend_books.objects.order_by('id')
    template = loader.get_template('index.html')
    context = {
        'UploadBooks': UploadBooks,
        'Series': Series,
        'RecommendBooks': RecommendBooks,
    }
    return HttpResponse(template.render(context, request))


def upload_detail(request, upload_books_id):
    try:
        UploadBooks = upload_books.objects.get(pk=upload_books_id)
    except upload_books.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'upload_detail.html', {'UploadBooks': UploadBooks})


def series_detail(request, series_id):
    try:
        Series = series.objects.get(pk=series_id)
    except series.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'series_detail.html', {'Series': Series})


def recommend_detail(request, recommend_books_id):
    try:
        RecommendBooks = recommend_books.objects.get(pk=recommend_books_id)
    except recommend_books.DoesNotExist:
        raise Http404("Does not exist")
    return render(request, 'recommend_detail.html', {'RecommendBooks': RecommendBooks})


# 管理员操作
def add_series_detail(request):
    return render(request, 'add_series_detail.html')


def add_series(request):
    if request.method == 'POST':
        Series = series(
            series_name=request.POST.get('name'),
            cover=request.FILES.get('cover')
        )
        Series.save()
        print(Series.series_name)
        print(Series.cover)
    # return HttpResponse('Succeed!')
    return render(request, 'result.html', {'result': '添加系列成功!'})


def add_recommend_detail(request):
    return render(request, 'add_recommend_detail.html')


def add_recommend(request):
    if request.method == 'POST':
        RecommendBooks = recommend_books()
        RecommendBooks.bookname = request.POST.get('name')
        RecommendBooks.isbn = request.POST.get('isbn')
        RecommendBooks.author = request.POST.get('author')
        RecommendBooks.introduce = request.POST.get('introduce')
        RecommendBooks.cover = request.FILES.get('cover')
        RecommendBooks.url = request.FILES.get('url')
        RecommendBooks.series_id_id = request.POST.get('series_id')
        RecommendBooks.save()
        print(RecommendBooks.bookname)
    # return HttpResponse('Succeed!')
    return render(request, 'result.html', {'result': '添加成功!'})


def delete_this_book(request, recommend_books_id):
    try:
        RecommendBooks = recommend_books.objects.filter(id=recommend_books_id).first()
        RecommendBooks.delete()
    except recommend_books.DoesNotExist:
        raise Http404("Does not exist")
    # return HttpResponse('successfully delete!')
    return render(request, 'result.html', {'result': '删除成功!'})


def delete_this_series(request, series_id):
    try:
        Series = series.objects.filter(id=series_id).first()
        Series.delete()
    except recommend_books.DoesNotExist:
        raise Http404("Does not exist")
    # return HttpResponse('successfully delete!')
    return render(request, 'result.html', {'result': '删除成功!'})


def check_and_submit(request, upload_books_id):
    try:
        book = upload_books.objects.filter(id=upload_books_id).first()
        book.status = 'passed'
        book.save()
        book2 = books()
        book2.title = book.title
        book2.type = book.type
        book2.website = book.website
        book2.author = book.author
        book2.publisher = book.publisher
        book2.year = book.year
        book2.cover = book.cover
        book2.url = book.url
        book2.save()
    except recommend_books.DoesNotExist:
        raise Http404("Does not exist")
    # return HttpResponse('succeed!')
    return render(request, 'result.html', {'result': '提交成功!'})


# test
def uploadImg(request):
    """
    图片上传
    :param request:
    :return:
    """
    if request.method == 'POST':
        new_img = IMG(
            img=request.FILES.get('img'),
            name=request.FILES.get('img').name
        )
        new_img.save()
    return render(request, 'uploading.html')
