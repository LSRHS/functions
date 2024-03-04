#write a main function that:
  #takes a user text input
  #alllows the user to choose if they would like to
  #add elipses between words and/or
  #change text to upper case
#use the output of these functions to display the final text

def main():
  ...

#slow replaces spaces with elipses
def slow(text):
  slow_text = text.replace(" ", "...")
  return slow_text

#shout changes letters to uppercase
def shout(text):
  loud_text = text.upper()
  return loud_text

#prints the text input
def display(text):
  print(text)

main()
