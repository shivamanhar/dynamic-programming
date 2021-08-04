def count_substring(string, sub_string):
    find_str = string.find(sub_string)
    if find_str == -1:
        find_str = 0
    return find_str

if __name__ == '__main__':
    #string = raw_input().strip()
    #sub_string = raw_input().strip()
    string = 'WoW!ItSCoOWoWW'
    sub_string = 'oW'
    count = count_substring(string, sub_string)
    print(count)