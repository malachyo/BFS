# def unique_in_order(sequence):
#     pos = 0
#     newstr = ""
#     for x in sequence:
#         pos += 1
#         x = pos
#         if x == pos-1:
#             newstr = sequence.replace(x, "")
#
#     print(newstr)
#
#
# unique_in_order('AAABCBDBAABDBDCC')

def unique_in_order(sequence):


    sequence = " ".join(sequence)
    list = sequence.split()
    print(list)

    for x in list:
        if list.index(x) + 1 == list.index(x):
            list.remove(x)
        elif list.index(x) - 1 == list.index(x):
            list.remove(x)
    print(list)

unique_in_order('AAABCBDBAABDBDCC')
