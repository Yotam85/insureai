# estimate/urls.py  (project-level)
from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from estimate.views import (
    UploadViewSet, EstimateJobViewSet, EstimateResultViewSet,
    results_mine, results_guest, guest_quota,
)

router = DefaultRouter()
router.register(r'files',   UploadViewSet,         basename='upload')
router.register(r'jobs',    EstimateJobViewSet,    basename='job')
router.register(r'results', EstimateResultViewSet, basename='result')


urlpatterns = [
    path('admin/', admin.site.urls),

    # fixed, consistent API prefix
    path('api/guest-quota/', guest_quota, name='guest-quota'),
    path('api/results/mine/',  results_mine,  name='results-mine'),
    path('api/results/guest/', results_guest, name='results-guest'),


    # Router + auth
    path('api/', include(router.urls)),
    path('api/', include('accounts.urls')),
]
