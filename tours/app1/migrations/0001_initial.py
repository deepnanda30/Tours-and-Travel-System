# Generated by Django 2.2.10 on 2020-11-02 05:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=255)),
                ('mname', models.CharField(max_length=255)),
                ('lname', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('houseno', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(max_length=255)),
                ('dstate', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tier', models.IntegerField(max_length=1)),
                ('hname', models.CharField(max_length=255)),
                ('street', models.CharField(max_length=255)),
                ('locality', models.CharField(max_length=255)),
                ('d_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Mot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fare', models.FloatField()),
                ('t_type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Roadways',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carname', models.CharField(max_length=30)),
                ('cartype', models.CharField(max_length=20)),
                ('mot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Mot')),
            ],
        ),
        migrations.CreateModel(
            name='Railways',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AC_NAC', models.CharField(max_length=20)),
                ('C_class', models.CharField(max_length=20)),
                ('mot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Mot')),
            ],
        ),
        migrations.CreateModel(
            name='PopularSpots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=255)),
                ('did', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days', models.IntegerField()),
                ('cost', models.FloatField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Destination')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Hotel')),
                ('mot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Mot')),
            ],
        ),
        migrations.CreateModel(
            name='Luxury',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Destination')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnumber', models.IntegerField(max_length=10)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('n_people', models.IntegerField()),
                ('trip_date', models.DateField()),
                ('total', models.FloatField()),
                ('rooms', models.IntegerField()),
                ('payment_mode', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Customer')),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Package')),
            ],
        ),
        migrations.CreateModel(
            name='Airways',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foodAC', models.CharField(max_length=20)),
                ('A_class', models.CharField(max_length=20)),
                ('mot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Mot')),
            ],
        ),
    ]
