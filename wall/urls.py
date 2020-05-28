from django.urls import path, include 
from . import views as wall
from loginapp import views as loginviews


urlpatterns = [
    path('', wall.home),
    path('loginpage', loginviews.index),
    path('logoutpage', wall.newlogout),
    path('<user_id>/create_post', wall.addPost),
    path('<post_id>/delete_post', wall.deletePost),
    path('<post_id>/create_comment', wall.addComment),
    path('<comment_id>/delete_comment', wall.deleteComment)
]