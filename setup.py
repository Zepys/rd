import pyautogui as pag
import time
import pyperclip

# Define the coordinates and use the `actions` list
actions = [
    (704, 509, 2),  # click next
    (450, 293, 10),  # additional
    (628, 414, 2),  # change pass
    (384, 253, 3),  # type pass
    (384, 299, 2),  # type pass
    (584, 595, 2),  # ok
    (371, 295, 2),  # change tab
    (532, 387, 3),  # right click (select all)
    (575, 451, 4),  # right click (copy)
          ]

# Wait for a few seconds to give time to focus on the target application
time.sleep(20)
password = "disalardp"
    
for x, y, duration in actions:
        if (x, y, duration) == (384, 253, 3):
            pag.click(x, y, duration=duration)
            pag.typewrite(password)
        elif (x, y, duration) == (384, 299, 2):
            pag.click(x, y, duration=duration)
            pag.typewrite(password)
        elif (x, y, duration) == (532, 387, 3):
            pag.rightClick(x, y, duration=duration)
        else:
            pag.click(x, y, duration=duration)

def save_echo_to_batch(file_path, echo_text):
    with open(file_path, 'a') as file:
        file.write(f'\necho {echo_text}\n')

def save_command():
    clipboard_text = pyperclip.paste()
    password_echo = 'LiteManager Password : disalardp'  
    save_echo_to_batch('show.bat', f'LiteManager ID: {clipboard_text}')
    save_echo_to_batch('show.bat', password_echo)

if __name__ == "__main__":
    save_command()

print("Done , Log in Credintials is below")