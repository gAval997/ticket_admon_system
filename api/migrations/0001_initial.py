# Generated by Django 3.0.6 on 2020-05-10 05:50

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
            name='TicketStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Ticket Statuses',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_opened', models.DateTimeField()),
                ('date_closed', models.DateTimeField(blank=True, null=True)),
                ('ticket_uid', models.CharField(max_length=16)),
                ('title', models.CharField(max_length=500)),
                ('ticket_description', models.CharField(max_length=500)),
                ('solution', models.CharField(blank=True, max_length=500, null=True)),
                ('released_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='ticket_released_user', to=settings.AUTH_USER_MODEL)),
                ('reporting_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ticket_reporting_user', to=settings.AUTH_USER_MODEL)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='ticket_status', to='api.TicketStatus')),
            ],
            options={
                'verbose_name_plural': 'Tickets',
            },
        ),
    ]
