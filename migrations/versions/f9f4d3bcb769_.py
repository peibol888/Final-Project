"""empty message

Revision ID: f9f4d3bcb769
Revises: 58c38124f3c9
Create Date: 2022-01-24 15:28:24.768788

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f9f4d3bcb769'
down_revision = '58c38124f3c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('status', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'status')
    # ### end Alembic commands ###
