# Generated by Django 3.0.5 on 2021-01-15 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_content_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='footnote',
            field=models.TextField(blank=True, null=True),
        ),
    ]