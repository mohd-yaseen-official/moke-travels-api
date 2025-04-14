from django.urls import path

from .views import *

urlpatterns = [
    path('', places),
    path('view/<int:pk>', view_place),
    path('protected/<int:pk>', view_protected_place),

    path('categories/', categories),
    
    path('comment/list/<int:pk>', view_comments),
    path('comment/add/<int:pk>', add_comment),

    path('like/list/<int:pk>', view_likes),
    path('like/update/<int:pk>/', update_likes),

    path('reply/add/<int:pk>', add_reply)
]
