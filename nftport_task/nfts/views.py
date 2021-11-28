from rest_framework import viewsets, mixins, decorators
from django_filters import rest_framework as filters
from nftport_task.nfts import serializers, models


class NFTFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="metadata__name", lookup_expr='contains')
    contract = filters.CharFilter(field_name="contract", lookup_expr='contains')
    token_id = filters.CharFilter(field_name="token_id")


class NFTViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    Lists and retrieves NFTs
    """
    serializer_class = serializers.NFTSerializer
    queryset = models.NFT.objects.all().select_related("metadata")
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NFTFilter

    @decorators.action(detail=False, description="Reindex and process a new collection")
    def reindex(self, request, *args, **kwargs):
        pass


