# Generated by Django 4.1.4 on 2023-01-03 20:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('business_type', models.CharField(choices=[('Y', 'Yoga'), ('G', 'Gym'), ('C', 'Chiropractor'), ('R', 'Resturant'), ('S', 'Shop'), ('A', 'Acupuncture'), ('M', 'Massage')], default='Y', max_length=1)),
                ('business_hours', models.CharField(choices=[('1', '24 hours a day'), ('2', 'Hours to be determined'), ('3', 'Contact business for more information'), ('4', '8am - 5pm'), ('5', '8am - 10pm'), ('6', '6am - 10pm'), ('7', '12pm - 12am'), ('8', '9am - 6pm'), ('9', 'Closed for the Holidays')], default='1', max_length=1)),
                ('rates', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('specialty', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=250)),
                ('availability', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='GroupClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(verbose_name='Group Class Date')),
                ('description', models.TextField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.CharField(choices=[('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')], default='5', max_length=1)),
                ('comment', models.CharField(max_length=500)),
                ('groupclass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.groupclass')),
            ],
        ),
    ]
