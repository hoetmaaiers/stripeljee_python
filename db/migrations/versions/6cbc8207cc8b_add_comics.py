"""Add comics

Revision ID: 6cbc8207cc8b
Revises: c70a874d975a
Create Date: 2023-12-20 11:23:16.566440

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

from db.migrations import utils

# revision identifiers, used by Alembic.
revision: str = "6cbc8207cc8b"
down_revision: Union[str, None] = "c70a874d975a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "comics",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=False),
        sa.Column("serie_number", sa.Integer(), nullable=False),
        sa.Column("isbn", sa.String(), nullable=True),
        sa.Column("serie_id", sa.Integer(), nullable=True),
        sa.Column(
            "inserted_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.Column(
            "updated_at", sa.DateTime(), server_default=sa.text("now()"), nullable=True
        ),
        sa.ForeignKeyConstraint(
            ["serie_id"],
            ["series.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )

    # utils.create_update_timestamp_trigger(op, "comics")


def downgrade() -> None:
    op.drop_table("comics")
