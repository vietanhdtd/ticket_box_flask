"""empty message

Revision ID: 1030ea422f01
Revises: 9a5d31ce5659
Create Date: 2019-07-08 17:12:22.391904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1030ea422f01'
down_revision = '9a5d31ce5659'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('purchases', sa.Column('ticket_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'purchases', 'ticket', ['ticket_id'], ['ticket_name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'purchases', type_='foreignkey')
    op.drop_column('purchases', 'ticket_id')
    # ### end Alembic commands ###