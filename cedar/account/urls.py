from django.urls import path, re_path

from . import views
app_name = "account"

urlpatterns = [

    re_path(r'^$',
            views.IndexViews.as_view(),
            name='index',),

    re_path(r'^login$',
            views.LoginView.as_view(),
            name='login',),

    re_path(r'^register/$',
            views.RegisterView.as_view(),
            name='register',),

    re_path(r'^user/active/(?P<token>.*)$',
            views.ActiveView.as_view(), name='useractive')
    # path('user/active/<str:token>',views.ActiveView.as_view(),name='useractive'),
]
