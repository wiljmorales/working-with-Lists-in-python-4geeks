def lyrics_generator(music_list):
  lyric = ""
  for i in range(len(music_list)):
    if music_list[i] == 0:
      lyric += "Boom "
    if music_list[i] == 1:
      lyric += "Drop the base "
    if music_list[i - 1] and music_list[i - 2] and music_list[i] and i >1:
      lyric += "!!!Break the base!!! "
  return lyric

# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))