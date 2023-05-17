from rest_framework.routers import DefaultRouter
from new_app.views import RegistationViewSet,UserViewSet
router=DefaultRouter()
router.register("auth/register",RegistationViewSet,basename="register")
router.register("users",UserViewSet)
urlpatterns=[]
urlpatterns += router.urls
            