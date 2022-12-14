# Generated by Django 4.0.5 on 2022-07-04 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_doc', '0002_rename_office_phone_clinic_office_phone1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image_slider',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.CreateModel(
            name='Top_Image_slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_slider_img', models.ImageField(upload_to='img')),
                ('image_slider', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_doc.image_slider')),
            ],
        ),
    ]
