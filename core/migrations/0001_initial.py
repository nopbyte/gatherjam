# Generated by Django 4.2 on 2023-04-26 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('email', models.CharField(max_length=320)),
                ('public_key', models.CharField(max_length=3000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VendorCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VendorPromotion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('enabled', models.BooleanField()),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('points_required', models.IntegerField()),
                ('expiration_date', models.DateTimeField(default=None)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendorcategory')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VendorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendorcategory')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VendorPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('path', models.CharField(max_length=4096)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendorprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PromotionPicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('path', models.CharField(max_length=4096)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendorpromotion')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NFCTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('serial', models.CharField(max_length=200)),
                ('current_value', models.CharField(max_length=1000)),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.vendor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
