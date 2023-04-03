"""many to many upgrade

Revision ID: f437d5c8504e
Revises: 
Create Date: 2023-03-28 20:48:06.873268

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f437d5c8504e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('helper',
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], )
    )
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint('fk_post_author_id_author', type_='foreignkey')
        batch_op.drop_column('author_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key('fk_post_author_id_author', 'author', ['author_id'], ['id'])

    op.drop_table('helper')
    # ### end Alembic commands ###
