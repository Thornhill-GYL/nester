""" this is a way to show your
    list which includes a multiple-line in comment in your code"""
def print_lol(the_list):
    """ using the bif isinstance to judge
    the index whether a list"""
    for outside in the_list:
        if isinstance(outside,list):
            print_lol(outside)
        else:
            print(outside)
