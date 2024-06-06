"""add last few columns to posts table

Revision ID: 7cbfff1a946d
Revises: ab58ed325d5f
Create Date: 2024-06-05 22:37:56.327057

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cbfff1a946d'
down_revision: Union[str, None] = 'ab58ed325d5f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'))
    op.add_column('posts',
                  sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()'))
                  )
    pass

def downgrade() -> None:
    op.drop_table('posts', 'published')
    op.drop_table('posts', 'created_at')
    pass
