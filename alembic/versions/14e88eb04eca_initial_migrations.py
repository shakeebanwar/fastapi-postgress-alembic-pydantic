"""Initial migrations

Revision ID: 14e88eb04eca
Revises: 
Create Date: 2023-07-28 03:46:49.360482

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '14e88eb04eca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('created_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_items_created_date'), 'items', ['created_date'], unique=False)
    op.create_index(op.f('ix_items_description'), 'items', ['description'], unique=False)
    op.create_index(op.f('ix_items_id'), 'items', ['id'], unique=False)
    op.create_index(op.f('ix_items_name'), 'items', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_items_name'), table_name='items')
    op.drop_index(op.f('ix_items_id'), table_name='items')
    op.drop_index(op.f('ix_items_description'), table_name='items')
    op.drop_index(op.f('ix_items_created_date'), table_name='items')
    op.drop_table('items')
    # ### end Alembic commands ###
