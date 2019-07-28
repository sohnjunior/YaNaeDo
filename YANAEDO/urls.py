
from django.contrib import admin
from django.urls import path, include 
import AppMain.urls
import AppPronounce.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AppMain.urls')), # 홈 화면
    path('pronounce/', include('AppPronounce.urls')), # 발음 기호 앱
]
