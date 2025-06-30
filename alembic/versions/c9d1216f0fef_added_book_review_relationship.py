"""Added Book-Review relationship

Revision ID: c9d1216f0fef
Revises: 46783594dbeb
Create Date: 2025-06-28 19:21:20.228261

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9d1216f0fef'
down_revision: Union[str, Sequence[str], None] = '46783594dbeb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
