from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import News, Category
from .form import ContactForm
from django.views.generic import TemplateView, ListView

def news_list(request):
    #news_list = News.objects.filter(status = News.Status.Published)
    # yoki 
    news_list = News.published.all()
    context = {
        'news_list':news_list
    }
    return render(request, 'news_app/news_list.html', context=context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        'news': news
    }
    return render(request, 'news_app/news_detail.html', context)

class HomePageView(ListView):
    model = News
    template_name = 'news_app/home.html'
    context_object_name = 'news'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_list'] = News.published.all().order_by('-published_time')[:5]
        context['business_main'] = News.published.filter(category__name = "Business")[0]
        context['business'] = News.published.all().filter(category__name='Business').order_by('-published_time')[1:6]
        context['politic_news'] = News.published.filter(category__name='Politics')[1:6]
        context['politic_main'] = News.published.filter(category__name = 'Politics')[0]
        context['technology'] = News.published.filter(category__name='Technology').order_by('-published_time')[1:6]
        context['technology_main'] = News.published.filter(category__name='Technology')[0]
        context['sport'] = News.published.filter(category__name='Sport').order_by('-published_time')[1:6]
        context['sport_main'] = News.published.filter(category__name='Sport')[0]
        
        return context
    
    
    
class Contact(TemplateView):
    template_name = 'news_app/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news_app/contact.html')
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2>Thank you for contacting us!</h2>")
        context = {
            'form': form
        }
        return render(request, 'news_app/contact.html', context)
    
class PoliticsView(ListView):
    model = News
    template_name = 'news_app/politics.html'
    context_object_name = 'politics_news'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Politics')
        return news
    
class BusinessView(ListView):
    model = News
    template_name = 'news_app/business.html'
    context_object_name = 'business_news'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Business')
        return news
    
class SportView(ListView):
    model = News
    template_name = 'news_app/sport.html'
    context_object_name = 'sport_news'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Sport')
        return news
    
class TechnologyView(ListView):
    model = News
    template_name = 'news_app/technology.html'
    context_object_name = 'technology_news'
    
    def get_queryset(self):
        news = self.model.published.all().filter(category__name='Technology')
        return news
    
    
def page404(request):
    return render(request, 'news_app/404.html')  