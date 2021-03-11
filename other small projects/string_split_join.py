#a challenge from hackerrank

#https://www.hackerrank.com/challenges/python-string-split-and-join/problem?h_r=next-challenge&h_v=zen
# new_line = ""
# line = "this is a string"
# split_line = line.split(" ")
#
# for word in split_line:
#     new_line+=word
#     if word != split_line[-1]:
#         new_line+="-"
# print(new_line)


#alternative simpler code

line = "this is a string"
split_list = line.split(" ")
new_string = "-".join(split_list)




print(new_string)




