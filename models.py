#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# Association Object - Show (see sqlalchemy docs)
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many
# The association object pattern is a variant on many-to-many: it’s used when your 
# association table contains additional columns beyond those which are foreign keys 
# to the left and right tables. 
# https://stackoverflow.com/questions/52920701/many-to-many-with-three-tables-relating-with-each-other-sqlalchemy

class Show(db.Model):
    __tablename__ = 'Show'
    id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id', ondelete='cascade'), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id', ondelete='cascade'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __init__(self, venue_id, artist_id, start_time):
      self.venue_id = venue_id,
      self.artist_id = artist_id,
      self.start_time = start_time

    def __repr__(self):
      return f'<Show {self.id} {self.venue_id} {self.artist_id} {self.start_time}>'

class Venue(db.Model):
    __tablename__ = 'Venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    genres = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    website = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    shows = db.relationship('Show', backref='venues', cascade='all, delete-orphan', lazy=True)

    def __init__(self, name, genres, city, state, address, phone, 
      image_link, website, facebook_link, seeking_talent, 
      seeking_description):
      self.name = name
      self.genres = genres
      self.city = city
      self.state = state
      self.address = address
      self.phone = phone
      self.image_link =image_link
      self.website = website
      self.facebook_link = facebook_link
      self.seeking_talent = seeking_talent
      self.seeking_description = seeking_description

    def __repr__(self):
      return f'<Venue {self.id} {self.name}>'

class Artist(db.Model):
    __tablename__ = 'Artist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state= db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String, nullable=False)
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(500))
    website = db.Column(db.String(500))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship('Show', backref='artists', lazy=True, cascade='all, delete-orphan')


    def __init__(self, name, city, state, phone, genres, seeking_venue,
    seeking_description, website, image_link, facebook_link):
        self.name = name
        self.city = city
        self.state = state
        self.phone = phone
        self.genres = genres
        self.seeking_venue = seeking_venue
        self.seeking_description = seeking_description
        self.website = website
        self.image_link = image_link
        self.facebook_link = facebook_link

    def __repr__(self):
        return f'<Venue {self.id} {self.name}>'