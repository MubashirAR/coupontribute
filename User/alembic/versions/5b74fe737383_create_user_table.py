"""create user table

Revision ID: 5b74fe737383
Revises: 
Create Date: 2021-05-15 15:20:35.361123

"""
from sqlalchemy.sql.sqltypes import String
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b74fe737383'
down_revision = None
branch_labels = None
depends_on = None
client_encoding='utf8'

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, unique=True, index=True),
        sa.Column('name', sa.String(100)),
        sa.Column('phone', sa.String(15)),
        sa.Column('email', sa.String(15), unique=True, index=True),
        sa.Column('hashed_password', sa.String(100)),
        sa.Column('roles', sa.ARRAY(item_type=String(20))),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade():
    pass
