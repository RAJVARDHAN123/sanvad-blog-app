from django.urls import path
from .views import (
	post_list,
	post_create,
	post_detail,
	post_delete,
	post_update,
	add_comment_to_post,
	)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:id>/',post_detail, name='post_detail'),
    path('create/',post_create, name='post_create'),
    path('post/<int:id>/delete/',post_delete, name='post_delete'),
    path('post/<int:id>/update/',post_update, name='post_update'),
    path('post/<int:id>/comment/', add_comment_to_post, name='add_comment_to_post'),
]
