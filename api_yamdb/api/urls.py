from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    TitleViewSet,
    CategoriesViewSet,
    GenresViewSet,
    RegisterView,
    ReceivingJWTToken,
    CustomUserViewSet,
    ReviewViewSet,
    CommentViewSet
)

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'titles', TitleViewSet, basename='titles')
router_v1.register('categories', CategoriesViewSet, basename='categories')
router_v1.register('genres', GenresViewSet, basename='genres')
router_v1.register('users', CustomUserViewSet)
router_v1.register(
    r'titles/(?P<title_id>[1-9]\d*)/reviews/(?P<review_id>[1-9]\d*)/comments',
    CommentViewSet,
    basename='comments'
)
router_v1.register(
    r'titles/(?P<title_id>[1-9]\d*)/reviews',
    ReviewViewSet,
    basename='reviews'
)
auth = [
    path('signup/', RegisterView.as_view()),
    path('token/', ReceivingJWTToken.as_view()),
]

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include(auth))
]
