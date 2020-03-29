from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from . views import HomeView
app_name = 'gforms'
urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    # path('',include('front.urls') ),
    ######################################################################################################
    path('period/', views.periodListView.as_view(), name='products_list'),
    path('period/new/', views.periodCreateView.as_view(), name='products_new'),
    path('period/detail/<int:pk>/', views.periodDetailView.as_view(), name='products_detail'),
    path('period/update/<int:pk>/', views.periodUpdateView.as_view(), name='products_update'),
    
     ######################################################################################################
    path('category/', views.categoryListView.as_view(), name='category_list'),
    path('category/new/', views.categoryCreateView.as_view(), name='category_new'),
    path('category/detail/<int:pk>/', views.categoryDetailView.as_view(), name='category_detail'),
    path('category/update/<int:pk>/', views.categoryUpdateView.as_view(), name='category_update'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)