# Generated by Django 3.0.8 on 2020-07-14 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('department', '0001_initial'),
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average_pay', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='department.Department')),
                ('lead', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team_lead', to='employees.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeInTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='team', to='employees.Employee')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employee', to='teams.Team')),
            ],
        ),
    ]
