# Generated by Django 4.1.7 on 2023-04-12 19:18

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='WalletUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nin', models.CharField(max_length=225)),
                ('home_address', models.CharField(max_length=225)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('account_number', models.CharField(max_length=255)),
                ('bank', models.CharField(choices=[('ZENITH', 'ZENITH'), ('UBA', 'UBA'), ('PALMPAY', 'PALMPAY'), ('KUDA', 'KUDA'), ('GTB', 'GTB')], default='', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Airtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('MTN', 'MTN'), ('GLO', 'GLO'), ('AIRTEL', 'AIRTEL'), ('ETISALAT', 'ETISALAT')], default='', max_length=25)),
                ('phone_number', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.CharField(max_length=255)),
                ('card_number', models.CharField(max_length=10)),
                ('expiry_date', models.DateField()),
                ('cvv', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('relationship', models.CharField(max_length=255)),
                ('bvn', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_types', models.CharField(choices=[('WITHDRAWN', 'WITHDRAWN'), ('SPENDING', 'SPEND'), ('SAVE', 'SAVE'), ('AIRTIME', 'AIRTIME')], default='', max_length=24)),
                ('status', models.CharField(choices=[('SUCCESSFUL', 'SUCCESSFUL'), ('FAILED', 'FAILED'), ('REVERSED', 'REVERSED'), ('PENDING', 'PENDING')], default='', max_length=25)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField()),
                ('transaction_time', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wallet.account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=4, default=0, max_digits=6)),
                ('transaction', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='wallet.transaction')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='credit_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.creditcard'),
        ),
        migrations.AddField(
            model_name='walletuser',
            name='credit_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='credit_cards', to='wallet.creditcard'),
        ),
        migrations.AddField(
            model_name='walletuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='walletuser',
            name='next_of_kin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='next_of_kin', to='wallet.nextofkin'),
        ),
        migrations.AddField(
            model_name='walletuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
