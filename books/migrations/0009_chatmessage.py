# Generated by Django 4.0.5 on 2023-08-11 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_userprofile_alter_book_pdf_alter_book_title_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_message', models.TextField()),
                ('bot_response', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
