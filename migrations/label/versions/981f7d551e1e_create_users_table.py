"""create users table

Revision ID: 981f7d551e1e
Revises:
Create Date: 2021-06-15 13:54:25.021964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '981f7d551e1e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade(engine_name):
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(60), nullable=False),
        sa.Column('password', sa.String(30), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade(engine_name):
    op.drop_table('users')
