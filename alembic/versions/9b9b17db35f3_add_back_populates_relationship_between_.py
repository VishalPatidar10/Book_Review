"""add back_populates relationship between Book and Review

Revision ID: 9b9b17db35f3
Revises: 665ff95a0efb
Create Date: 2025-06-28 19:44:21.616748

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9b9b17db35f3'
down_revision: Union[str, Sequence[str], None] = '665ff95a0efb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
