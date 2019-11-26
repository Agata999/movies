# Generated by Django 2.2.7 on 2019-11-26 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20191125_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genre',
            field=models.PositiveSmallIntegerField(choices=[(2, 'thriller'), (3, 'drama'), (4, 'horror'), (0, 'undefined'), (5, 'sci-fi'), (1, 'comedy')]),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('stars', models.PositiveSmallIntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.Movie')),
            ],
        ),
    ]