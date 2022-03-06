from django.urls import path, include


urlpatterns = [
    path('v1/', include('users.urls')),
    path('v1/', include('yamdb.urls')),
    path('v1/', include('reviews.urls')),
]
