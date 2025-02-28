"""empty message

Revision ID: 5371ddc93f14
Revises: 
Create Date: 2019-03-29 09:43:44.531596

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5371ddc93f14'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wheel',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('img', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wheel')
    # ### end Alembic commands ###
