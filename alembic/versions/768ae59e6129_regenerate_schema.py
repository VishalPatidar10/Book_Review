"""regenerate schema

Revision ID: 768ae59e6129
Revises: 8ede4c5094f6
Create Date: 2025-06-28 17:37:02.973770

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '768ae59e6129'
down_revision: Union[str, Sequence[str], None] = '8ede4c5094f6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
