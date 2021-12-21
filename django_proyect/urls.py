"""django_proyect URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# importing apps
from apps.portfolio import views
from django.views import generic
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('search-page/', views.search_page, name='search-page'),
    path('search-page-comments/', views.comment_search_page,
         name='search-page-comments'),
    path('about/', generic.TemplateView.as_view(template_name="about.html"), name='about'),
    path('ods/', generic.TemplateView.as_view(template_name="ods.html"), name='ods'),
    path('', views.PostListView.as_view(), name='list'),
    path('create/', views.PostCreateView.as_view(), name='create'),
    path('<slug>/', views.PostDetailView.as_view(), name='detail'),
    path('<slug>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<slug>/delete/', views.PostDeleteView.as_view(), name='delete'),
    path('like/<slug>/', views.like, name='like'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
else:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT, show_indexes=True)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT, show_indexes=True)
