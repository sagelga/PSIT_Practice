"""This program will try to match the sentence with the number provided."""
def major_branch():
    """This is the main fuction. It will do everything."""
    var_a = int(input())
    var_b = int(input())
    if var_a % 2 == 0:
        if int(input()) == var_b:
            print("My heart goes Sha la la lal la")
            print("clap clap clap")
        else:
            if var_b >= 0:
                print("My heart will go on and on")
                print("uh hmm ummm")
            else:
                print("My heart goes Sha la la la Just for you")
    else:
        if var_b % 2 == 0:
            print("What's in your head!! In your head!!")
        else:
            print("What's in your head!! Zombie Zombie!")
            print("Zombie ei ei eh oh!")
major_branch()
