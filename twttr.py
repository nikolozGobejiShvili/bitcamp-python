def main():
   text=input("input word :")
   print(shorten(text))
    


def shorten(word):
    text3=""

    for char in word:
      if  char not in "aeiouAEIOU":
         text3+=char
                 
    return text3


if __name__ == "__main__":
    main()