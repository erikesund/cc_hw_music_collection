
from db.run_sql import run_sql
from models.artist import Artist
from models.album import Album

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row["name"], row["id"])
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    row = run_sql(sql, values)[0]
    if row is not None:
        artist = Artist(row["name"], row["id"])
    return artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values = [artist.name]
    results = run_sql(sql, values)
    id = results[0]["id"]
    artist.id = id
    return artist

def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM artists"

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def list_all_albums(artists):
    albums = []

    sql = "SELECT * FROM albums WHERE artist = %s"
    values = [artist.id]
    results = run_sql(sql, values)

    for row in results:
        album = Album(row["title"], row["genre"], artist, row["id"])
        albums.append(album)
    return albums