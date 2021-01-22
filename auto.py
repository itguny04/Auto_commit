# module
import os
import schedule
import time
import winsound

# function

    # init
def git_init():
    os.system("git init")
    print('git init')

    os.system("git add -A")
    print("git add -A")

    os.system("git commit -m 'init'")
    print("git commit -m 'init'")

    URL = input('URL: ')
    os.system(f"git remote add origin {URL}")
    os.system("git branch -M main")
    os.system("git push -u origin main")

    winsound.Beep(200,100)

    return

    # commit
def auto_commit():
    this_tm = time.localtime(time.time())

    os.system("git add -A")
    print("git add -A")
    os.system(f"git commit -m '{this_tm.tm_year}-{this_tm.tm_mon}-{this_tm.tm_mday}-{this_tm.tm_hour}:{this_tm.tm_min}'")
    print(f"git commit -m '{this_tm.tm_year}-{this_tm.tm_mon}-{this_tm.tm_mday}-{this_tm.tm_hour}:{this_tm.tm_min}'")
    os.system("git push")
    print("git push")

    winsound.Beep(200,100)

    return 

# schedule
schedule.every().day.at("12:00").do(auto_commit)
schedule.every().day.at("17:00").do(auto_commit)
schedule.every().day.at("23:00").do(auto_commit)

# Main
if __name__  == '__main__':

    if 'Y' == input('You need Init? Y or N (default: N): '):
        git_init()

    for i in range(4):
        winsound.Beep(150,300)

    print('!!! running !!!')

    while True:
        schedule.run_pending()
        time.sleep(1)

