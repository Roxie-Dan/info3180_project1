"""empty message

Revision ID: 940b72a1e300
Revises: 
Create Date: 2017-03-10 18:06:35.050000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '940b72a1e300'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_profile',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.Column('profile_created_on', sa.DateTime(), nullable=True),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('image', sa.String(length=80), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('bio', sa.String(length=500), nullable=True),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_profile')
    # ### end Alembic commands ###
