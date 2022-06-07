import pdb

from models.artist import Artist

import repositories.artist_repository as artist_repository

artist_repository.select_all()

artist_1 = Artist("Radiohead")
artist_repository.save(artist_1)
artist_repository.select_all()

artist_2 = Artist("Frightened Rabbit")
artist_repository.save(artist_2)
artist_repository.select_all()

pdb.set_trace()