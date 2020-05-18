"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ghost.models import PostItem
from ghost import views

admin.site.register(PostItem)
urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.index, name='homepage'),
	path('post/<str:post_id>', views.post, name='post'),
	path('post/upvote/<str:post_id>', views.upvote, name='upvote'),
	path('post/downvote/<str:post_id>', views.downvote, name='downvote'),
	path('addpost/', views.add_post, name='addpost'),
]
