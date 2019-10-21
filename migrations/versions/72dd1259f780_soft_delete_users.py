"""soft delete users

Revision ID: 72dd1259f780
Revises: 2f31d469cdc4
Create Date: 2016-09-27 11:34:56.340310

"""

# revision identifiers, used by Alembic.
revision = '72dd1259f780'
down_revision = '2f31d469cdc4'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('deleted', sa.Boolean(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'deleted')
    ### end Alembic commands ###