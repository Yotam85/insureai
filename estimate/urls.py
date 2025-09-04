# insureai_core/urls.py
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from estimate.views import update_json_by_job

from estimate.views import (
    UploadViewSet, EstimateJobViewSet, EstimateResultViewSet,
    results_mine, results_guest,  # <-- add
)

router = DefaultRouter()
router.register(r'files',   UploadViewSet,         basename='upload')
router.register(r'jobs',    EstimateJobViewSet,    basename='job')
router.register(r'results', EstimateResultViewSet, basename='result')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Put these FIRST so they’re not shadowed by the router:
    path('api/results/mine/',  results_mine,  name='results-mine'),
    path('api/results/guest/', results_guest, name='results-guest'),


    # Router (viewsets)
    path('api/', include(router.urls)),

    # Auth (passwordless)
    path('api/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
c