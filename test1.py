import subprocess,time


# opening Camera
subprocess.run('start microsoft.windows.camera:', shell=True)
time.sleep(2)
subprocess.run('Taskkill /IM WindowsCamera.exe /F', shell=True)

# opening Notepad
program = "notepad.exe"
subprocess.Popen(program)


# Testing internet
args = ["ping", "www.google.com"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
print(data)
with open('internet_Response.txt', 'w') as file:
    file.write(f'{data}')


url = 'www.google.com'

# Opening YouTube to test speakers
subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome.exe", 'www.youtube.com/watch?v=XqZsoesa55w'])
