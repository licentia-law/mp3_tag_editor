# 참고사이트 : https://commonengineerr.tistory.com/15

import eyed3

### 곡 정보 입력
mp3 = "Tesla - Love Song.mp3" # 파일명, .mp3도 같이 기입
artist = "Tesla" # 아티스트, 참여 아티스트
title = "Love Song" # 곡 제목
# album = "Album"
# track_num = 1 # 트랙 넘버

### 곡 정보 수정
audiofile = eyed3.load(mp3) # 곡 경로
audiofile.tag.artist = artist # 아티스트
audiofile.tag.album_artist = artist # 앨범 참여 아티스트
audiofile.tag.title = title # 곡 제목
# audiofile.tag.album = album # 앨범
# audiofile.tag.track_num = track_num # 트랙 넘버

### 곡 정보 저장
audiofile.tag.save()
