from django.urls import path
from . import views
from main.views import index, blog, posting, new_post 
# for image
from django.conf.urls.static import static
from django.conf import settings

app_name='main'

urlpatterns = [
    # first page
    path('', index, name='index'),
    # URL:80/blog
    path('blog/', blog, name='blog'),
    # URL:80/blog/pk 
    path('blog/<int:pk>',posting, name="posting"),
    # 
    path('blog/new_post/', new_post),

    path('getdata/', views.get_data, name='get_data'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
