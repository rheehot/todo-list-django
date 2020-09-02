# Generated by Django 3.1 on 2020-09-02 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0005_auto_20200902_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_type', models.CharField(max_length=50, verbose_name='우선순위')),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='todolist.priority'),
        ),
    ]
