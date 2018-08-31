# Generated by Django 2.0.7 on 2018-08-03 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("election", "0002_auto_20180802_2035")]

    operations = [
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(blank=True, max_length=250)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("1", "PRÉDIO RESIDENCIAL"),
                            ("2", "PRÉDIO COMERCIAL"),
                            ("3", "GALPÃO"),
                            ("11", "APARTAMENTO"),
                            ("12", "CASA"),
                            ("13", "TERRENO"),
                            ("14", "TERRA NUA"),
                            ("15", "SALA OU CONJUNTO"),
                            ("16", "CONSTRUÇÃO"),
                            ("17", "BENFEITORIAS"),
                            ("18", "LOJA"),
                            ("19", "OUTROS BENS IMÓVEIS"),
                            (
                                "21",
                                "VEÍCULO AUTOMOTOR TERRESTRE: CAMINHÃO, AUTOMÓVEL, MOTO, ETC.",
                            ),
                            ("22", "AERONAVE"),
                            ("23", "EMBARCAÇÃO"),
                            (
                                "24",
                                "BEM RELACIONADO COM O EXERCÍCIO DA ATIVIDADE AUTÔNOMA",
                            ),
                            (
                                "25",
                                "JÓIA, QUADRO, OBJETO DE ARTE, DE COLEÇÃO, ANTIGUIDADE, ETC.",
                            ),
                            ("26", "LINHA TELEFÔNICA"),
                            ("29", "OUTROS BENS MÓVEIS"),
                            (
                                "31",
                                "AÇÕES (INCLUSIVE AS PROVENIENTES DE LINHA TELEFÔNICA)",
                            ),
                            ("32", "QUOTAS OU QUINHÕES DE CAPITAL"),
                            ("39", "OUTRAS PARTICIPAÇÕES SOCIETÁRIAS"),
                            ("41", "CADERNETA DE POUPANÇA"),
                            ("45", "APLICAÇÃO DE RENDA FIXA (CDB, RDB E OUTROS)"),
                            ("46", "OURO, ATIVO FINANCEIRO"),
                            ("47", "MERCADO FUTUROS, DE OPÇÕES E A TERMO"),
                            ("49", "OUTRAS APLICAÇÕES E INVESTIMENTOS"),
                            ("51", "CRÉDITO DECORRENTE DE EMPRÉSTIMO"),
                            ("52", "CRÉDITO DECORRENTE DE ALIENAÇÃO"),
                            ("53", "PLANO PAIT E CADERNETA DE PECÚLIO"),
                            (
                                "54",
                                "POUPANÇA PARA CONSTRUÇÃO OU AQUISIÇÃO DE BEM IMÓVEL",
                            ),
                            ("59", "OUTROS CRÉDITOS E POUPANÇA VINCULADOS"),
                            ("61", "DEPÓSITO BANCÁRIO EM CONTA CORRENTE NO PAÍS"),
                            ("62", "DEPÓSITO BANCÁRIO EM CONTA CORRENTE NO EXTERIOR"),
                            ("63", "DINHEIRO EM ESPÉCIE - MOEDA NACIONAL"),
                            ("64", "DINHEIRO EM ESPÉCIE - MOEDA ESTRANGEIRA"),
                            ("69", "OUTROS DEPÓSITOS À VISTA E NUMERÁRIO"),
                            ("71", "FUNDO DE INVESTIMENTO FINANCEIRO - FIF"),
                            (
                                "72",
                                "FUNDO DE APLICAÇÃO EM QUOTAS DE FUNDOS DE INVESTIMENTO",
                            ),
                            ("73", "FUNDO DE CAPITALIZAÇÃO"),
                            (
                                "74",
                                "FUNDO DE AÇÕES, INCLUSIVE CARTEIRA LIVRE E FUNDO DE INVESTIMENTO NO EXTERIOR",
                            ),
                            ("79", "OUTROS FUNDOS"),
                            ("91", "LICENÇA E CONCESSÕES ESPECIAIS"),
                            ("92", "TÍTULO DE CLUBE E ASSEMELHADO"),
                            ("93", "DIREITO DE AUTOR, DE INVENTOR E PATENTE"),
                            ("94", "DIREITO DE LAVRA E ASSEMELHADO"),
                            ("95", "CONSÓRCIO NÃO CONTEMPLADO"),
                            ("96", "LEASING"),
                            ("97", "VGBL - VIDA GERADOR DE BENEFÍCIO LIVRE"),
                            ("99", "OUTROS BENS E DIREITOS"),
                        ],
                        max_length=2,
                    ),
                ),
                ("value", models.FloatField()),
                (
                    "election",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assets",
                        to="election.Election",
                    ),
                ),
            ],
        )
    ]
