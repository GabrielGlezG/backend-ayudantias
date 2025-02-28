"""empty message

Revision ID: 6c41a2b56f0a
Revises: ad23dd2c167f
Create Date: 2024-11-21 15:56:49.328931

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c41a2b56f0a'
down_revision: Union[str, None] = 'ad23dd2c167f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fechas_postulaciones', sa.Column('is_asigned', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fechas_postulaciones', 'is_asigned')
    # ### end Alembic commands ###
