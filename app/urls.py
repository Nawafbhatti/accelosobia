from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('career/', views.career, name="career"),
    path('about/', views.about, name='about'),
    path('work/', views.our_work, name='work'),
    path('partnership/', views.partnership, name='partnership'),
    path('privacypolicy/', views.privacy_policy, name='privacypolicy'),
    path('whoweare/', views.who_we_are, name='whoweare'),
    path('test/', views.test, name='test'),
    path('partnership2/', views.partnership2, name='partnership2'),

]