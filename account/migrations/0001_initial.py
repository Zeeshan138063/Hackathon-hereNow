# Generated by Django 2.0.3 on 2018-03-16 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('U', 'Unspecified')], default='U', max_length=15)),
                ('address', models.TextField(blank=True, default=None, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True, verbose_name='Contact Number')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('related_users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_related_users', to='account.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('P', 'Primary User'), ('C', 'Connected User')], max_length=50)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users', to='account.UserRole'),
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='taxpayer', to=settings.AUTH_USER_MODEL),
        ),
    ]
