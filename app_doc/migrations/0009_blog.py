# Generated by Django 4.0.5 on 2022-07-04 12:22

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0008_clinic_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, null=True)),
                ('image', models.ImageField(upload_to='img')),
                ('description', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
    ]