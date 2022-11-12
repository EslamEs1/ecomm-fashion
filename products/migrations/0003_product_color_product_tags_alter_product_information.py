# Generated by Django 4.1.3 on 2022-11-10 10:50

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('products', '0002_remove_product_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('white', 'white'), ('red', 'red'), ('blue', 'blue'), ('green', 'green'), ('black', 'black'), ('gray', 'gray'), ('silver', 'silver'), ('brown', 'brown'), ('azure', 'azure')], default='asd', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='product',
            name='information',
            field=models.TextField(blank=True, max_length=15000, null=True),
        ),
    ]
