# Generated by Django 3.2 on 2021-08-01 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slotDate', models.DateField()),
                ('slotStatTime', models.TimeField()),
                ('slotEndTime', models.TimeField()),
                ('bookingType', models.CharField(max_length=300)),
                ('groupSize', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ItemLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loanDate', models.DateTimeField(verbose_name='borrowed_on')),
                ('returnDate', models.DateTimeField(blank=True, null=True, verbose_name='returned_on')),
            ],
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=60)),
                ('surName', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=60)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('bookMachine', models.ManyToManyField(through='fablab.Booking', to='fablab.Machines')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=300, verbose_name='Description')),
                ('quantity', models.IntegerField()),
                ('loans', models.ManyToManyField(through='fablab.ItemLoan', to='fablab.Users')),
            ],
        ),
        migrations.AddField(
            model_name='itemloan',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fablab.users'),
        ),
        migrations.AddField(
            model_name='itemloan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fablab.items'),
        ),
        migrations.AddField(
            model_name='booking',
            name='machine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fablab.machines'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fablab.users'),
        ),
    ]
