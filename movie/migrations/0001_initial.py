# Generated by Django 3.2.2 on 2021-05-12 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(blank=True, max_length=45)),
                ('gender', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(null=True)),
            ],
            options={
                'db_table': 'actors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(blank=True, max_length=45)),
                ('gender', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(null=True)),
            ],
            options={
                'db_table': 'directors',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('korean_title', models.CharField(max_length=45)),
                ('english_title', models.CharField(max_length=45)),
                ('country', models.CharField(max_length=45)),
                ('release_date', models.DateField(null=True)),
                ('running_time', models.IntegerField()),
                ('discription', models.TextField(null=True)),
                ('audience_count', models.IntegerField()),
                ('thumbnail_img', models.URLField()),
                ('background_img', models.URLField()),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'providers',
            },
        ),
        migrations.CreateModel(
            name='Movie_Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
                ('provider_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.provider')),
            ],
            options={
                'db_table': 'movies_providers',
            },
        ),
        migrations.CreateModel(
            name='Movie_Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.genre')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
            options={
                'db_table': 'categories_genres',
            },
        ),
        migrations.CreateModel(
            name='Movie_Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.director')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
            options={
                'db_table': 'movies_directors',
            },
        ),
        migrations.CreateModel(
            name='Movie_Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.actor')),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie')),
            ],
            options={
                'db_table': 'movies_actors',
            },
        ),
        migrations.AddField(
            model_name='movie',
            name='actor_id',
            field=models.ManyToManyField(through='movie.Movie_Actor', to='movie.Actor'),
        ),
        migrations.AddField(
            model_name='movie',
            name='category_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.category'),
        ),
        migrations.AddField(
            model_name='movie',
            name='director_id',
            field=models.ManyToManyField(through='movie.Movie_Director', to='movie.Director'),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre_id',
            field=models.ManyToManyField(through='movie.Movie_Genre', to='movie.Genre'),
        ),
        migrations.AddField(
            model_name='movie',
            name='provider_id',
            field=models.ManyToManyField(through='movie.Movie_Provider', to='movie.Provider'),
        ),
    ]
