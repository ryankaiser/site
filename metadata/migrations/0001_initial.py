# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-28 01:01
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='LocalBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(default='http://schema.org', max_length=200, verbose_name='@context')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('alt_name', models.CharField(blank=True, max_length=200, verbose_name='alternateName')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('url', models.URLField(blank=True, verbose_name='url')),
                ('logo', models.URLField(blank=True, verbose_name='logo')),
                ('founder', models.CharField(max_length=200, verbose_name='founder')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, size=None)),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
        migrations.CreateModel(
            name='PhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(blank=True, max_length=3)),
                ('area_code', models.CharField(max_length=3, validators=[django.core.validators.MinLengthValidator(3)])),
                ('main_digits', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(7)])),
            ],
        ),
        migrations.CreateModel(
            name='PostalAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200, verbose_name='streetAddress')),
                ('locality', models.CharField(max_length=200, verbose_name='addressLocality')),
                ('region', models.CharField(max_length=200, verbose_name='addressRegion')),
                ('postal_code', models.CharField(max_length=200, verbose_name='postalCode')),
            ],
        ),
        migrations.AddField(
            model_name='localbusiness',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.PostalAddress', verbose_name='address'),
        ),
        migrations.AddField(
            model_name='localbusiness',
            name='links',
            field=models.ManyToManyField(to='metadata.Link', verbose_name='sameAs'),
        ),
        migrations.AddField(
            model_name='localbusiness',
            name='telephone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metadata.PhoneNumber'),
        ),
    ]
