# Generated by Django 3.2 on 2023-04-24 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='habit',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.CreateModel(
            name='UsersHabit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.habit')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
