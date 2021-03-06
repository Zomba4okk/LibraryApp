# Generated by Django 3.1.7 on 2021-03-02 00:49

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('author', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='BookLendingLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lending_date', models.DateField(default=datetime.datetime.now)),
                ('returning_date', models.DateField(null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='logs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
