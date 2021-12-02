"""empty message

Revision ID: 1d36fbc3fa03
Revises: 
Create Date: 2021-11-25 20:08:31.145304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d36fbc3fa03'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('dispo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product', sa.String(length=120), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('time', sa.Time(), nullable=False),
    sa.Column('available', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('product',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('lastname', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('product')
    op.drop_table('dispo')
    op.drop_table('book')
    # ### end Alembic commands ###
