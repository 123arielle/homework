# Generated by Django 3.1.3 on 2020-12-13 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_auto_20201213_0230'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolStu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit_year', models.CharField(max_length=4)),
                ('recruit_num', models.PositiveIntegerField()),
                ('kindergarten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainsite.kindergarten')),
            ],
        ),
    ]
