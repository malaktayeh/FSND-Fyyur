"""empty message

Revision ID: addeb931d08b
Revises: f7fb614a08df
Create Date: 2019-11-22 16:36:39.907708

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'addeb931d08b'
down_revision = 'f7fb614a08df'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Artist',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('genres', sa.JSON(), nullable=False),
    sa.Column('seeking_venue', sa.Boolean(), nullable=False),
    sa.Column('seeking_description', sa.String(length=500), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('artist_id')
    )
    op.create_table('Venue',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('genres', sa.JSON(), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('state', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=120), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.Column('website', sa.String(length=500), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=False),
    sa.Column('seeking_description', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('venue_id')
    )
    op.create_table('Show',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['Artist.artist_id'], ondelete='cascade'),
    sa.ForeignKeyConstraint(['venue_id'], ['Venue.venue_id'], ondelete='cascade'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Show')
    op.drop_table('Venue')
    op.drop_table('Artist')
    # ### end Alembic commands ###