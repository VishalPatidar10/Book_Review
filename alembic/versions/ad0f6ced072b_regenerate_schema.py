"""regenerate schema

Revision ID: ad0f6ced072b
Revises: 768ae59e6129
Create Date: 2025-06-28 17:49:45.986170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ad0f6ced072b'
down_revision: Union[str, Sequence[str], None] = '768ae59e6129'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
