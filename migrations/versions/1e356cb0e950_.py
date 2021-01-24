"""empty message

Revision ID: 1e356cb0e950
Revises: 
Create Date: 2021-01-24 12:32:52.308936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e356cb0e950'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('drink')
    op.drop_table('donut')
    op.drop_table('combo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('combo',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('drink_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('donut_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['donut_id'], ['donut.id'], name='combo_donut_id_fkey'),
    sa.ForeignKeyConstraint(['drink_id'], ['drink.id'], name='combo_drink_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='combo_pkey')
    )
    op.create_table('donut',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='donut_pkey')
    )
    op.create_table('drink',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='drink_pkey')
    )
    # ### end Alembic commands ###
