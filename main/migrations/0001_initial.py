# Generated by Django 3.1.3 on 2020-11-11 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Industrial_Trainging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_categeory', models.CharField(choices=[('Select', 'Select'), ('Technical', 'Technical'), ('Non Technical', 'Non Technical'), ('Finance', 'Finance'), ('Sap', 'Sap'), ('Ca', 'Ca'), ('Business Development', 'Business Development'), ('others', 'others')], max_length=20)),
                ('image', models.ImageField(upload_to='')),
                ('project', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internship_categeory', models.CharField(choices=[('Select', 'Select'), ('Technical', 'Technical'), ('Non Technical', 'Non Technical'), ('Finance', 'Finance'), ('Sap', 'Sap'), ('Ca', 'Ca'), ('Business Development', 'Business Development'), ('others', 'others')], max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=30)),
                ('work_type', models.CharField(choices=[('Select', 'Select'), ('Fulltime', 'Fulltime'), ('Contract', 'Contract'), ('hourly', 'hourly')], max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_categeory', models.CharField(choices=[('Select', 'Select'), ('Technical', 'Technical'), ('Non Technical', 'Non Technical'), ('Finance', 'Finance'), ('Sap', 'Sap'), ('Ca', 'Ca'), ('Business Development', 'Business Development'), ('others', 'others')], max_length=30)),
                ('jobtitle', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=20)),
                ('vacancycount', models.IntegerField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Seminar_Webinar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('Select', 'Select'), ('Technical', 'Technical'), ('Non Technical', 'Non Technical'), ('Finance', 'Finance'), ('Sap', 'Sap'), ('Ca', 'Ca'), ('Business Development', 'Business Development'), ('others', 'others')], max_length=20)),
                ('topic_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('long', models.BooleanField(default=0)),
                ('lat', models.BooleanField(default=0)),
                ('image', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('Select', 'Select'), ('Technical', 'Technical'), ('Non Technical', 'Non Technical'), ('Finance', 'Finance'), ('Sap', 'Sap'), ('Ca', 'Ca'), ('Business Development', 'Business Development'), ('others', 'others')], max_length=20)),
                ('topic_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(choices=[('Select', 'Select'), ('Technical', 'Technical'), ('Non Technical', 'Non Technical'), ('Finance', 'Finance'), ('Sap', 'Sap'), ('Ca', 'Ca'), ('Business Development', 'Business Development'), ('others', 'others')], max_length=20)),
                ('topic_name', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('long', models.BooleanField(default=0)),
                ('lat', models.BooleanField(default=0)),
                ('image', models.FileField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
