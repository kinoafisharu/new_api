from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20200531_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='sourcefilms',
            name='filmobject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.Films'),
        ),
    ]
