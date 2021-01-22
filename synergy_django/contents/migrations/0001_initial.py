# Generated by Django 3.0.5 on 2021-01-15 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=20)),
                ('publisher', models.CharField(max_length=10)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(blank=True, max_length=30, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book', to='contents.Book')),
            ],
        ),
    ]