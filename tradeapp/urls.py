from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path('signup/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('pak-traders/', views.pak_traders_view, name='pak_traders'),
    path('logout/', views.logout_view, name='logout'),
    path('ai-predictor/', views.ai_predictor, name='ai_predictor'),  
    # path('profile/', views.profile_view, name='profile'),
    # path('edit_profile/', views.edit_profile_view, name='edit_profile'),
]