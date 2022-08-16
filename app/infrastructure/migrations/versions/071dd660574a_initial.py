"""Initial

Revision ID: 071dd660574a
Revises: 
Create Date: 2022-07-23 18:19:23.994269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '071dd660574a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    conn = op.get_bind()
    conn.execute(
        '''
        CREATE TABLE IF NOT EXISTS users (
            id uuid PRIMARY KEY,
            first_name varchar(100) NOT NULL,
            last_name varchar(100) NOT NULL,
            middle_name varchar(100),
            created_at timestamp DEFAULT (now()),
            updated_at timestamp DEFAULT (now())
        );
        '''
    )


def downgrade() -> None:
    with op.get_bind() as conn:
        conn.execute('DROP TABLE users')
