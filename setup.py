import pyautogui as pag
import time
import pyperclip

# Define the coordinates and use the `actions` list
actions = [
    (713, 521, 2),  # click next
    (452, 297, 2),  # additional
    (626, 420, 2),  # change pass
    (399, 255, 3),  # type pass
    (398, 306, 2),  # type pass
    (563, 600, 2),  # ok
    (377, 299, 2),  # change tab
    (557, 393, 3),  # right click (select all)
    (540, 388, 4),  # right click (copy)
          ]

# Wait for a few seconds to give time to focus on the target application
time.sleep(2)
password = "disalardp"
    
for x, y, duration in actions:
        if (x, y, duration) == (399, 255, 3):
            pag.click(x, y, duration=duration)
            pag.typewrite(password)
        elif (x, y, duration) == (713, 521, 2):
            pag.click(x, y, duration=duration)
            time.sleep(10)
        elif (x, y, duration) == (398, 306, 2):
            pag.click(x, y, duration=duration)
            pag.typewrite(password)
        elif (x, y, duration) == (540, 388, 4):
            pag.rightClick(x, y, duration=duration)
            pag.click(593, 446, duration=2) # click copy
        elif (x, y, duration) == (557, 393, 3):
            pag.rightClick(x, y, duration=duration)
            pag.click(618, 527, duration=2) # click select all
        else:
            pag.click(x, y, duration=duration)

def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}\n')

def save_command():
    clipboard_text = pyperclip.paste()
    password_echo = 'Password : disalardp'  
    save_echo_to_batch('show.bat', f'LiteManager ID: {clipboard_text}')
    save_echo_to_batch('show.bat', password_echo)

if __name__ == "__main__":
    save_command()

print("Done , Log in Credintials is below")