from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home, tour_list, tour_detail, book_tour, register_tour_guide, add_tour
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('tours/', tour_list, name='tour_list'),
    path('tour/<int:tour_id>/', tour_detail, name='tour_detail'),
    path('tour/<int:tour_id>/book/', book_tour, name='book_tour'),
    path('register/tour-guide/', register_tour_guide, name='register_tour_guide'),
    path('add-tour/', add_tour, name='add_tour'),

    # تسجيل الدخول والخروج
    path('login/', auth_views.LoginView.as_view(template_name='tours/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
