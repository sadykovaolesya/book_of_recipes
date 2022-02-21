"""app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings

from book.views import LoginUserView, RecipeCreate, RecipeDetail, RecipeList, RegistrationView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RecipeList.as_view(), name='recipes'),
    path('recipe_create/', login_required(RecipeCreate.as_view()), name='recipe_create'),
    path('recipe/<int:pk>/', RecipeDetail.as_view(), name='recipe'),
    path('accounts/login/', LoginUserView.as_view(), name='login'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('author/<int:id_author>/', RecipeList.as_view(), name='author'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

