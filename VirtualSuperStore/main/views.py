from django.shortcuts import render
from django.views.generic import DetailView, View
from .models import EarphonesProduct, SpeakersProduct, Category, LatestProducts
from .mixins import CategoryDetailMixin

class BaseView(View):
    def get(self,request,*args,**kwargs):
        categories = Category.objects.get_categories_for_sidebar()
        products= LatestProducts.objects.get_products_for_main_page(
            'earphonesproduct', 'speakersproduct', with_respect_to='speakersproduct')
        context = {
            'categories':categories,
            'products': products
        }
        return render(request, 'base.html', context)


# def test_view(request):
#     categories = Category.objects.get_categories_for_sidebar()
#     return render(request, 'base.html', {'categories':categories})



class ProductDetailView(CategoryDetailMixin, DetailView):

    CT_MODEL_MODEL_CLASS = {
        'earphonesproduct': EarphonesProduct,
        'speakersproduct': SpeakersProduct,
    }

    def dispatch(self, request, *args, **kwargs):
        self.model = self.CT_MODEL_MODEL_CLASS[kwargs['ct_model']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)

    # model = Model
    # queryset = Model.object.all()
    context_object_name = 'product'
    template_name = 'product_detail.html'
    slug_url_kwarg = 'slug'


class CategoryDetailView(CategoryDetailMixin, DetailView):
    model = Category
    queryset = Category.objects.all()
    context_object_name = 'category'
    template_name = 'category_detail.html'
    slug_url_kwarg = 'slug'