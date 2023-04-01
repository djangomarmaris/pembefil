from django.shortcuts import render,reverse,redirect ,get_object_or_404

# Create your views here.
from cart.cart import Cart
from shop.models import Category, Product, Rules
from yoga.models import Slider, Blog, About, kvvk

from django.conf import settings
from django.core.mail import send_mail


def index(request):

    done = kvvk.objects.all()

    cart = Cart(request)
    blogs = Blog.objects.all().order_by('-id')
    cate = Category.objects.all()



    saler = Product.objects.filter(available=True,saler='True')

    news = Product.objects.filter(available=True, news='True')

    products = Product.objects.filter(available=True,list='True')

    slider = Slider.objects.all()

    context = {
        'slider':slider,
        'cate':cate,
        'products':products,
        'cart':cart,
        'saler':saler,
        'news':news,
        'blogs':blogs,
        'done':done
    }
    return render(request,'central/index.html',context)




def about(request):
    cart = Cart(request)
    done = kvvk.objects.all()
    abouts = About.objects.all()
    cate = Category.objects.all()
    context = {
        'cart': cart,
        'abouts':abouts,
        'cate':cate,
        'done':done
    }
    return render(request,'central/about.html',context)




def contact(request):
    cart = Cart(request)
    cate = Category.objects.all()
    done = kvvk.objects.all()
    if 'btnSubmit' in request.POST:
        if True:
            name = request.POST.get('name')
            email = request.POST.get('email')
            info = request.POST.get('info')
            sbuject = request.POST.get('subject')
            phone = request.POST.get('phone')
            message = request.POST.get('message')

            subject = 'Costumer Contact Messages'
            from_email = settings.EMAIL_HOST_USER
            to_email = [from_email,"djangomarmaris@gmail.com","info@pembefilyayinevi.com"]
            contact_message = "Name:%s\nEmail:%s\nInfo:%s\nSubject:%s\nPhone:%s\nMessage:%s" % (
                name,
                email,
            info,
            sbuject,
            phone,
            message)
            send_mail(subject, contact_message, from_email, to_email, fail_silently=True)
        return redirect('/')

    context ={
        'cate':cate,
        'cart':cart,
        'done':done
    }

    return render(request,'central/contact.html',context)



def blog_list(request):
    cart = Cart(request)
    blogs = Blog.objects.all().order_by('-id')
    cate = Category.objects.all()
    done = kvvk.objects.all()

    context= {
        'blogs' : blogs,
        'cate':cate,
        'cart':cart,
        'done':done
    }

    return render(request, 'central/blog.html', context)



def blog_detail(request,slug):
    cart = Cart(request)
    blog = Blog.objects.all()
    product = get_object_or_404(Blog,slug=slug)
    done = kvvk.objects.all()
    cate = Category.objects.all()

    context = {
        'product':product,
        'blog':blog,
        'cate':cate,
        'cart':cart,
        'done':done
    }

    return render(request,'central/blog_detail.html',context)




def sss(request):
    cart = Cart(request)
    cate = Category.objects.all()
    rules = Rules.objects.all()
    done = kvvk.objects.all()


    context = {
        'rules':rules,
        'cate':cate,
        'cart':cart,
        'done':done
    }

    return render(request,'central/sss.html',context)