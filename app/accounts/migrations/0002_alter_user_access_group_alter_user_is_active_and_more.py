# Generated by Django 4.2.6 on 2023-12-01 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="access_group",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="access_group_user",
                to="auth.group",
                verbose_name="grupo",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_active",
            field=models.BooleanField(
                default=True,
                help_text="Indica que o usuário será tratado como ativo. Ao invés de excluir contas de usuário, desmarque isso.",
                verbose_name="Ativo?",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_staff",
            field=models.BooleanField(
                default=False,
                help_text="Indica que usuário consegue acessar este site de administração.",
                verbose_name="Acesso ao Dashboard?",
            ),
        ),
    ]
