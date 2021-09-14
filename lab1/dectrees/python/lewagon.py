def spinWords(string):
  new_string = ""
  string_list = string.split()
  for word in string_list:
    if len(word) >= 5:
      word = word[::-1]
    new_string += word + " "
  return new_string

spinWords("Hey fellow Le Wagon alumni")
