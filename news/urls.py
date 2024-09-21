from django.urls import path
from news.views import news_home, add_news, NewsDetailView, NewsUpdateView, my_news

urlpatterns = [
    path('', news_home, name="news_home"),
    path('addNews', add_news, name="add_news"),
    path('<int:pk>', NewsDetailView.as_view(), name="news_detail"),
    path('<int:pk>/update', NewsUpdateView.as_view(), name="news_update"),
    path("my_news", my_news, name="my_news")
]
