"""empty message

Revision ID: 3ff300857ee3
Revises: d3af8f1f93d5
Create Date: 2016-10-22 23:05:23.998168

"""

# revision identifiers, used by Alembic.
revision = '3ff300857ee3'
down_revision = 'd3af8f1f93d5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.drop_constraint('users_username_key', 'users', type_='unique')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('users_username_key', 'users', ['username'])
    op.drop_index(op.f('ix_users_username'), table_name='users')
    ### end Alembic commands ###