# Generated by Django 4.1 on 2022-09-12 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('position', models.IntegerField()),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
                'ordering': ['position'],
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1),
        ),
    ]
