from lib.music_library import *
from lib.track import *

"""
When we add two tracks
We get the tracks back in the track list
"""
def test_adds_multiple_tracks_and_lists_them():
    music_library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.all() == [track_1, track_2]

    """
    When we add two tracks
    And we search for a word in the title
    We get the matching track back
    """
def test_searches_by_title():
    music_library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("Way") == [track_1]

    """
    When we add two tracks
    And we search for a small part of a word in the title
    We get the matching track back
    """
def test_searches_by_part_of_title():
    music_library = MusicLibrary()
    track_1 = Track("Always The Hard Way", "Terror")
    track_2 = Track("Higher Place", "Malevolence")
    music_library.add(track_1)
    music_library.add(track_2)
    assert music_library.search_by_title("lace") == [track_2]

"""
Initially there are no tracks
"""
def test_initially_has_no_tracks():
    music_library = MusicLibrary()
    assert music_library.all() == []

"""
Initially
Searching for tracks gets an empty list
"""
def test_initially_searches_return_empty():
    music_library = MusicLibrary()
    assert music_library.search_by_title("hello") == []