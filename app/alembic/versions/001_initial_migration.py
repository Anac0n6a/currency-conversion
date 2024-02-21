"""Initial migration

Revision ID: 001
Create Date: 2024-02-21
Down Revision ID: None

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# Объявление переменной revision
revision = '001'
down_revision = None


def upgrade():
    # Создаем таблицу currencies
    op.create_table(
        'currencies',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('code', sa.String, unique=True),
        sa.Column('rate', sa.Float),
        sa.Column('updated_at', sa.String)
    )

    currencies_table = table('currencies',
                             column('name', sa.String),
                             column('code', sa.String),
                             column('rate', sa.Float),
                             column('updated_at', sa.String))

    op.bulk_insert(
        currencies_table,
        [
            {'name': 'US Dollar', 'code': 'USD', 'rate': 1.0,
             'updated_at': '2024-02-21'},
            {'name': 'Euro', 'code': 'EUR', 'rate': 0.85,
             'updated_at': '2024-02-21'},

        ]
    )


def downgrade():
    op.drop_table('currencies')
