def color(ohms):

    colors = ['black','black','black','gold']   # ex. of a color code, represents 0.
    arr = list(ohms)    # makes an array of the number provided, split into each digit.

    for i in range(1,6):
        arr.pop(-1)         # takes out, or pops, the first value of the array.

    pos = 0
    mul = 0
    for i in range(len(arr)):   # setting the meaning of each number in relation to its color.
        if arr[pos] == '0':
            colors[pos] = 'black'   # 0 signifies black
            mul = mul + 1
        elif arr[pos] == '1':
            colors[pos] = 'brown'   # 1 signifies brown
            mul = mul + 1
        elif arr[pos] == '2':
            colors[pos] = 'red'     # 2 signifies red
            mul = mul + 1
        elif arr[pos] == '3':
            colors[pos] = 'orange'  # 3 signifies orange
            mul = mul + 1
        elif arr[pos] == '4':
            colors[pos] = 'yellow'  # 4 signifies yellow
            mul = mul + 1
        elif arr[pos] == '5':
            colors[pos] = 'green'   # 5 signifies green
            mul = mul + 1
        elif arr[pos] == '6':
            colors[pos] = 'blue'    # 6 signifies blue
            mul = mul + 1
        elif arr[pos] == '7':
            colors[pos] = 'violet'  # 7 signifies violet
            mul = mul + 1
        elif arr[pos] == '8':
            colors[pos] = 'gray'    # 8 signifies gray
            mul = mul + 1
        elif arr[pos] == '9':
            colors[pos] = 'white'   # 9 signifies white
        elif arr[pos] == 'k':
            mul = mul + 3           # if the number of ohms contains unit 'k', it is converted into thousands.
        elif arr[pos] == 'M':
            mul = mul + 6           # if the number of ohms contains unit 'M', it is converted into millions.
        pos = pos + 1               # repeats this process for each value in arr.

    mul = mul - 2
    if mul == 0:                # multiplier that puts the value back into its thousand or million form.
        colors[2]= 'black'
    if mul == 1:
        colors[2]= 'brown'
    if mul == 2:
        colors[2]= 'red'
    if mul == 3:
        colors[2]= 'orange'
    if mul == 4:
        colors[2]= 'yellow'
    if mul == 5:
        colors[2]= 'green'
    if mul == 6:
        colors[2]= 'blue'
    if mul == 7:
        colors[2]= 'violet'
    if mul == 8:
        colors[2]= 'gray'
    if mul == 9:
        colors[2]= 'white'

    print(colors)


def run():
    color("10 ohms")
    color("100 ohms")
    color("220 ohms")
    color("330 ohms")
    color("470 ohms")
    color("680 ohms")
    color("1k ohms")
    color("10k ohms")
    color("22k ohms")
    color("47k ohms")
    color("100k ohms")
    color("330k ohms")
    color("2M ohms")

run()       # runs function color for each ohm value in the run function.
