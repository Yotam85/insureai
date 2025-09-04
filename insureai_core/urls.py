from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter

from estimate.views import (
    UploadViewSet, EstimateJobViewSet, EstimateResultViewSet, guest_quota, results_mine, results_guest,   # ← add these
)

router = DefaultRouter()
router.register(r'files',   UploadViewSet,         basename='upload')
router.register(r'jobs',    EstimateJobViewSet,    basename='job')
router.register(r'results', EstimateResultViewSet, basename='result')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Put these first
    path("api/guest-quota/", guest_quota, name="guest-quota"),
    path('api/results/mine/',  results_mine,  name='results-mine'),
    path('api/results/guest/', results_guest, name='results-guest'),

    # Then router + auth
    path('api/', include(router.urls)),
    path('api/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
