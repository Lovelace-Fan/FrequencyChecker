#This function parses in the text file with lyrics.
def get_song(name):
    file = open(name,"r")
    lyrics = ""
    
    for line in file:
        lyrics += line
        
    return lyrics

#This function approximates the number of words in the song. The second parameter 'excess' is to count
#for filler words that might innaccurately represent the total number of words (i.e. Chorus, Verse One, etc.)
def words_in_the_song(tune, excess):
    word_count = len(tune.split()) - excess
    return word_count

#This function counts the frequency of a single word or multiple words depending on the input
#from the song
def count_of_special_words(tune,words):
    count = 0
    for word in words:
        count += tune.count(word)
        
    return count

#This function simple retrieves a percentage value
def get_percentage(total_words, words):
    return words/total_words * 100

filename = input("Type in the name of your file with the song lyrics: ")
song = get_song(filename)
special_words = input("Type in the word(s) you want to check the frequency of separated by a space: ").split()
filler = int(input("Type in an estimate of words that should not be a part of your total count (just type in 0 if this does not apply): "))
words_in_the_song = words_in_the_song(song,filler)
special_word_count = (count_of_special_words(song, special_words))
print('The percentage for the words you wanted to check in the song is: {}%.'.format(round(get_percentage(words_in_the_song, special_word_count),2)))
