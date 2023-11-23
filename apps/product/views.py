from django.db.models import Q
from rest_framework import views, status
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(views.APIView):
    def get(self, request):
        products = []
        response_data = {}
        selected_products = request.session.get('selected_products')
        previous_search = request.session.get('previous_search', [])
        search_term = request.query_params.get("search")
        previous_sort = request.session.get("sort")
        sort = request.query_params.get('sort') or previous_sort

        if selected_products:
            products = Product.objects.filter(id__in=selected_products)
        if search_term:
            search_result = Product.objects.filter(
                Q(name__icontains=search_term) |
                Q(description__icontains=search_term)
            )
            if products:
                products = search_result | products
            else:
                products = search_result
            new_search_result = [product.id for product in products if product]
            request.session["previous_search"] = new_search_result
        elif previous_search:
            previous_products = Product.objects.filter(id__in=previous_search)
            if products:
                products = previous_products | products
            else:
                products = previous_products
        if sort:
            request.session["sort"] = sort
            fld, sign = sort.split("_")
            sort_str = f"-{fld}" if sign == "desc" else fld

            if not isinstance(products, list):
                products = products.order_by(sort_str)

        response_data["results"] = ProductSerializer(products, many=True).data
        response_data["selected"] = selected_products
        return Response(data=response_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        request_data = request.data
        selected_products = request.session.get('selected_products', [])

        if request_data.get("selected"):
            selected_products.append(pk)
        else:
            selected_products.remove(pk)
        request.session["selected_products"] = selected_products
        return Response(selected_products, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
