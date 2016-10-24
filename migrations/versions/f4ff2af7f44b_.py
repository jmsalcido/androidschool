"""empty message

Revision ID: f4ff2af7f44b
Revises: 5529d5f46387
Create Date: 2016-10-22 22:23:04.527242

"""

# revision identifiers, used by Alembic.
revision = 'f4ff2af7f44b'
down_revision = '5529d5f46387'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('events', sa.Column('modified_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('modified_at', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'modified_at')
    op.drop_column('users', 'created_at')
    op.drop_column('events', 'modified_at')
    op.drop_column('events', 'created_at')
    ### end Alembic commands ###
