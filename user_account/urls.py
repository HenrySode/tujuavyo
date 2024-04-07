from django.urls import path
from . import views

urlpatterns = [
    #User path
    path('users/', views.UserListCreate.as_view(), name='user-create'),
    path('users/<int:pk>', views.UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('login/', views.LoginApiView.as_view(), name='login'),
    
    #Category path
    path('categories/', views.CategoryListCreate.as_view(), name='category-create'),
    
    #Expert path
    path('experts/', views.ExpertListCreate.as_view(), name='experts'),
    path('expert/<int:pk>/', views.ExpertRetrieveUpdateDestroy.as_view(), name='expert-details'),

    #Message path
    path('messages/', views.MessageListCreate.as_view(), name='experts'),
    path('message/<str:pk>/', views.MessageRetrieveUpdateDestroy.as_view(), name='message'),
    
]