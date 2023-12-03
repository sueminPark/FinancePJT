# Generated by Django 4.2.7 on 2023-11-23 05:49

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
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prdt_div', models.TextField(null=True)),
                ('dcls_month', models.TextField(max_length=6, null=True)),
                ('fin_co_non', models.TextField(null=True)),
                ('kor_co_nm', models.TextField(null=True)),
                ('fin_prdt_cd', models.TextField(null=True)),
                ('fin_prdt_nm', models.TextField(null=True)),
                ('mtrt_int', models.TextField(null=True)),
                ('join_deny', models.TextField(null=True)),
                ('join_member', models.TextField(null=True)),
                ('max_limit', models.IntegerField(null=True)),
                ('dcls_strt_day', models.TextField(null=True)),
                ('dcls_end_day', models.TextField(null=True)),
                ('fin_co_subm_day', models.TextField(null=True)),
                ('intr_rate_type', models.TextField(null=True)),
                ('intr_rate_type_nm', models.TextField(null=True)),
                ('save_trm', models.TextField(null=True)),
                ('intr_rate', models.FloatField(null=True)),
                ('intr_rate2', models.FloatField(null=True)),
                ('isWon', models.BooleanField(null=True)),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
