# Generated by Django 2.0.3 on 2019-04-28 02:32

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.IntegerField()),
                ('bname', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('publish_date', models.DateField()),
                ('publisher', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='BorrowMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrow_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField()),
                ('status', models.BooleanField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.Book')),
            ],
        ),
        migrations.CreateModel(
            name='StudentUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('college', models.CharField(max_length=20)),
                ('studentnum', models.IntegerField()),
                ('psw', models.IntegerField()),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='borrowmessage',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booktest.StudentUser'),
        ),
    ]
