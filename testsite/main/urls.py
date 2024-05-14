from django.urls import path, include


from . import views


urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('<int:page>', views.page_num, name='page_num'),
    path('shop/<int:page>/', views.get_page, name='da'),
    path('create', views.create, name='s'),
    path('t/', views.post_test, name='r'),
    path('reg/', views.register, name='reeg'),
    path('login/', views.login_wiev, name='lgin'),
    # path('', include('django.contrib.auth.urls')),
    path('logout/', views.logout_wiew, name='logout'),

    
    # path('click/', views.click, name='main_page')
]


