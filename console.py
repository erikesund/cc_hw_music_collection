import pdb

from models.album import Album
from models.artist import Artist

import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Radiohead")
artist_repository.save(artist_1)

artist_2 = Artist("Frightened Rabbit")
artist_repository.save(artist_2)


album_1 = Album("The Bends", "Alternative Rock", artist_1)
album_repository.save(album_1)


album_2 = Album("OK Computer", "Alternative Rock", artist_1)
album_repository.save(album_2)


album_3 = Album("Sing the Greys", "Indie", artist_2)
album_repository.save(album_3)

album_repository.select_all()
artist_repository.select_all()


pdb.set_trace()