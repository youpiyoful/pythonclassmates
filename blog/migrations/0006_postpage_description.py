# Generated by Django 3.1.4 on 2021-01-02 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_postpage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='postpage',
            name='description',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
