# Generated by Django 2.1.5 on 2019-07-02 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=10)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(choices=[('0', 'Select'), ('1', 'New Delhi'), ('2', 'Bihar'), ('3', 'Haryana'), ('4', 'Punjab'), ('6', 'Rajasthan'), ('7', 'Utterpradesh'), ('8', 'Maharashtra'), ('9', 'Kerala'), ('10', 'Jharkhand')], default='Select', max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=False, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=False, related_name='order_items', to='myapp.Product')),
            ],
        ),
    ]
