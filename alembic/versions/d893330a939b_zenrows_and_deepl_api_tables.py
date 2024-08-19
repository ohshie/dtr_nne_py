"""zenrows and deepl api tables

Revision ID: d893330a939b
Revises: 3ba97a075656
Create Date: 2024-08-19 17:38:21.563352

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd893330a939b'
down_revision: Union[str, None] = '3ba97a075656'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('zenrows',
    sa.Column('ApiKey', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('ApiKey')
    )
    op.create_table('deepl',
    sa.Column('ApiKey', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('ApiKey')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('deepl')
    op.drop_table('zenrows')
    # ### end Alembic commands ###
