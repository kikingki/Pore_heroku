# Generated by Django 3.0.6 on 2021-11-29 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deal_title', models.CharField(max_length=200)),
                ('deal_content', models.TextField()),
                ('deal_date', models.DateTimeField()),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('ready', '미결제'), ('paid', '결제완료')], db_index=True, default='ready', max_length=9)),
                ('deal_buyer', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_title', models.CharField(max_length=200)),
                ('pf_content', models.TextField()),
                ('pf_attach', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('pf_date', models.DateTimeField()),
            ],
        ),
    ]
