# Generated by Django 4.1.5 on 2023-01-24 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pradech360', '0003_delete_for_partnership_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='For_partnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('c_code', models.IntegerField()),
                ('phone', models.IntegerField()),
                ('contry', models.CharField(max_length=50)),
                ('sent_date', models.DateField(auto_now_add=True)),
                ('city', models.CharField(max_length=50)),
                ('page_url', models.URLField(max_length=240)),
                ('how_you_heared_about_us', models.CharField(max_length=50)),
                ('Industry_type', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]
