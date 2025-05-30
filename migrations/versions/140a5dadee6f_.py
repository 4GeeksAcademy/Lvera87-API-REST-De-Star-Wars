"""empty message

Revision ID: 140a5dadee6f
Revises: a5cffa318ac2
Create Date: 2025-04-14 15:24:09.208492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '140a5dadee6f'
down_revision = 'a5cffa318ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('diameter', sa.String(length=40), nullable=True),
    sa.Column('rotation_period', sa.String(length=40), nullable=True),
    sa.Column('orbital_period', sa.String(length=40), nullable=True),
    sa.Column('gravity', sa.String(length=40), nullable=True),
    sa.Column('population', sa.String(length=40), nullable=True),
    sa.Column('climate', sa.String(length=100), nullable=True),
    sa.Column('terrain', sa.String(length=100), nullable=True),
    sa.Column('surface_water', sa.String(length=40), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=200), nullable=False),
    sa.Column('first_name', sa.String(length=80), nullable=True),
    sa.Column('last_name', sa.String(length=80), nullable=True),
    sa.Column('subscription_date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('model', sa.String(length=100), nullable=False),
    sa.Column('manufacturer', sa.String(length=200), nullable=False),
    sa.Column('cost_in_credits', sa.String(length=40), nullable=True),
    sa.Column('length', sa.String(length=20), nullable=True),
    sa.Column('max_atmosphering_speed', sa.String(length=40), nullable=True),
    sa.Column('crew', sa.String(length=40), nullable=True),
    sa.Column('passengers', sa.String(length=40), nullable=True),
    sa.Column('cargo_capacity', sa.String(length=40), nullable=True),
    sa.Column('consumables', sa.String(length=40), nullable=True),
    sa.Column('vehicle_class', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('favorite_planets',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('planet_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['planet_id'], ['planets.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'planet_id')
    )
    op.create_table('favorite_vehicles',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('vehicle_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['vehicle_id'], ['vehicles.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'vehicle_id')
    )
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('height', sa.String(length=20), nullable=True),
    sa.Column('mass', sa.String(length=20), nullable=True),
    sa.Column('hair_color', sa.String(length=50), nullable=True),
    sa.Column('skin_color', sa.String(length=50), nullable=True),
    sa.Column('eye_color', sa.String(length=50), nullable=True),
    sa.Column('birth_year', sa.String(length=20), nullable=True),
    sa.Column('gender', sa.String(length=20), nullable=True),
    sa.Column('homeworld_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['homeworld_id'], ['planets.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favorite_people',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('person_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['person_id'], ['people.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'person_id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='user_pkey'),
    sa.UniqueConstraint('email', name='user_email_key')
    )
    op.drop_table('favorite_people')
    op.drop_table('people')
    op.drop_table('favorite_vehicles')
    op.drop_table('favorite_planets')
    op.drop_table('vehicles')
    op.drop_table('users')
    op.drop_table('planets')
    # ### end Alembic commands ###
