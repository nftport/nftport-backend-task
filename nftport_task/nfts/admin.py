from django.contrib import admin
from nftport_task.nfts import models


@admin.register(models.NFT)
class NFTAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MetaData)
class MetaDataAdmin(admin.ModelAdmin):
    pass
