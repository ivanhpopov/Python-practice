def make_album(name, album, songs=None):
    albums = {'Artist': name, 'Album': album}
    if songs:
        albums['songs'] = songs
    return albums

while True:
    name = input("Please provide artist name or enter 'q' to quit.")
    if name == 'q':
        break
    album = input("Please provide album, or enter 'q' to quit.")
    if album == 'q':
        break
    songs = input("Please provide number of songs, or enter 'q' to skip.")
    if songs == 'q':
        answer = make_album(name, album)
        print(answer)
        break
    else:
        answer = make_album(name, album, songs)
        print(answer)