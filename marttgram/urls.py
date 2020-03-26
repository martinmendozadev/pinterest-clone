"""marttgram URL Configuration"""

# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Local
from marttgram import views as local_views
from posts import views as posts_views


urlpatterns = [

    path('admin/', admin.site.urls),

    path('hello_word/', local_views.hello_word),
    path('get/', local_views.get),
    path('check_point/<str:name>/<int:age>/', local_views.check_point),

    path('posts/', posts_views.list_posts),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
