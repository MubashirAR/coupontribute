"""create payment table

Revision ID: 59e71d1ebbbc
Revises: 
Create Date: 2021-05-15 18:10:30.703796

"""
from Payment.app.models import PayedFor
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59e71d1ebbbc'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'payments',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('amount', sa.Integer, min=0),
        sa.Column('user_id', sa.Integer, required=True),
        sa.Column('ref_id', sa.Integer, required=True),
        sa.Column('payed_for', sa.Enum(PayedFor), required=True)
    )


def downgrade():
    pass
