# Generated by Django 5.1.4 on 2024-12-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pclass', models.IntegerField()),
                ('Age', models.FloatField()),
                ('SibSp', models.IntegerField()),
                ('Parch', models.IntegerField()),
                ('Fare', models.FloatField()),
                ('Sex_male', models.BooleanField()),
                ('Embarked_Q', models.BooleanField()),
                ('Embarked_S', models.BooleanField()),
                ('prediction', models.CharField(max_length=20)),
            ],
        ),
    ]
