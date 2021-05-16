"""create payment table

Revision ID: 59e71d1ebbbc
Revises: 
Create Date: 2021-05-15 18:10:30.703796

"""
import sys
sys.path.append("/app")
try:
    from Payment.app.models import PayedFor
except:
    print('Docker!')
    from app.models import PayedFor
from alembic import op
import sqlalchemy as sa
from sqlalchemy.orm import validates


# revision identifiers, used by Alembic.
# revision = '59e71d1ebbbc'
revision = '5b74fe737383'

down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'payments',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('amount', sa.Integer),
        sa.Column('user_id', sa.Integer, nullable=False),
        sa.Column('ref_id', sa.Integer, nullable=False),
        sa.Column('paid_for', sa.Enum(PayedFor), nullable=False)
    )


def downgrade():
    pass
