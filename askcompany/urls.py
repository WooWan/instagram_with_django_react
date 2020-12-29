
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django_pydenticon.views import image as pydenticon_image

# @login_required
# def root(required):
#     return render(request, 'root.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('identicon/image<path:data>', pydenticon_image, name='pydenticon_image'),
    # as_view라는 메소드는 해당 클래스의 인스턴스를 생성하고 해당 이름을 갖는 views의 메소드를 호출한다!! class기반 함수
    path('', login_required(TemplateView.as_view(template_name='root.html')), name='root')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns+= [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
