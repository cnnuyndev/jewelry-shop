from .models import Category, Cart, Like


def store_menu(request):
    categories = Category.objects.filter(is_active=True)
    context = {
        'categories_menu': categories,
    }
    return context

def cart_menu(request):
    if request.user.is_authenticated:
        cart_items= Cart.objects.filter(user=request.user)
        context = {
            'cart_items': cart_items,
        }
    else:
        context = {}
    return context
def like_item(request):
    if request.user.is_authenticated:
        like_item= Like.objects.filter(user=request.user)
        context = {
            'like_item': like_item,
        }
    else:
        context = {}
    return context