"""Added checkout and due dates

Revision ID: fb28189ebe89
Revises: 073bd9979a52
Create Date: 2024-04-30 00:46:26.516525

"""
from alembic import op
import sqlalchemy as sa
import fastapi_users_db_sqlalchemy


# revision identifiers, used by Alembic.
revision = 'fb28189ebe89'
down_revision = '073bd9979a52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('transactions', 'checkout_date',
               existing_type=sa.DATE(),
               nullable=False)
    op.alter_column('transactions', 'due_date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('transactions', 'due_date',
               existing_type=sa.DATE(),
               nullable=True)
    op.alter_column('transactions', 'checkout_date',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###
