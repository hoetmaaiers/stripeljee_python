"""Add series

Revision ID: c70a874d975a
Revises:
Create Date: 2023-12-20 11:10:21.656163

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from db.migrations import utils

# revision identifiers, used by Alembic.
revision: str = "c70a874d975a"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    utils.create_update_modified_column_function(op)

    op.create_table(
        "series",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("inserted_at", sa.DateTime, server_default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, onupdate=sa.func.now()),
        sa.PrimaryKeyConstraint("id"),
    )

    # utils.create_update_timestamp_trigger(op, "series")


def downgrade() -> None:
    op.drop_table("series")
    # utils.drop_update_modified_column_function(op)
