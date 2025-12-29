from django.urls import path, include
from .views import (UserProfileListAPIView, UserProfileDetailAPIView, CategoryListAPIView,
                    CategoryDetailAPIView,
                    GenreListAPIView, GenreDetailAPIView,
                    CountryListAPIView,
                    CountryDetailAPIView,
                    DirectorListAPIView, DirectorDetailAPIView,
                    ActorListAPIView, ActorDetailAPIView,
                    MovieListAPIView, MovieDetailAPIView,
                    RatingCreateAPIView,  # ИЗМЕНЕНО
                    ReviewViewSet, ReviewLikeViewSet,
                    FavoriteViewSet, FavoriteItemViewSet, HistoryViewSet,RegisterView,LoginView,LogoutView)
from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'rating', RatingViewSet)  # УБРАНО
router.register(r'review', ReviewViewSet)
router.register(r'review_like', ReviewLikeViewSet)
router.register(r'favorite', FavoriteViewSet)
router.register(r'favorite_item', FavoriteItemViewSet)
router.register(r'history', HistoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryListAPIView.as_view(), name='category_list'),
    path('category/<int:pk>/', CategoryDetailAPIView.as_view(), name='category_detail'),
    path('genre/', GenreListAPIView.as_view(), name='genre_list'),
    path('genre/<int:pk>/', GenreDetailAPIView.as_view(), name='genre_detail'),
    path('movie/', MovieListAPIView.as_view(), name='movie_list'),
    path('movie/<int:pk>/', MovieDetailAPIView.as_view(), name='movie_detail'),
    path('country/', CountryListAPIView.as_view(), name='country_list'),
    path('country/<int:pk>/', CountryDetailAPIView.as_view(), name='country_detail'),
    path('director/', DirectorListAPIView.as_view(), name='director_list'),
    path('director/<int:pk>/', DirectorDetailAPIView.as_view(), name='director_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='userprofile_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='userprofile_detail'),
    path('actor/', ActorListAPIView.as_view(), name='actor_list'),
    path('actor/<int:pk>/', ActorDetailAPIView.as_view(), name='actor_detail'),
    path('rating/', RatingCreateAPIView.as_view(), name='rating_create'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
]