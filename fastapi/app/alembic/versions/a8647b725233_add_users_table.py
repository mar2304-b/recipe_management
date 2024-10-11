"""add users table

Revision ID: a8647b725233
Revises: 9d208bbef725
Create Date: 2024-10-11 12:58:05.597795

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'a8647b725233'
down_revision: Union[str, None] = '9d208bbef725'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('weigth', sa.Float(), nullable=False),
    sa.Column('diabetic', sa.Boolean(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=50), nullable=False),
    sa.Column('account_type', sa.Integer(), nullable=False),
    sa.Column('profile_picture', sa.String(length=100), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['user_roles.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.drop_index('email', table_name='ingredients_categories')
    op.drop_index('username', table_name='ingredients_categories')
    op.drop_constraint('ingredients_categories_ibfk_1', 'ingredients_categories', type_='foreignkey')
    op.drop_column('ingredients_categories', 'username')
    op.drop_column('ingredients_categories', 'email')
    op.drop_column('ingredients_categories', 'weigth')
    op.drop_column('ingredients_categories', 'role_id')
    op.drop_column('ingredients_categories', 'account_type')
    op.drop_column('ingredients_categories', 'age')
    op.drop_column('ingredients_categories', 'diabetic')
    op.drop_column('ingredients_categories', 'profile_picture')
    op.drop_column('ingredients_categories', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ingredients_categories', sa.Column('password', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('ingredients_categories', sa.Column('profile_picture', mysql.VARCHAR(length=100), nullable=True))
    op.add_column('ingredients_categories', sa.Column('diabetic', mysql.TINYINT(display_width=1), autoincrement=False, nullable=False))
    op.add_column('ingredients_categories', sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('ingredients_categories', sa.Column('account_type', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('ingredients_categories', sa.Column('role_id', mysql.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('ingredients_categories', sa.Column('weigth', mysql.FLOAT(), nullable=False))
    op.add_column('ingredients_categories', sa.Column('email', mysql.VARCHAR(length=50), nullable=False))
    op.add_column('ingredients_categories', sa.Column('username', mysql.VARCHAR(length=80), nullable=False))
    op.create_foreign_key('ingredients_categories_ibfk_1', 'ingredients_categories', 'user_roles', ['role_id'], ['id'])
    op.create_index('username', 'ingredients_categories', ['username'], unique=True)
    op.create_index('email', 'ingredients_categories', ['email'], unique=True)
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
