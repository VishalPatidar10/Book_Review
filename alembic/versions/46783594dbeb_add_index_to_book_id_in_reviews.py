"""add index to book_id in reviews

Revision ID: 46783594dbeb
Revises: ad0f6ced072b
Create Date: 2025-06-28 18:16:49.528731

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '46783594dbeb'
down_revision: Union[str, Sequence[str], None] = 'ad0f6ced072b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
