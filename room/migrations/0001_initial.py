# Generated by Django 4.1.3 on 2022-11-04 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(help_text='Slug is a field in autocomplete mode, but if you want you can modify its contents', unique='True', verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]