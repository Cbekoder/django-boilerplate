# Generated by Django 5.1.4 on 2025-01-02 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VersionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('version', models.CharField(max_length=64)),
                ('required', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Version history',
                'verbose_name_plural': 'Version histories',
            },
        ),
    ]