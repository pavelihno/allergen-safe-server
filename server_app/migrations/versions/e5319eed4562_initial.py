"""initial

Revision ID: e5319eed4562
Revises: 
Create Date: 2024-05-09 07:43:15.346934

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5319eed4562'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('allergen_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('cuisines',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('reaction_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('image', sa.LargeBinary(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.Column('role', sa.String(length=10), nullable=True),
    sa.Column('created_at', sa.Date(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.CheckConstraint("role IN ('admin', 'standard')", name='role_types'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('allergens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nFASS', sa.Float(), nullable=False),
    sa.Column('probability', sa.Float(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('allergen_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['allergen_type_id'], ['allergen_types.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reactions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('dish_name', sa.String(length=50), nullable=False),
    sa.Column('dish_description', sa.Text(), nullable=True),
    sa.Column('reaction_strength', sa.Integer(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('reaction_type_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.ForeignKeyConstraint(['reaction_type_id'], ['reaction_types.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ingredients', sa.Text(), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('cuisine_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cuisine_id'], ['cuisines.id'], ),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    op.drop_table('reactions')
    op.drop_table('allergens')
    op.drop_table('profiles')
    op.drop_table('users')
    op.drop_table('reaction_types')
    op.drop_table('cuisines')
    op.drop_table('allergen_types')
    # ### end Alembic commands ###
