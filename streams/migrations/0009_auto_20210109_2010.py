# Generated by Django 3.1.4 on 2021-01-09 20:10

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210102_1554'),
        ('streams', '0008_auto_20210109_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_tags', to='blog.postpage'),
        ),
    ]
