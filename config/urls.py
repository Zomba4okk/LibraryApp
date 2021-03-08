from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='books/list'), name='main_page'),
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
    path('books/', include('apps.books.urls'))
]
