"""marttgram URL Configuration"""

# Django
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

# Local
from marttgram import views as local_views
from posts import views as posts_views
from users import views as users_views


urlpatterns = [

    # URLs Admin
    path('admin/', admin.site.urls),

    # URLS Tests
    path('hello_word/', local_views.hello_word, name='hello_word'),
    path('get/', local_views.get, name='get'),
    path('check_point/<str:name>/<int:age>/', local_views.check_point, name='check_pint'),

    # URLs Posts
    path('', posts_views.list_posts, name='feed',),
    path('posts/new/', posts_views.new_post, name='new_post'),

    # URLs for users
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup'),
    path('users/me/update_profile/', users_views.update_profile, name='update_profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
