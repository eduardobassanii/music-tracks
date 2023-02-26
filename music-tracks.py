import doctest

MS_PER_SECOND = 1000
SECONDS_PER_MINUTE = 60


# represents the characteristic score of a song as:
# (tempo, popularity score, danceability score, energy score)
# where all values are >=0
Scores = tuple[float, int, float, float]
TEMPO = 0
POPULARITY = 1
DANCEABILITY = 2
ENERGY = 3

# represents a music track as:
# (track id, name, artist, duration (in ms), genre tags, scores)
# where id, name, artist != '', duration>0, and genre tags can be empty
MusicTrack = tuple[str, str, str, int, list[str], Scores]
TRACK_ID = 0
TITLE = 1
ARTIST = 2
DURATION = 3
GENRES = 4
SCORES = 5

# represents time as: (minutes, seconds, milliseconds)
# where all values are >= 0
Time = tuple[int, int, int]
MINUTES = 0
SECONDS = 1
MSECONDS = 2

# column numbers of data within input csv file
INPUT_TRACK_ID = 0
INPUT_TITLE = 3
INPUT_ARTIST = 2
INPUT_DURATION = 7
INPUT_GENRE = 1
INPUT_POPULARITY = 4
INPUT_TEMPO = 15
INPUT_DANCEABILITY = 6
INPUT_ENERGY = 8

def read_file(filename: str) -> tuple[dict[str, list[str]], dict[str, MusicTrack]]:
    """
    Populates and returns a tuple with the following 2 dictionaries
    with data from valid filename.

    2 dictionaries returned as a tuple:
    - dict[genre tag: list of track ids associated with the tag]
    - dict[unique track id: music track information]

    Precondition: file is csv with data in expected columns
        and contains a header row with column titles
        Track ids are considered unique.

    >>> read_file('0lines_data.csv')
    ({}, {})

    >>> read_file('4lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    ({'Movie': ['000CzNKC8PEt1yC3L8dqwV'],
      'Reggae': ['000DfZJww8KiixTKuk9usJ'],
      'Jazz': ['000EWWBkYaREzsBplYjUag'],
      'R&B': ['000EWWBkYaREzsBplYjUag']},
    {'00021Wy6AyMbLP2tqij86e':
        ('00021Wy6AyMbLP2tqij86e', 'Zangiefs Theme',
         'Capcom Sound Team', 169173, [], (129.578, 13, 0.617, 0.862)),
     '000CzNKC8PEt1yC3L8dqwV':
        ('000CzNKC8PEt1yC3L8dqwV', 'Coeur Brise √† Prendre - Remastered',
         'Henri Salvador', 130653, ['Movie'], (79.124, 5, 0.518, 0.805)),
     '000DfZJww8KiixTKuk9usJ':
        ('000DfZJww8KiixTKuk9usJ', 'Earthlings', 'Mike Love',
         357573, ['Reggae'], (120.365, 30, 0.631, 0.513)),
     '000EWWBkYaREzsBplYjUag':
        ('000EWWBkYaREzsBplYjUag', 'Fewerdolr', 'Don Philippe',
         104924, ['Jazz', 'R&B'], (76.43, 39, 0.768, 0.137))})


    >>> read_file('20lines_data.csv') # doctest: +NORMALIZE_WHITESPACE
    ({'Anime': ['00021Wy6AyMbLP2tqij86e'],
      'Reggae': ['000DfZJww8KiixTKuk9usJ', '52TDNHSeWey4NFAfLDgfjL',
                 '01w7h4gfJMHtUnykpD6M3f', '01yvyZWcqtI2ZqGhPB2uZq',
                 '02C5QgRFecna4B8Sv406WA', '02cW3CN4DC1QV6D4XRH9UV'],
      'Jazz': ['000EWWBkYaREzsBplYjUag'],
      'Dance': ['000xQL6tZNLJzIrtIgxqSl', '003eoIwxETJujVWmNFMoZy',
                '00S35gEf40z03JTJgvQMqi', '01qMOMudbkIHZS9BFPUGNk',
                '02D9uD9WQb834Lb54xCvDS', '02UYYPOGSBXxGEMce927XV',
                '02ZorlDGq0uTnMobHNh4EL'],
      'Pop': ['000xQL6tZNLJzIrtIgxqSl', '003eoIwxETJujVWmNFMoZy',
              '01qMOMudbkIHZS9BFPUGNk', '02ZorlDGq0uTnMobHNh4EL'],
      'Comedy': ['0017XiMkqbTfF2AUOzlhj6'],
      'Blues': ['001CyR8xqmmpVZFiTZJ5BC'],
      'Soundtrack': ['001VMKfkHZrlyj7JlQbQFL'],
      'Ska': ['001YQlnDSduXd5LgBd66gT'],
      'R&B': ['003eoIwxETJujVWmNFMoZy', '02D9uD9WQb834Lb54xCvDS'],
      'Soul': ['02D9uD9WQb834Lb54xCvDS', '02UYYPOGSBXxGEMce927XV']},
     {'00021Wy6AyMbLP2tqij86e':
        ('00021Wy6AyMbLP2tqij86e',
         'Zangiefs Theme',
         'Capcom Sound Team', 169173, ['Anime'],
         (129.578, 13, 0.617, 0.862)),
      '000DfZJww8KiixTKuk9usJ':
        ('000DfZJww8KiixTKuk9usJ',
         'Earthlings',
         'Mike Love', 357573, ['Reggae'],
         (120.365, 30, 0.631, 0.513)),
      '000EWWBkYaREzsBplYjUag':
        ('000EWWBkYaREzsBplYjUag',
         'Fewerdolr',
         'Don Philippe', 104924, ['Jazz'],
         (76.43, 39, 0.768, 0.137)),
      '000xQL6tZNLJzIrtIgxqSl':
        ('000xQL6tZNLJzIrtIgxqSl',
         'Still Got Time',
         'ZAYN', 188491, ['Dance', 'Pop'],
         (120.963, 70, 0.748, 0.627)),
      '0017XiMkqbTfF2AUOzlhj6':
        ('0017XiMkqbTfF2AUOzlhj6',
         'Thanksgiving Chicken',
         'Chad Daniels', 127040, ['Comedy'],
         (173.912, 27, 0.536, 0.78)),
      '001CyR8xqmmpVZFiTZJ5BC':
        ('001CyR8xqmmpVZFiTZJ5BC',
         'She Knows How To Rock Me',
         'Taj Mahal', 160107, ['Blues'],
         (90.048, 31, 0.826, 0.679)),
      '52TDNHSeWey4NFAfLDgfjL':
        ('52TDNHSeWey4NFAfLDgfjL',
         'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
         'Bob Marley & The Wailers', 278987, ['Reggae'],
         (180.043, 31, 0.675, 0.808)),
      '001VMKfkHZrlyj7JlQbQFL':
        ('001VMKfkHZrlyj7JlQbQFL',
         '"Await The Kings Justice - From The ""Game Of Thrones"" Soundtrack"',
         'Ramin Djawadi', 120840, ['Soundtrack'],
         (113.655, 41, 0.168, 0.0354)),
      '001YQlnDSduXd5LgBd66gT':
        ('001YQlnDSduXd5LgBd66gT',
         'El Tiempo Es Dinero - Remasterizado 2007',
         'Soda Stereo', 177267, ['Ska'],
         (183.571, 38, 0.554, 0.921)),
      '003eoIwxETJujVWmNFMoZy':
        ('003eoIwxETJujVWmNFMoZy',
         'Growing Pains',
         'Alessia Cara', 193680, ['Dance', 'Pop', 'R&B'],
         (191.153, 66, 0.353, 0.755)),
      '00S35gEf40z03JTJgvQMqi':
        ('00S35gEf40z03JTJgvQMqi',
         'Its You - Radio Edit',
         'Syn Cole', 211875, ['Dance'],
         (127.957, 57, 0.646, 0.831)),
      '01qMOMudbkIHZS9BFPUGNk':
        ('01qMOMudbkIHZS9BFPUGNk',
         'Let It Be Me (feat. Ava Max)',
         'David Guetta', 172933, ['Dance', 'Pop'],
         (102.048, 62, 0.743, 0.529)),
      '01qNIJfMc14nxpOoM0Xwb0':
        ('01qNIJfMc14nxpOoM0Xwb0',
         'The Fool and Me - 2007 Remaster',
         'Robin Trower', 235720, [],
         (122.692, 31, 0.409, 0.766)),
      '01w7h4gfJMHtUnykpD6M3f':
        ('01w7h4gfJMHtUnykpD6M3f',
         'See Dem Fake Leaders - Dub Remix',
         'Ziggy Marley', 249740, ['Reggae'],
         (77.501, 24, 0.801, 0.636)),
      '01yvyZWcqtI2ZqGhPB2uZq':
        ('01yvyZWcqtI2ZqGhPB2uZq',
         'Lost Our Way',
         'I-Octane', 232091, ['Reggae'],
         (133.936, 5, 0.733, 0.492)),
      '02D9uD9WQb834Lb54xCvDS':
        ('02D9uD9WQb834Lb54xCvDS',
         'Love U 4 Life',
         'Jodeci', 290067, ['Dance', 'R&B', 'Soul'],
         (118.106, 53, 0.695, 0.638)),
      '02C5QgRFecna4B8Sv406WA':
        ('02C5QgRFecna4B8Sv406WA',
         'Get Up  Stand Up - Thievery Corporation Remix',
         'Bob Marley & The Wailers', 261693, ['Reggae'],
         (166.067, 27, 0.676, 0.702)),
      '02UYYPOGSBXxGEMce927XV':
        ('02UYYPOGSBXxGEMce927XV',
         'Nobody (feat. Athena Cage) - Remastered Single Version',
         'Keith Sweat', 251760, ['Dance', 'Soul'],
         (117.896, 47, 0.712, 0.511)),
      '02ZorlDGq0uTnMobHNh4EL':
        ('02ZorlDGq0uTnMobHNh4EL',
         'Bravado',
         'Lorde', 221409, ['Dance', 'Pop'],
         (175.879, 60, 0.489, 0.536)),
      '02cW3CN4DC1QV6D4XRH9UV':
        ('02cW3CN4DC1QV6D4XRH9UV',
         'Cant Dweet Again',
         'Christopher Martin', 144000, ['Reggae'],
         (99.531, 44, 0.71, 0.645))})
    """
    genre_to_track_ids = {}
    track_id_to_information = {}
    file = open(filename, 'r')
    file.readline()
    for line in file:
      track_info = line.strip().split(',')
      scores = (float(track_info[INPUT_TEMPO]), int(track_info[INPUT_POPULARITY]), float(track_info[INPUT_DANCEABILITY]), float(track_info[INPUT_ENERGY]))
      if len(track_info[INPUT_GENRE]) == 0:
        genres = []
      else:
        genres = track_info[INPUT_GENRE].split(':')
      track = (track_info[INPUT_TRACK_ID], track_info[INPUT_TITLE], track_info[INPUT_ARTIST], int(track_info[INPUT_DURATION]), genres, scores)
      track_id_to_information[track[TRACK_ID]] = track
      for genre in genres:
        if genre not in genre_to_track_ids:
          genre_to_track_ids[genre] = [track[TRACK_ID]]
        else:
          genre_to_track_ids[genre].append(track[TRACK_ID])
    return (genre_to_track_ids, track_id_to_information)
    file.close()

def make_playlist(filename: str, logenres: list[str], loartists: list[str], score_type: str, threshold: float) -> tuple[list[str], Time]:
    """ creates a playlist of all tracks that fit the given criteria below,
    returns a sorted list of the track titles and the duration of the playlist

    Criteria: the titles added to the playlist must...
    - have at least one of the given genre(s) in logenres.
      If no genre is specified (empty list), all genres in library are valid;
    - have at least one of the given artist(s) in loartists.
      If no artist is specified (empty list), all artists in library are valid;
    - have the given score_type value above the given threshold

    Preconditions:
     - given genre terms must match case exactly.
       For example: 'blues' doesn't match 'Blues'
     - given artist ignores case:
         ('lorDE' is found in 'Lorde'),
       and matches on a substring:
         ('marley' is found in 'Bob Marley & The Wailers' and 'Ziggy Marley')
     - score_type is one of: 'tempo', 'popularity', 'danceability', 'energy'

    You MUST call read_file and use look ups in the returned dictionaries
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.


    >>> make_playlist('0lines_data.csv', [], [], 'tempo', 0.2)
    ([], (0, 0, 0))

    >>> make_playlist('20lines_data.csv', \
                       [], [], 'tempo', 0.2)  # doctest: +NORMALIZE_WHITESPACE
    (['"Await The Kings Justice - From The ""Game Of Thrones"" Soundtrack"',
      'Bravado',
      'Cant Dweet Again',
      'Earthlings',
      'El Tiempo Es Dinero - Remasterizado 2007',
      'Fewerdolr',
      'Get Up  Stand Up - Thievery Corporation Remix',
      'Growing Pains',
      'Its You - Radio Edit',
      'Let It Be Me (feat. Ava Max)',
      'Lost Our Way',
      'Love U 4 Life',
      'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
      'Nobody (feat. Athena Cage) - Remastered Single Version',
      'See Dem Fake Leaders - Dub Remix',
      'She Knows How To Rock Me',
      'Still Got Time',
      'Thanksgiving Chicken',
      'The Fool and Me - 2007 Remaster',
      'Zangiefs Theme'],
     (69, 9, 370))


    >>> make_playlist('20lines_data.csv', \
                       ['Dance', 'Pop', 'Reggae', 'not found'], \
                       [], 'tempo', 0.2)  # doctest: +NORMALIZE_WHITESPACE
    (['Bravado',
      'Cant Dweet Again',
      'Earthlings',
      'Get Up  Stand Up - Thievery Corporation Remix',
      'Growing Pains',
      'Its You - Radio Edit',
      'Let It Be Me (feat. Ava Max)',
      'Lost Our Way', 'Love U 4 Life',
      'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
      'Nobody (feat. Athena Cage) - Remastered Single Version',
      'See Dem Fake Leaders - Dub Remix', 'Still Got Time'],
     (50, 54, 299))

    >>> make_playlist('20lines_data.csv', \
                       [], \
                       ['zayn', 'Marley', 'not there', 'LORDE', 'robin'], \
                       'tempo', 0.2)  # doctest: +NORMALIZE_WHITESPACE
    (['Bravado',
      'Get Up  Stand Up - Thievery Corporation Remix',
      'Natural Mystic - Banjamin Devigne Deep Jazz Remix',
      'See Dem Fake Leaders - Dub Remix',
      'Still Got Time',
      'The Fool and Me - 2007 Remaster'],
     (23, 56, 40))

    >>> make_playlist('20lines_data.csv', \
                       ['Dance', 'Pop', 'not found'], \
                       ['zayn', 'Marley', 'not there', 'LORDE'], \
                       'tempo', 0.2)  # doctest: +NORMALIZE_WHITESPACE
    (['Bravado',
      'Still Got Time'],
     (6, 49, 900))
    """
    genre_to_track_ids, track_id_to_information = read_file(filename)

    track_ids__with_genres = get_track_ids__with_genres(track_id_to_information, genre_to_track_ids, logenres)
    track_ids_with_artists = get_track_ids_with_artists(track_id_to_information, track_ids__with_genres, loartists)
    track_ids_with_score_above = get_track_ids_with_score_above(track_id_to_information, track_ids_with_artists, score_type, threshold)

    track_ids_witout_repeats = []
    for track_id in track_ids_with_score_above:
      if track_id not in track_ids_witout_repeats:
        track_ids_witout_repeats.append(track_id)

    playlist_tracks = []
    for track_id in track_ids_witout_repeats:
      playlist_tracks.append(track_id_to_information[track_id])

    playlist_titles = []
    duration_ms = 0
    for track in playlist_tracks:
      playlist_titles.append(track[TITLE])
      duration_ms += track[DURATION]
    playlist_titles.sort()
    duration = get_length_of_playlist(playlist_tracks)
    return (playlist_titles, duration)

def get_length_of_playlist(lotracks: list[MusicTrack]) -> tuple[int, int, int]:
  '''
  Takes a list of music track tuples and returns the total duration converted to minutes, seconds and milliseconds.
    
  >>> t1 = ('00021Wy6AyMbLP2tqij86e', 'Party', \
  'Bad Bunny', 189837, ['Latin trap', 'Reggaeton'], (475.578, 34, 0.382, 0.918))
    
  >>> t2 = ('001CyR8xqmmpVZFiTZJ5BC', 'Lemon Tree', \
  'Post Malone', 218293, ['Hip hop'], (43.832, 21, 0.384, 0.774))
    
  >>> t3 = ('7zmleW3XZx0uUsL2CkFuDe', 'Honest', 'Justin Bieber', \
  285200, ['R&B', 'Rap', 'Pop'], (135.414, 55, 0.592, 0.569))
    
  >>> tracks = [t1, t2, t3]
    
  >>> get_length_of_playlist(tracks)
  (11, 33, 330)
  '''
  total_duration_ms = 0
  for track in lotracks:
    total_duration_ms += track[DURATION]
  minutes = total_duration_ms // (SECONDS_PER_MINUTE * MS_PER_SECOND)
  remainder = total_duration_ms % (SECONDS_PER_MINUTE * MS_PER_SECOND)
  seconds = remainder // MS_PER_SECOND
  milliseconds = remainder % MS_PER_SECOND
  return (minutes, seconds, milliseconds)

def get_track_ids__with_genres(track_id_to_information: dict[str, MusicTrack], genre_to_track_ids: dict[str, list[str]], logenres: list[str]) -> list[str]:
  '''
  Returns a list of track ids that contain at least one genre in logenres.
  '''
  track_ids__with_genres = []
  if logenres == []:
    for track_id in track_id_to_information:
      track_ids__with_genres.append(track_id)
  else:
    for genre in logenres:
      if genre in genre_to_track_ids:
        track_ids__with_genres += genre_to_track_ids[genre]
  return track_ids__with_genres

def get_track_ids_with_artists(track_id_to_information: dict[str, MusicTrack], track_ids__with_genres: list[str], loartists: list[str]) -> list[str]:
  '''
  Takes a list of track ids and returns a list only of tracks that also contain an artist from loartists.
  '''
  track_ids_with_artists = []
  if loartists == []:
    track_ids_with_artists = track_ids__with_genres
  else:
    for track_id in track_ids__with_genres:
      track_artist = track_id_to_information[track_id][ARTIST]
      for artist in loartists:
        if artist.lower() in track_artist.lower():
          track_ids_with_artists.append(track_id)
          break
  return track_ids_with_artists

def get_track_ids_with_score_above(track_id_to_information: dict[str, MusicTrack], track_ids_with_artists: list[str], score_type: str, threshold: float) -> list[str]:
  '''
  Takes a list of track ids and returns a list only of tracks that contain the specified score type above the treshold.
  '''
  track_ids_with_score_above = []
  for track_id in track_ids_with_artists:
    scores = track_id_to_information[track_id][SCORES]
    if score_type == 'tempo':
      score = scores[TEMPO]
    elif score_type == 'popularity':
      score = scores[POPULARITY]
    elif score_type == 'danceability':
      score = scores[DANCEABILITY]
    else:
      score = scores[ENERGY]
    if score > threshold:
      track_ids_with_score_above.append(track_id)
  return track_ids_with_score_above
