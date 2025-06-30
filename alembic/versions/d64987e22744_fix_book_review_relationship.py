"""Fix book-review relationship

Revision ID: d64987e22744
Revises: a62c54474aaa
Create Date: 2025-06-28 19:28:32.128754

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd64987e22744'
down_revision: Union[str, Sequence[str], None] = 'a62c54474aaa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
