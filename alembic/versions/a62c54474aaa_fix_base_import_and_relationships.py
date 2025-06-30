"""Fix Base import and relationships

Revision ID: a62c54474aaa
Revises: c9d1216f0fef
Create Date: 2025-06-28 19:26:57.433443

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a62c54474aaa'
down_revision: Union[str, Sequence[str], None] = 'c9d1216f0fef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
