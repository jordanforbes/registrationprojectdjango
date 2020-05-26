# Generated by Django 2.2.4 on 2020-05-26 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0003_auto_20200525_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('favorites', models.ManyToManyField(related_name='items_favorited', to='loginapp.User')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_uploaded', to='loginapp.User')),
            ],
        ),
    ]