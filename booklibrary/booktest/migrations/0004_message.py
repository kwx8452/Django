# Generated by Django 2.0.3 on 2019-04-29 06:38

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('booktest', '0003_hotpic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('message', tinymce.models.HTMLField()),
            ],
        ),
    ]
