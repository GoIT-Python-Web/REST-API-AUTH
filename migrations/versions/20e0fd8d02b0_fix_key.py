"""fix key

Revision ID: 20e0fd8d02b0
Revises: 0736298ff636
Create Date: 2023-02-01 15:44:47.343643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20e0fd8d02b0'
down_revision = '0736298ff636'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tags_name_key', 'tags', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('tags_name_key', 'tags', ['name'])
    # ### end Alembic commands ###
