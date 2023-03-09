# Generated by Django 4.1.7 on 2023-03-01 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kinopoiskapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='isRecomended',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is recomended'),
        ),
        migrations.AddField(
            model_name='movie',
            name='isTopTen',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Is top ten'),
        ),
    ]