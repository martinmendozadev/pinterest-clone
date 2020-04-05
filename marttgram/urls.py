"""marttgram URL Configuration"""

# Django
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [

    # URLs Admin
    path('admin/', admin.site.urls),

    # URLs Posts
    path('', include(('posts.urls', 'posts'), namespace='posts')),

    # URLs for users
    path('users/', include(('users.urls', 'users'), namespace='users')),
    
] 

if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
