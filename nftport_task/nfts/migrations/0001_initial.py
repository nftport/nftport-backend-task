# Generated by Django 3.1.13 on 2021-11-28 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MetaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_url', models.URLField()),
                ('description', models.TextField()),
                ('fee_recipient', models.CharField(max_length=100)),
                ('image', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('seller_fee_basis_points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NFT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract', models.CharField(max_length=255)),
                ('chain', models.CharField(max_length=40)),
                ('token_id', models.CharField(max_length=40)),
                ('metadata_url', models.URLField()),
                ('file_url', models.FileField(upload_to='')),
                ('cached_file_url', models.FileField(upload_to='')),
                ('mint_date', models.DateTimeField()),
                ('updated_date', models.DateTimeField()),
                ('metadata', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='related_nfts', to='nfts.metadata')),
            ],
        ),
    ]