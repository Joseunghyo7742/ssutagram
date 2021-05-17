# Generated by Django 3.1.5 on 2021-05-17 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='photos/%m/%d')),
            ],
        ),
    ]
