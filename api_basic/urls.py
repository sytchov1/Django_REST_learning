from xml.etree.ElementInclude import include
from django.urls import path
from .views import article_list, article, ArticlesAPIView, ArticleAPIView, GenericAPIView, ArticleViewSet, ArticleGenericViewSet, ArticleModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'viewset', ArticleViewSet, basename='article')
router.register(r'viewset/<int:pk>', ArticleViewSet, basename='article')
router.register(r'generic_viewset', ArticleGenericViewSet, basename='article')
router.register(r'generic_viewset/<int:pk>', ArticleGenericViewSet, basename='article')
router.register(r'model_viewset', ArticleModelViewSet, basename='article')
router.register(r'model_viewset/<int:pk>', ArticleModelViewSet, basename='article')


urlpatterns = [
    #path('articles/', article_list),
    path('articles/', ArticlesAPIView.as_view()),
    path('generic/articles/<int:id>/', GenericAPIView.as_view()),
    #path('article/<int:pk>', article),
    path('article/<int:id>', ArticleAPIView.as_view()),
]

urlpatterns += router.urls