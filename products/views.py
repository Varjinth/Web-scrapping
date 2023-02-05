from django.shortcuts import render,redirect
from bs4 import BeautifulSoup
import requests
from .models import Product, Category
from .forms import MyForm
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from selenium import webdriver
from django.utils import timezone
from datetime import timedelta
from django.views.generic import ListView, DetailView


def scrape_data(url):

    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    unknown=0
    try:
       title = soup.find('span', class_="G6XhRU").text
    except:
        title="unknown"
        unknown+=1
    try:
        description = soup.find("span", class_="B_NuCI").text
    except:
        description="unknown"
        unknown+=1
    try:
       price = soup.find("div" ,class_="_30jeq3 _16Jk6d").text
       price = str(price).split('₹')[1]
    except:
        price="unknown"
        unknown+=1
    try:
       category_name = soup.find_all('a', {'class': '_2whKao'})[1].text
    except:
        category_name="others"
        unknown+=1
    try:
       img = soup.find_all('img', {'class': 'q6DClP'})[1]['src']  
    except:
        img='https://www.idealstandard.lt/-/media/project/ideal-standard/commerce-websites/shared-website/default-fallback-images/product-tile/product_image_placeholder.jpg'
    try:
        size = soup.find('a', class_='_1fGeJ5').text
    except:
        size= 'unknown'
        unknown+=1
    

    category, created = Category.objects.update_or_create(category=category_name,defaults={"category":category_name})
    category.save()    

    product, created = Product.objects.update_or_create(
        url=url,
        defaults={
            'title': title,
            'description': description,
            'price': price,
            'size': size,
            'image': img,
            'category': category
            
        }
    )
    product.save()
    

    
    

    return product, category, unknown


def my_view(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                product=Product.objects.get(url=url)
                if ((timezone.now() - product.scraped_at) > timedelta(days=3)) :
                    product, category, unknown = scrape_data(url)
                    content={'product':product}
                    return render(request, "display.html", content)
                else:
                    content={'product':product}
                    return render(request, "display.html", content)

            except Product.DoesNotExist:
                product, category, unknown = scrape_data(url)
                if unknown>3:
                    Product.objects.filter(url=product.url).delete()
                    return render(request,"NA.html")
                else:
                    content={'product':product}
                    return render(request, "display.html", content)
            
            
 
            
    else:
        form = MyForm()
        return render(request, 'home.html', {'form': form})


class UrlListView(ListView):
    model= Product
    template_name= "URLs.html"
    context_object_name= "products"
    ordering= ['scraped_at']


class UrlDetailView(DetailView):
    model=Product
    template_name="display.html"
    context_object_name= "product"