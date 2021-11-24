# Generated by Django 3.2.7 on 2021-11-24 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20211119_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='student',
        ),
        migrations.AlterField(
            model_name='room',
            name='category',
            field=models.CharField(choices=[('single', 'SINGLE'), ('share', 'SHARE')], default='choose', max_length=50),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='student', to='management.profile')),
            ],
        ),
    ]
