from .models import (UserProfile, Category, Genre, Country, Director,
                     Actor, Movie, MovieVideo, MovieFrame, Rating, Review,
                     ReviewLike, Favorite, FavoriteItem, History)
from rest_framework import serializers


class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','user_photo','username','status']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    date_registered = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name','username','email','age',
                  'phone_number','user_photo','status','date_registered']


class UserProfileNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name','last_name']

class UserProfileReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username','user_photo']

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','category_name']

class GenreNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']

class CategoryDetailSerializer(serializers.ModelSerializer):
    genres = GenreNameSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['category_name','genres']


class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id','genre_name']

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['id','country_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']

class MovieListSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%d-%m-%Y')
    country = CountrySerializer(many=True)
    genre = GenreNameSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id','movie_poster','movie_name','year',
                  'country','genre','movie_status']


class CountryDetailSerializer(serializers.ModelSerializer):
    country = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Country
        fields = ['id', 'country_name','country']

class GenreDetailSerializer(serializers.ModelSerializer):
    genres_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['genres_movies','id']

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['full_name']

class DirectorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['id','full_name']


class DirectorDetailSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format='%d-%m-%Y')
    director_movies = MovieListSerializer(many=True,read_only=True)
    class Meta:
        model = Director
        fields = ['full_name','director_photo','bio','birth_date','director_movies']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['full_name']

class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id','full_name']


class ActorDetailSerializer(serializers.ModelSerializer):
    birth_date = serializers.DateField(format='%d-%m-%Y')
    actor_movies = MovieListSerializer(many=True, read_only=True)
    class Meta:
        model = Actor
        fields = ['full_name','actor_photo','birth_date','bio','actor_movies']

class MovieVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieVideo
        fields = ['video_name','video']


class MovieFrameSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFrame
        fields = ['image']


class RatingSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y-%H-%M')
    user = UserProfileNameSerializer()
    class Meta:
        model = Rating
        fields = ['user', 'stars', 'created_date']


class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['movie', 'stars','user']


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d-%m-%Y-%H-%M')  # ИСПРАВЛЕНО: created_at → created_date
    user = UserProfileReviewSerializer()

    class Meta:
        model = Review
        fields = ['user', 'comment', 'parent', 'created_date']  # ИСПРАВЛЕНО: created_at → created_date


class MovieDetailSerializer(serializers.ModelSerializer):
    year = serializers.DateField(format='%d-%m-%Y')
    country = CountrySerializer(many=True)
    director = DirectorSerializer(many=True)
    genre = GenreNameSerializer(many=True)
    actor = ActorListSerializer(many=True)
    videos = MovieVideoSerializer(many=True,read_only=True)
    frames = MovieFrameSerializer(many=True,read_only=True)
    ratings = RatingSerializer(many=True,read_only=True)
    reviews = ReviewSerializer(many=True,read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()
    class Meta:
        model = Movie
        fields = ['movie_name','year','genre','director',
                  'country','slogan','actor','movie_status','description',
                  'trailer','movie_poster','movie_type','movie_time',
                  'videos','avg_rating','frames','count_rating','ratings','reviews']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()

    def get_count_rating(self, obj):
        return obj.get_count_rating()


class ReviewLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLike
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItem
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'