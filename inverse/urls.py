"""
URL configuration for inverse project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path, include
from projects.views import ProjectAPIDetailView, ProjectAPIListCreateView, ProjectAPIMyListView, \
    ProjectAPISendInviteView, ProjectAPIConfirmInviteView, ProjectAPIRejectInviteView, ProjectAPIMyInvitesView
from users.views import SkillAPIListCreateView

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Projects
    path('api/projects/', ProjectAPIListCreateView.as_view()),
    path('api/projects/my/', ProjectAPIMyListView.as_view()),
    path('api/projects/<int:pk>/', ProjectAPIDetailView.as_view()),
    path('api/projects/invites/my/', ProjectAPIMyInvitesView.as_view()),
    path('api/projects/<int:project_pk>/invites/send/<int:user_pk>/', ProjectAPISendInviteView.as_view()),
    path('api/projects/<int:pk>/invites/confirm/', ProjectAPIConfirmInviteView.as_view()),
    path('api/projects/<int:pk>/invites/reject/', ProjectAPIRejectInviteView.as_view()),

    # Users
    path('api/users/skills/', SkillAPIListCreateView.as_view()),
    path('api/users/auth/', include('djoser.urls')),
    re_path(r'^api/users/auth/', include('djoser.urls.authtoken'))
]
