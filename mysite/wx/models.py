from django.db import models


class books(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=45, null=True)
    website = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    publisher = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=45, null=True)
    url = models.CharField(max_length=400, null=True)
    cover = models.CharField(max_length=400, null=True)
    introduce = models.TextField(null=True)


class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # 用户账号、不唯一
    userAccount = models.CharField(max_length=20, unique=True)
    # 密码
    userPasswd = models.CharField(max_length=20)
    level = models.IntegerField(default=1)
    # 经验，升级用
    exp = models.IntegerField(default=0)
    # 积分
    scores = models.IntegerField(default=0)
    book = models.ManyToManyField(books, through='user_action')


class user_action(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    books = models.ForeignKey(books, on_delete=models.CASCADE)
    # 用户自定义类型
    type = models.CharField(max_length=45, null=True)
    # 收藏 或 下载历史
    action = models.CharField(max_length=45)

    class Meta:
        db_table = 'user_action'


class manager(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    # 用户账号、不唯一
    userAccount = models.CharField(max_length=20, unique=True)
    # 密码
    userPasswd = models.CharField(max_length=20)


class upload_books(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=45, null=True)
    website = models.CharField(max_length=200, null=True)
    author = models.CharField(max_length=200, null=True)
    publisher = models.CharField(max_length=200, null=True)
    year = models.CharField(max_length=45, null=True)
    url = models.CharField(max_length=400, null=True)
    cover = models.CharField(max_length=400, null=True)
    status = models.CharField(max_length=45, null=True)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    introduce = models.TextField(null=True)


class series(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    series_name = models.CharField(max_length=255, unique=True)
    cover = models.ImageField(upload_to='series_cover/')


class recommend_books(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    bookname = models.CharField(max_length=255, unique=True)
    isbn = models.CharField(max_length=45, null=True)
    author = models.CharField(max_length=200, null=True)
    introduce = models.TextField(null=True)
    cover = models.ImageField(upload_to='recommend_cover/')
    url = models.ImageField(upload_to='recommend_url/')
    series_id = models.ForeignKey(series, on_delete=models.CASCADE)


class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)