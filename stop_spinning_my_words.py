# Stop gninnipS My sdroW!

#Write a function that takes in a string of one or more words, and returns the
#same string, but with all five or more letter words reversed
#(Just like the name of this Kata). Strings passed in will consist of only
#letters and spaces. Spaces will be included only when more than one word is present.

#Examples:
#spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
#spinWords( "This is a test") => returns "This is a test"
#spinWords( "This is another test" )=> returns "This is rehtona test"

### Solution
def spin_words(sentence):
    if len(sentence) == 0:
        return None
    else:
        words = sentence.split(" ")
        for i,word in enumerate(words):
            if len(word) >=5:
                words[i] = reverse(word)
    return " ".join(word for word in words)


def reverse(word):
  l = len(word)
  r = ""
  for i in range(1,l+1):
      r += word[-i]
  return r
