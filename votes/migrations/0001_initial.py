# Generated by Django 4.0.2 on 2022-02-26 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Points_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_name', models.CharField(max_length=20)),
                ('get_point', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Competitions_M',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts_at', models.DateField()),
                ('ends_at', models.DateField()),
                ('point_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='votes.points_m')),
            ],
        ),
    ]