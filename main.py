import requests
import sys

def check_username(username):
    url = f"https://hackerone.com/{username}"
    try:
        response = requests.get(url)
        if response.status_code == 404:
            return True
        else:
            return False
    except requests.RequestException as e:
        print(f"Error checking username '{username}': {e}")
        return False

if __name__ == "__main__":
    try:
        with open('usernames.txt') as f:
            usernames = [line.rstrip() for line in f]
    except FileNotFoundError:
        print("Error: 'usernames.txt' file not found.")
        sys.exit(1)

    available_usernames = []
    for username in usernames:
        if check_username(username):
            available_usernames.append(username)
            print(f"The username '{username}' is available.")
            with open('available_usernames.txt', 'a') as f:
                f.write(username + '\n')
        else:
            print(f"The username '{username}' is not available.")
    
    print(f"\n{len(available_usernames)} usernames are available.")
