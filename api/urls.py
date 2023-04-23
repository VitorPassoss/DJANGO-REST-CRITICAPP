from django.urls import path
from .views import (FilmView,FilmDetail,UserRegistrationAPIView,Reviews,ReviewDelete,ReviewDetail,CustomTokenObtainPairView,GetUserByToken)


urlpatterns = [
    path('', Reviews.as_view(), name="home-review"),
    path('reviews/delete/<int:id>', ReviewDelete.as_view(), name="delete-review"),
    path('reviews/details/<int:id>', ReviewDetail.as_view(), name="details-review"),
    path('films/', FilmView.as_view(), name='films-view'),
    path('films/details/<int:id>', FilmDetail.as_view(), name='books-details'),
    path('register/', UserRegistrationAPIView.as_view(), name='user-registration'),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('userinfo/', GetUserByToken.as_view(),name="user_by_token")
]