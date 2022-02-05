# from E:\Documents H\EDU\Coding\Crash-Course-on-Python\Week 3\W3-02 For Loops\03-12 More for Loop Examples

# def to_celsius(x):
#    return (x-32)*5/9
#
# for x in range(0, 101, 10):
#    print(x, to_celsius(x))
#

def to_celsius(x):
    return (x-32)*(5/9)

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
