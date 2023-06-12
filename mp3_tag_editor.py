# 참고사이트 : https://commonengineerr.tistory.com/15

import eyed3

# 곡 정보 입력
mp3 = "Tesla - Love Song.mp3"
artist = "Tesla"
title = "Love Song"

# 곡 정보 수정
audiofile = eyed3.load(mp3)
audiofile.tag.artist = artist
# audiofile.tag.album = "Free For All Comp LP"
audiofile.tag.album_artist = artist
audiofile.tag.title = title
# audiofile.tag.track_num = 3

# 곡 정보 저장
audiofile.tag.save()