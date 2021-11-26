from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Product, Provider
from .serializers import CategorySerializer, ProductSerializer, ProviderSerializer


class ProductListCreate(APIView):

    def get(self, request):
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        product_serializer = ProductSerializer(data=request.data, many=False)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({
                'msg': 'Error al enviar datos al registrar producto',
                'error(es)': product_serializer.errors,
            }, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteUpdate(APIView):

    def get(self, request, id):
        product = Product.objects.all().filter(pk=id).first()
        if product:
            product_serializer = ProductSerializer(product, many=False)
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'Producto no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        product = Product.objects.all().filter(pk=id).first()
        if product:
            product_serializer = ProductSerializer(product, request.data)
            product_serializer.is_valid(raise_exception=True)
            product_serializer.save()
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'Producto no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = Product.objects.all().filter(pk=id).first()
        if product:
            product.status_delete = True
            return Response({'msg': 'Producto eliminado'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Producto no encontrado'}, status=status.HTTP_400_BAD_REQUEST)


class ProviderListCreate(APIView):

    def get(self, request):
        providers = Provider.objects.all()
        providers_serializer = ProviderSerializer(providers, many=True)
        return Response(providers_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        provider_serializer = ProviderSerializer(data=request.data, many=False)
        if provider_serializer.is_valid():
            provider_serializer.save()
            return Response(provider_serializer.data, status=status.HTTP_200_OK)
        return Response({
            'msg': 'Error al enviar datos al registrar proveedor',
            'error(es)': provider_serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class ProviderDeleteUpdate(APIView):

    def get(self, request, id):
        provider = Provider.objects.all().filter(pk=id).first()
        if provider:
            provider_serializer = ProviderSerializer(provider, many=False)
            return Response(provider_serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'Proveedor no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        provider = Provider.objects.all().filter(pk=id).first()
        if provider:
            provider_serializer = ProviderSerializer(provider, request.data)
            provider_serializer.is_valid(raise_exception=True)
            provider_serializer.save()
            return Response(provider_serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'Proveedor no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        provider = Provider.objects.all().filter(pk=id).first()
        if provider:
            provider.status_delete = True
            provider.save()
            return Response({'msg': 'Proveedor eliminado'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Proveedor no encontrado'}, status=status.HTTP_400_BAD_REQUEST)


class CategoryListCreate(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        category_serializer = CategorySerializer(data=request.data, many=False)
        if category_serializer.is_valid():
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_200_OK)
        return Response({
            'msg': 'Error al enviar datos al registrar categoria',
            'error(es)': category_serializer.errors,
        }, status=status.HTTP_400_BAD_REQUEST)


class CategoryDeleteUpdate(APIView):

    def get(self, request, pk):
        category = Category.objects.all().filter(pk=pk).first()
        if category:
            category_serializer = CategorySerializer(category, many=False)
            return Response(category_serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'Categoria no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        category = Category.objects.all().filter(pk=pk).first()
        if category:
            category_serializer = CategorySerializer(category, request.data)
            category_serializer.is_valid(raise_exception=True)
            category_serializer.save()
            return Response(category_serializer.data, status=status.HTTP_200_OK)
        return Response({'msg': 'Categoria no encontrada'}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = Category.objects.all().filter(pk=pk).first()
        if category:
            category.status_delete = True
            category.save()
            return Response({'msg': 'Categoria eliminada'}, status=status.HTTP_200_OK)
        return Response({'msg': 'Categoria no encontrada'}, status=status.HTTP_400_BAD_REQUEST)
