"""created authors model and connected it to books with foreign key

Revision ID: 87e64ff943a0
Revises: 75cfeea3791b
Create Date: 2023-05-08 11:35:45.883876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '87e64ff943a0'
down_revision = '75cfeea3791b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('author',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('book', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'book', 'author', ['author_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'book', type_='foreignkey')
    op.drop_column('book', 'author_id')
    op.drop_table('author')
    # ### end Alembic commands ###
