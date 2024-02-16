import traceback
from django.http import Http404
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
import json

from prime.models import (
    Address,
    Category,
    Store,
    Item
)

from prime.v1.serializers import (
    AddressSerializer,
    CategorySerializer,
    StoreSerializer,
    ItemSerializer,
    StoreDetailSerializer
)


class AddressViewset(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class StoreViewset(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    parser_classes = [MultiPartParser, JSONParser]

    def create(self, request, *args, **kwargs):
        serializer = None
        try:
            data = json.loads(request.data["data"])
            serializer = StoreSerializer(
                data={**data, "image": request.FILES.get("image")}
            ) if request.FILES.get("image") else StoreSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                        serializer.data,
                        status=status.HTTP_201_CREATED
                    )
        except ValidationError:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            return Response(
                    {
                        "error": type(e).__name__,
                        "message": str(e),
                        "at": traceback.format_exc()
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    def retrieve(self, request, *args, **kwargs):
        try:
            store = get_object_or_404(Store, id=kwargs.get("pk"))
            return Response(
                StoreDetailSerializer(store).data,
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                    {"detail": "Store não encontrado"},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception as e:
            return Response(
                    {
                        "error": type(e).__name__,
                        "message": str(e),
                        "at": traceback.format_exc()
                    },
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

    def update(self, request, *args, **kwargs):
        serializer = None
        try:
            data = request.data
            store = get_object_or_404(Store, id=kwargs.get("pk"))
            serializer = StoreSerializer(
                instance=store,
                data=data,
                partial=True
            )

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
        except ValidationError:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Store.DoesNotExist:
            return Response(
                    {"detail": "Store não encontrado"},
                    status=status.HTTP_404_NOT_FOUND
                )
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["PUT"], detail=True)
    def upload_store_image(self, request, *args, **kwargs):
        try:
            store = get_object_or_404(Store, id=kwargs.get("pk"))
            store.image = request.FILES.get("image")
            store.save()
            return Response(
                StoreSerializer(store).data,
                status=status.HTTP_200_OK
            )
        except Http404:
            return Response(
                {"detail": "Store não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {
                        "error": type(e).__name__,
                        "message": str(e),
                        "at": traceback.format_exc()
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class ItemViewset(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    parser_classes = [MultiPartParser, JSONParser]

    def create(self, request, *args, **kwargs):
        serializer = None
        try:
            data = json.loads(request.data["data"])

            serializer = ItemSerializer(
                data={**data, "image": request.FILES.get("image")}
            ) if request.FILES.get("image") else ItemSerializer(data=data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
        except ValidationError:
            return Response(
                serializer.errors,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        # except Exception:
        #     return Response(
        #         {"detail": "Algo deu errado"},
        #         status=status.HTTP_500_INTERNAL_SERVER_ERROR
        #     )

    def update(self, request, *args, **kwargs):
        serializer = None
        try:
            data = request.data
            item = get_object_or_404(Item, id=kwargs.get("pk"))
            serializer = ItemSerializer(
                instance=item,
                data=data,
                partial=True
            )
            
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )
        except ValidationError:
            return Response(
                serializer.errors,
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        except Item.DoesNotExist:
            return Response(
                {"detail": "Item não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )

    @action(methods=["PUT"], detail=True)
    def upload_item_image(self, request, *args, **kwargs):
        try:
            item = get_object_or_404(Item, id=kwargs.get("pk"))
            item.image = request.FILES.get("image")
            item.save()
            return Response(
                ItemSerializer(item).data,
                status=status.HTTP_200_OK
            )
        except Item.DoesNotExist:
            return Response(
                {"detail": "Item não encontrado."},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception:
            return Response(
                {"detail": "Algo deu errado"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
