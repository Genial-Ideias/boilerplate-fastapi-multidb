"""create tenant table

Revision ID: c99db18325af
Revises:
Create Date: 2021-06-15 13:42:26.092059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c99db18325af'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'tenants',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('code', sa.String(20), nullable=False),
        sa.Column('domain', sa.String(150), nullable=False),
        sa.Column('is_active', sa.Boolean, default=True)
    )


def downgrade():
    op.drop_table('tenants')
