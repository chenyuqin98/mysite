# Generated by Django 3.0.3 on 2020-04-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wx', '0004_auto_20200423_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='recommend_books',
            name='cover',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
        migrations.AlterField(
            model_name='series',
            name='cover',
            field=models.ImageField(null=True, upload_to='photos/'),
        ),
    ]