"""fix book-review relationship

Revision ID: 665ff95a0efb
Revises: 189017e2291b
Create Date: 2025-06-28 19:36:38.044420

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '665ff95a0efb'
down_revision: Union[str, Sequence[str], None] = '189017e2291b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
