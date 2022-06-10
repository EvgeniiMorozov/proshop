from django.urls import path

from api.views.user_views import (
    MyTokenObtainPairView,
    delete_user,
    get_user_by_id,
    get_user_profile,
    get_users,
    register_user,
    update_user,
    update_user_profile,
)

urlpatterns = [
    path(
        "login/",
        MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("update/<str:pk>/", update_user, name="user-update"),
    path("delete/<str:pk>/", delete_user, name="user-delete"),
    path("profile/update/", update_user_profile, name="users-profile-update"),
    path("register/", register_user, name="register"),
    path("<str:pk>/", get_user_by_id, name="user"),
    path("profile/", get_user_profile, name="users-profile"),
    path("", get_users, name="users"),
]
