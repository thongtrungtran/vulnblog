# Generated by Django 3.2 on 2021-05-04 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vulnblogapp', '0003_post_post_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='uncategorized', max_length=255),
        ),
    ]