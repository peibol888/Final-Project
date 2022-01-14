"""empty message

Revision ID: 113d2299ea69
Revises: 6d55d66fc743
Create Date: 2022-01-14 16:38:50.141643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '113d2299ea69'
down_revision = '6d55d66fc743'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('business',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=9), nullable=False),
    sa.Column('schedule', sa.String(length=40), nullable=False),
    sa.Column('fb_url', sa.String(length=255), nullable=True),
    sa.Column('ig_url', sa.String(length=255), nullable=True),
    sa.Column('twitter_url', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('business')
    # ### end Alembic commands ###
