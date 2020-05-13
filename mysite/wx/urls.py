from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


app_name = 'wx'
urlpatterns = [
    # 用户相关
    path('getdata/', views.wxapp, name='wxapp'),
    path('search/', views.search, name='search'),
    path('search_detail/', views.search_detail, name='search_detail'),
    path('search_recommend_detail/', views.search_recommend_detail, name='search_recommend_detail'),
    path('login/', views.wx_login, name='wx_login'),
    path('regist/', views.wx_regist, name='wx_regist'),
    # 用户行为
    path('add_history/', views.add_history, name='add_history'),
    path('add_favo/', views.add_favo, name='add_favo'),
    path('show_history/', views.show_history, name='show_history'),
    path('show_favo/', views.show_favo, name='show_favo'),
    path('user_upload/', views.user_upload, name='user_upload'),
    path('show_upload/', views.show_upload, name='show_upload'),
    path('add_exp/', views.add_exp, name='add_exp'),
    path('add_scores/', views.add_scores, name='add_scores'),
    path('show_user_info/', views.show_user_info, name='show_user_info'),
    path('show_all_recommend/', views.show_all_recommend, name='show_all_recommend'),
    path('show_all_series/', views.show_all_series, name='show_all_series'),
    path('show_one_recommend/', views.show_one_recommend, name='show_one_recommend'),

    # manager system
    # 管理员网站的界面
    path('manager_login/', views.manager_login, name='manager_login'),
    path('manager_home/', views.manager_home, name='manager_home'),
    path('index/', views.index, name='manage_index'),
    path('upload_books/<int:upload_books_id>/', views.upload_detail, name='upload_detail'),
    path('series/<int:series_id>/', views.series_detail, name='series_detail'),
    path('recommend_books/<int:recommend_books_id>/', views.recommend_detail, name='recommend_detail'),
    # manager action
    path('add_series_detail/', views.add_series_detail, name='add_series_detail'),
    path('add_series/', views.add_series, name='add_series'),
    path('add_recommend_detail/', views.add_recommend_detail, name='add_recommend_detail'),
    path('add_recommend/', views.add_recommend, name='add_recommend'),
    path('delete_this_book/<int:recommend_books_id>/', views.delete_this_book, name='delete_this_book'),
    path('delete_this_series/<int:series_id>/', views.delete_this_series, name='delete_this_series'),
    path('check_and_submit/<int:upload_books_id>/', views.check_and_submit, name='check_and_submit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)