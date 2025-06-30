"""Fix models again

Revision ID: 189017e2291b
Revises: d64987e22744
Create Date: 2025-06-28 19:32:27.877306

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '189017e2291b'
down_revision: Union[str, Sequence[str], None] = 'd64987e22744'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
