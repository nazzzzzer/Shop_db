# Generated by Django 4.0.4 on 2022-04-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(db_index=True, max_length=30)),
                ('slug', models.SlugField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
