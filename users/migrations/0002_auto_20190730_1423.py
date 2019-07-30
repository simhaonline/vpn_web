# Generated by Django 2.2.3 on 2019-07-30 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='radacct',
            options={'managed': False, 'verbose_name_plural': 'VPN计费表'},
        ),
        migrations.AlterModelOptions(
            name='radgroupreply',
            options={'managed': False, 'verbose_name': 'VPN组', 'verbose_name_plural': 'VPN组授权表'},
        ),
        migrations.AlterModelOptions(
            name='radpostauth',
            options={'managed': False, 'verbose_name_plural': 'VPN登录记录表'},
        ),
        migrations.AlterModelOptions(
            name='radusergroup',
            options={'managed': False, 'verbose_name': 'VPN用户名', 'verbose_name_plural': 'VPN账户&组对应表'},
        ),
        migrations.AddField(
            model_name='user',
            name='in_office',
            field=models.BooleanField(default=True, verbose_name='是否在职'),
        ),
        migrations.AlterField(
            model_name='user',
            name='c_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='邮件地址'),
        ),
        migrations.AlterField(
            model_name='user',
            name='has_confirmed',
            field=models.BooleanField(default=False, verbose_name='是否邮件确认'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='用户名'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=64, verbose_name='密码'),
        ),
    ]