import Insta3Unfollower
import Insta2




print('''Packages : 
                    1. Follow Application(Headless)
                    2. Unfollow Application(Headless)
                    
                    3. Follow Application(Head)
                    4. Unfollow Application(Head)\n''')

while(True):
    task = int(input("Enter the Sr. No. of task you want to perform : "))
    if task == 1:
        print("\nInstagram Follower(Headless) application initiated!\n")
        Insta2.follow_main(0)
        break
    elif task == 2:
        print("\nInstagram Unfollower(Headless) application initiated!\n")
        Insta3Unfollower.unfollow_main(0)
        break
    elif task == 3:
        print("\nInstagram Follower(Head) application initiated!\n")
        Insta3Unfollower.follow_main(1)
        break
    elif task == 4:
        print("\nInstagram Unfollower(Head) application initiated!\n")
        Insta3Unfollower.unfollow_main(1)
        break
    else:
        print("\nEnter a valid number please!\n")
        pass

