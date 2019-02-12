# changing index value from a string using list and join
def mutate_string_using_list(string, position, character):
      newString = list(string)
      newString[position] = character
      return ''.join(newString)

# changing index value from a string using slice
def mutate_string(string, position, character):
      newString = string[:position] + character + string[position+1:]
      return newString

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
