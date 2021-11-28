from django.db import models


# class Contract(models.Model):
#     pass


class MetaData(models.Model):
    external_url = models.URLField()
    description = models.TextField()
    fee_recipient = models.CharField(max_length=100)
    image = models.URLField()
    name = models.CharField(max_length=100)
    seller_fee_basis_points = models.IntegerField()

    def __str__(self):
        return f"MetaData #{self.pk} {self.name}"


class NFT(models.Model):
    contract = models.CharField(max_length=255)
    chain = models.CharField(max_length=40)
    token_id = models.CharField(max_length=40)
    metadata = models.OneToOneField('MetaData', on_delete=models.CASCADE, null=False, related_name='related_nfts')
    metadata_url = models.CharField(max_length=255)
    file_url = models.FileField()
    cached_file_url = models.FileField()
    mint_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    def __str__(self):
        return f"NFT {self.metadata.name} #{self.contract}"
