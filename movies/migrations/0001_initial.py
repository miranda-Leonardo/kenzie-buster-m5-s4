# Generated by Django 4.1.7 on 2023-02-27 22:07

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
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=127)),
                ('duration', models.CharField(default=None, max_length=10, null=True)),
                ('rating', models.CharField(choices=[('G', 'G'), ('PG', 'Pg'), ('PG-13', 'Pg 13'), ('R', 'R'), ('NC-17', 'Nc 17')], default='G', max_length=20)),
                ('synopsis', models.CharField(default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='MovieOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyed_at', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_order', to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_order', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='movies',
            field=models.ManyToManyField(related_name='movies_orders', through='movies.MovieOrder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='movie',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie', to=settings.AUTH_USER_MODEL),
        ),
    ]
