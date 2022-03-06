"""neftgazproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path


from django.conf import settings
from django.conf.urls.static import static




from rest_framework.routers import DefaultRouter
from rest_framework.decorators import api_view


from api.views import *



router = DefaultRouter()


router.register(r'advertisement', AdvertisementViews)
router.register(r'news', NewsViews)
router.register(r'accountant', AccountantsViews)
router.register(r'tenders', TendersViews)
router.register(r'noun', NounsViews)

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'advertisement':'https://neft-gaz.api.abrorjonaxmadov.uz/advertisement/',
#         'news':'https://neft-gaz.api.abrorjonaxmadov.uz/news/',
#         'accountant':'https://neft-gaz.api.abrorjonaxmadov.uz/accountant/',
#         'tenders':'https://neft-gaz.api.abrorjonaxmadov.uz/tenders/',
#         'noun':'https://neft-gaz.api.abrorjonaxmadov.uz/noun/',
#     })

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', api_root, name='api_root'),
    # # path('add/<int:pk>', AdvertisementViews.as_view(), name="addvertisements-detail"),

    # path('advertisement/', AdvertisementViews.as_view(), name="addvertisements"),
    # path(r'advertisement/<int:pk>/', AdvertisementsDetailView.as_view(), name="addvertisements-detail"),

    # path('news/', NewsViews.as_view(), name="news"),
    # path(r'news/<int:pk>/', NewsDetailView.as_view(), name="addvertisements-detail"),

    # path('accountant/', AccountantsViews.as_view(), name="addvertisements"),
    # path(r'accountant/<int:pk>/', AccountantsDetailView.as_view(), name="addvertisements-detail"),

    # path('tenders/', TendersViews.as_view(), name="addvertisements"),
    # path(r'tenders/<int:pk>/', TendersDetailView.as_view(), name="addvertisements-detail"),

    # path('noun/', NounsViews.as_view(), name="addvertisements"),
    # path(r'noun/<int:pk>/', NounsDetailView.as_view(), name="addvertisements-detail"),




]

urlpatterns += router.urls

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)