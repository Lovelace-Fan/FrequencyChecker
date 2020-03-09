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
#from the tune and returns a dictionary of words and their frequencies
def count_of_special_words(tune,words):
    word_counter = {}
    sv = 0
    for word in words:
        current = tune.count(word)
        sv += current
        word_counter[word] = current
       
    word_counter["combined"] = sv
    
    return word_counter

#This function simple retrieves a dictionary of percentage values for each special word as well as the combined percentage 
def get_percentages(total_words, special_words_count):
    percentages = {}
    for entry in special_words_count:
        percentages[entry] = str(round(special_words_count[entry] / total_words * 100, 2)) + "%"
    return percentages

filename = input("Type in the name of your file with the song lyrics: ")
print()
song = get_song(filename)
special_words = input("Type in the word(s) you want to check the frequency of separated by a space: ").split()
print()

filler = int(input("Type in an estimate of words that should not be a part of your total count (just type in 0 if this does not apply or unsure): "))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

words_in_the_song = words_in_the_song(song,filler)
print('There are {} total words in the song.'.format(words_in_the_song))
print()


sw_counter = count_of_special_words(song, special_words)


print("The count of each word in the song is:", sw_counter )
print()
print("The percentages for each word are:",get_percentages(words_in_the_song, sw_counter ))

