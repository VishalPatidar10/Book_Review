"""Fix review-book relationship

Revision ID: b9536c69a415
Revises: 9b9b17db35f3
Create Date: 2025-06-28 19:59:52.197132

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b9536c69a415'
down_revision: Union[str, Sequence[str], None] = '9b9b17db35f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
