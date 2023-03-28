"""Add setup for seed data and columns: round 2

Revision ID: 463ef599e342
Revises: 9e8651add341
Create Date: 2023-03-28 07:00:34.875586

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '463ef599e342'
down_revision = '9e8651add341'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('dancers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_dancers_name'), 'dancers', ['name'], unique=False)
    op.create_table('instructors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_instructors_name'), 'instructors', ['name'], unique=False)
    op.create_table('lessons',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_lessons_type'), 'lessons', ['type'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_lessons_type'), table_name='lessons')
    op.drop_table('lessons')
    op.drop_index(op.f('ix_instructors_name'), table_name='instructors')
    op.drop_table('instructors')
    op.drop_index(op.f('ix_dancers_name'), table_name='dancers')
    op.drop_table('dancers')
    # ### end Alembic commands ###
