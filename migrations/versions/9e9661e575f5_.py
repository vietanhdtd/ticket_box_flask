"""empty message

Revision ID: 9e9661e575f5
Revises: 656ef987c631
Create Date: 2019-07-09 10:21:48.340529

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9e9661e575f5'
down_revision = '656ef987c631'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('purchase',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('event_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('date_purchase', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('payment_menthod', sa.String(length=255), nullable=False),
    sa.Column('ticket_type', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], ),
    sa.ForeignKeyConstraint(['ticket_type'], ['tickets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('purchases')
    op.alter_column('events', 'starting_date',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.DateTime(),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('events', 'starting_date',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False)
    op.create_table('purchases',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('event_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('payment_method', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('date_purchase', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('ticket_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['event_id'], ['events.id'], name='purchases_event_id_fkey'),
    sa.ForeignKeyConstraint(['ticket_id'], ['tickets.id'], name='purchases_ticket_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='purchases_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='purchases_pkey')
    )
    op.drop_table('purchase')
    # ### end Alembic commands ###
