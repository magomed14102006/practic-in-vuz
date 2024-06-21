from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('anons', models.CharField(max_length=200, verbose_name='Анонс')),
                ('text', models.TextField(max_length=50000, verbose_name='Текст')),
                ('data', models.DateField(verbose_name='Дата публикации')),
            ],
        ),
    ]
