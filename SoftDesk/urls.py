from email.mime import base
from django.contrib import admin
from django.urls import path,include
from rest_framework_nested import routers
from project import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()
router.register("projects",views.projects,basename="projects")
router.register("signup",views.signup,basename="signup")

first_depth_router = routers.NestedSimpleRouter(router,r"projects",lookup="project")
first_depth_router.register(r"users",views.contributors,basename="project-users")
first_depth_router.register(r"issues",views.issues,basename="project-issues")

second_depth_router = routers.NestedSimpleRouter(first_depth_router,r"issues",lookup="issue")
second_depth_router.register(r"comments",views.comments,basename="issue-comments")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(router.urls)),
    path("",include(first_depth_router.urls)),
    path("",include(second_depth_router.urls)),
    path("login/", TokenObtainPairView.as_view(),name="get_token"),
    # path("token/refresh", TokenRefreshView.as_view(),name="refresh_token"),

]
