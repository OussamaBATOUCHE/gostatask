import subprocess
import time

# Welcome 

def run_applescript(script):
    # run a block of AppleScript via osascript
    subprocess.run(["osascript", "-e", script], check=True)

def play_first_song_from_playlist(playlist_name):
    # open spotify
    subprocess.run(["open", "-a", "Spotify"])
    time.sleep(3)  # time to launch

    # bring it to front, otherwise we will be clicking elsewhere!
    run_applescript('tell application "Spotify" to activate')
    time.sleep(0.5)

    # AppleScript can do the rest ... 
    applescript = f'''
    -- prepare the query 
    set theQuery to "{playlist_name}"

    -- copy it into the clopboard, as the name contains ö,ä ...
    set the clipboard to theQuery

    tell application "System Events"
        -- focus search (cmd + l)
        keystroke "l" using {{command down}}
        delay 0.4

        -- paste the playlist name (cmd + v)
        keystroke "v" using {{command down}}
        delay 1.0

        -- search
        key code 36 -- enter
        delay 1.5

        -- move to the playlist component
        key code 48 -- tab
        delay 0.4

        -- click on it
        key code 36 -- enter
        delay 1.5
        
        -- move to the next component (profile !)
        key code 48 -- tab
        delay 0.4

        -- move to the play button 
        key code 48 -- tab
        delay 0.4

        -- hit enter
        key code 36 -- enter

    end tell
    '''

    # run the cmd above
    run_applescript(applescript)

    # thanks
    print(f'Searching and playing first song from playlist: "{playlist_name}"')

# give it a try !
play_first_song_from_playlist("Göstän parhaat")