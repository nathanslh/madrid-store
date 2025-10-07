from django.shortcuts import render, redirect, get_object_or_404
from main.models import Product
from main.forms import ProductForm
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get('filter', 'all')

    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'name': 'Natan Harum Panogu Silalahi',
        'npm' : '2406496170',
        'class': 'PBP E',
        'products': product_list,
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        forms_entry = form.save(commit = False)
        forms_entry.user = request.user
        forms_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
     product_list = Product.objects.all()
     xml_data = serializers.serialize("xml", product_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    product_list = Product.objects.select_related('user').all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user.id,
            'user_username': product.user.username if product.user else 'Anonymous'
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'created_at': product.created_at.isoformat() if product.created_at else None,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        # Handle AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                return JsonResponse({
                    'success': True,
                    'username': user.username,
                    'redirect_url': reverse('main:login_user')
                })
            else:
                return JsonResponse({
                    'success': False,
                    'errors': form.errors
                })
        
        # Handle regular form submission
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login_user')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      # Handle AJAX request
      if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
          form = AuthenticationForm(data=request.POST)
          if form.is_valid():
              user = form.get_user()
              login(request, user)
              return JsonResponse({
                  'success': True,
                  'username': user.username,
                  'redirect_url': reverse("main:show_main")
              })
          else:
              return JsonResponse({
                  'success': False,
                  'errors': form.errors
              })
      
      # Handle regular form submission
      form = AuthenticationForm(data=request.POST)
      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # Handle AJAX logout
        logout(request)
        return JsonResponse({'success': True, 'message': 'Logged out successfully'})
    
    # Handle regular logout
    logout(request)
    response = HttpResponseRedirect(reverse('main:login_user'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

@csrf_exempt
@login_required(login_url='/login')
def edit_product_ajax(request, id):
    if request.method == 'POST':
        try:
            product = get_object_or_404(Product, pk=id, user=request.user)
            
            # Update product fields
            product.name = strip_tags(request.POST.get("name"))
            product.price = int(request.POST.get("price")) if request.POST.get("price") else 0
            product.description = strip_tags(request.POST.get("description"))
            product.category = request.POST.get("category")
            product.thumbnail = request.POST.get("thumbnail")
            product.is_featured = request.POST.get("is_featured") == 'on'
            
            product.save()

            return JsonResponse({
                'success': True,
                'message': 'Product updated successfully!',
                'product': {
                    'id': str(product.id),
                    'name': product.name,
                    'price': product.price,
                    'description': product.description,
                    'category': product.category,
                    'thumbnail': product.thumbnail,
                    'is_featured': product.is_featured
                }
            })
        except Product.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Product not found or you do not have permission to edit it.'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error updating product: {str(e)}'
            }, status=400)
    
    return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@login_required(login_url='/login')
def delete_product_ajax(request, id):
    if request.method == 'DELETE':
        try:
            product = get_object_or_404(Product, pk=id, user=request.user)
            product_name = product.name
            product.delete()
            
            return JsonResponse({
                'success': True,
                'message': f'Product "{product_name}" deleted successfully!'
            })
        except Product.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Product not found or you do not have permission to delete it.'
            }, status=404)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error deleting product: {str(e)}'
            }, status=400)
    
    return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)

@csrf_exempt
@login_required(login_url='/login')
def create_product_ajax(request):
    if request.method == 'POST':
        try:
            name = strip_tags(request.POST.get("name"))  # strip HTML tags!
            price = request.POST.get("price")
            description = strip_tags(request.POST.get("description"))  # strip HTML tags!
            category = request.POST.get("category")
            thumbnail = request.POST.get("thumbnail")
            is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
            user = request.user

            new_product = Product(
                name=name,
                price=int(price) if price else 0,
                description=description,
                category=category,
                thumbnail=thumbnail,
                is_featured=is_featured,
                user=user
            )
            new_product.save()

            return JsonResponse({
                'success': True,
                'message': 'Product created successfully!',
                'product': {
                    'id': str(new_product.id),
                    'name': new_product.name,
                    'price': new_product.price,
                    'description': new_product.description,
                    'category': new_product.category,
                    'thumbnail': new_product.thumbnail,
                    'is_featured': new_product.is_featured
                }
            }, status=201)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': f'Error creating product: {str(e)}'
            }, status=400)
    
    return JsonResponse({'success': False, 'message': 'Method not allowed'}, status=405)