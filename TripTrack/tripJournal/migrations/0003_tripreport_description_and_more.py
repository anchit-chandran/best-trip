# Generated by Django 4.2.1 on 2023-05-13 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripJournal', '0002_remove_tripreport_date_of_trip_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripreport',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='Any thoughts?'),
        ),
        migrations.AlterField(
            model_name='tripreport',
            name='datetime_of_trip',
            field=models.DateTimeField(null=True, verbose_name='Date & time'),
        ),
        migrations.AlterField(
            model_name='tripreport',
            name='dosage',
            field=models.IntegerField(verbose_name='Amount'),
        ),
        migrations.AlterField(
            model_name='tripreport',
            name='dosage_units',
            field=models.CharField(default='mg', max_length=20, verbose_name='Units'),
        ),
        migrations.AlterField(
            model_name='tripreport',
            name='location',
            field=models.CharField(max_length=100, verbose_name='Where you were'),
        ),
        migrations.AlterField(
            model_name='tripreport',
            name='substance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tripJournal.substance', verbose_name='What you took'),
        ),
    ]