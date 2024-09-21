from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import login_required

from .models import News
from .forms import NewsForm


@login_required(login_url="/authentication/login/")
def my_news(request):
    current_user = request.user
    news = News.objects.filter(user = current_user)
    return render(request, "news/my_news.html", context={"news": news})


def news_home(request):
    news = News.objects.all()
    return render(request, "news/news.html", context={"news":news})


@login_required(login_url="/authentication/login/")
def add_news(request):
    form = NewsForm
    err = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        current_user = request.user

        if form.is_valid():
            new = form.save(commit=False)
            new.user = current_user

            new.save()
            
            return redirect(to='news_home')
        else:
            err = 'error'
        
    return render(request, "news/add_news.html", context={"form":form, "error":err})


# class NewsDetailView(DetailView):
#     model = News
#     template_name = "news/news_detail.html"
#     context_object_name = 'news'



class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = 'news'

    def get(self, request, *args, **kwargs):
        # Ваше дополнительное действие
        print("Новость была просмотрена!")
        
        last_news_id = request.get_full_path().split("/")[-1]
        
        current_user = request.user
        current_user.first_name = "Serhii"
        current_user.last_news_id = last_news_id
        current_user.save()
        
        # Вызов стандартного метода get для дальнейшей обработки
        return super().get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     # Получаем контекст из родительского класса
    #     context = super().get_context_data(**kwargs)
    #     # Ваше дополнительное действие
    #     print("Контекст был подготовлен!")
    #     # Возвращаем контекст
    #     return context


class NewsUpdateView(UpdateView):
    model = News
    template_name = "news/add_news.html"
    form_class = NewsForm

