# Generated by Django 3.1.3 on 2020-11-11 13:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_services_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='icon',
            field=models.CharField(choices=[('bx-bx-briefcase', 'bx-bx-briefcase'), ('bx-bx-brain ', 'bx-bx-brain '), ('bx-bx-book-reader', 'bx-bx-book-reader '), ('bx-bx-briefcase-alt-2', 'bx-bx-briefcase-alt-2'), ('bx-bxs-group ', 'bx-bxs-group')], default=django.utils.timezone.now, max_length=50, verbose_name='Icon'),
            preserve_default=False,
        ),
    ]
