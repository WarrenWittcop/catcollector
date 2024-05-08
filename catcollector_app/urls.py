from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    #Cat Pathing
    path('cats/', views.cats_index, name='index'),
    #   in express: cats/:cat_id
    path('cats/<int:cat_id>/', views.cats_detail, name='detail'),
    path('cats/create/', views.Catcreate.as_view(), name='cats_create'),
    path('cats/<int:pk>/update/', views.CatUpdate.as_view(), name='cats_update'),
    path('cats/<int:pk>/delete/', views.CatDelete.as_view(), name='cats_delete'),

    #Feeding pathing
    path('cats/<int:pk>/add_feeding/', views.add_feeding, name='add_feeding'),

    #Toys pathing
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

    # associate a toy with a cat (M:M)
    path('cats/<int:pk>/assoc_toy/<int:toy_pk>/', views.assoc_toy, name='assoc_toy'),
    path('cats/<int:pk>/assoc_delete/<int:toy_pk>', views.assoc_delete, name='assoc_delete'),

    # User auth pathing
    path('accounts/signup', views.signup, name='signup'),
]