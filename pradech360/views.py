from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from .models import Blog, For_creatives, For_partnership
from django.views.generic.base import TemplateView


# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get('subject')

        email = EmailMessage(
            subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=[settings.EMAIL_HOST_USER],
            reply_to=[email]
        )
        email.send()
        messages.add_message(request, messages.SUCCESS, f"Thanks {name} for reaching out to pradech360")
        return HttpResponseRedirect(request.path)
    
    return render(request, 'index.html')

def forms(request):
   return render(request, 'forms.html')


class Creatives(TemplateView):
        template_name = 'creatives.html'
        def post(self, request):
            if request.method == 'POST':
                f_name = request.POST.get('first-name')
                l_name = request.POST.get('last-name')
                prof_name = request.POST.get('Professional-name')
                website = request.POST.get('Website')
                _email = request.POST.get('email-creatives')
                c_code = request.POST.get('countryCode')
                _phone = request.POST.get('phone')
                contry = request.POST.get('country')
                city = request.POST.get('city')
                page_url = request.POST.get('page')
                user_type = request.POST.get('user-type')
                prim_obj = request.POST.get('objective')
                how_you_heared_about_us = request.POST.get('How')
                campaign_brief = request.POST.get('message')
                budget = request.POST.get('budget')

                creatives = For_creatives(first_name=f_name, 
                                            last_name=l_name, 
                                            _prof_name=prof_name, 
                                            email=_email, 
                                            website_url=website, 
                                            country_code=c_code, 
                                            phone = _phone,
                                            country=contry, 
                                            _city=city, 
                                            _page_url=page_url, 
                                            _user_Type=user_type, 
                                            _obj=prim_obj, 
                                            _how_you_heared_about_us=how_you_heared_about_us, 
                                            campaign=campaign_brief, 
                                            _industry_type=budget
                                        )
                creatives.save()
                messages.add_message(request, messages.SUCCESS, f"Thanks {f_name} for reaching out to pradech360")
            return HttpResponseRedirect(request.path)

class Partnerships(TemplateView):
    template_name = 'partnership.html'
    def post(self, request):
        if request.method == 'POST':
            f_name = request.POST['first-name']
            l_name = request.POST['last-name']
            website = request.POST['Website']
            email = request.POST['email']
            c_code = request.POST['countryCode']
            contry = request.POST['country']
            city = request.POST['city']
            page_url = request.POST['page']
            user_type = request.POST['user-type']
            how_you_heared_about_us = request.POST['How']
            Industry_type = request.POST['budget']

            partnership = For_partnership(first_name=f_name, 
                                      last_name=l_name, 
                                      _email=email, 
                                      website_url=website, 
                                      country_code=c_code, 
                                      country=contry, 
                                      _city=city, 
                                      _page_url=page_url, 
                                      _user_Type=user_type, 
                                      _how_you_heared_about_us=how_you_heared_about_us,  
                                      _Industry_type=Industry_type )

            partnership.save()

def blog(request):
    return render(request, 'blog.html')

def blog_entry(request):
    if request.method == 'POST':
        title = request.POST['blog_title']
        article = request.POST['article']
        image = request.POST['Blog_image']
        

        new_blog = Blog(blog_title=title, blog_article=article, Blog_image=image)
        new_blog.save()

    return render(request, 'blog-entry.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def inner_page(request):
    return render(request, 'inner-page.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

    