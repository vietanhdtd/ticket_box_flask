"""empty message

Revision ID: d086243cf0f3
Revises: 4601429fac34
Create Date: 2019-07-08 14:45:03.423657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd086243cf0f3'
down_revision = '4601429fac34'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('purchases', sa.Column('payment_method', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('purchases', 'payment_method')
    # ### end Alembic commands ###