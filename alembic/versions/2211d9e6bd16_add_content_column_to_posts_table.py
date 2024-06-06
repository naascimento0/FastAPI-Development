"""add content column to posts table

Revision ID: 2211d9e6bd16
Revises: bfb4b7ca28be
Create Date: 2024-06-05 19:26:33.452132

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2211d9e6bd16'
down_revision: Union[str, None] = 'bfb4b7ca28be'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
