def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if sub_string == string[i:len(sub_string) + i]:
            count += 1
    return count


string="ABCDCDC"
sub_string="CDC"

count = count_substring(string, sub_string)
print(count)