from rest_framework import serializers
from nftport_task.nfts import models


class MetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MetaData
        exclude = ('id',)


class NFTSerializer(serializers.ModelSerializer):
    metadata = MetaSerializer()

    class Meta:
        model = models.NFT
