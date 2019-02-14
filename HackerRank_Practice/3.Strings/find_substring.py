def count_substring(string, sub_string):
    cnt = 0
    for i in range(0, len(string)-1):
        newString = string[i:len(sub_string)+i]
        if newString == sub_string:
              cnt +=1
    return cnt


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
