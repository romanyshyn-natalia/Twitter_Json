import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl


def user_account():
    '''
    () -> str
    Function for getting user account as userinput.
    '''
    print('')
    account = input('Enter Twitter Account:')
    if (len(account) < 1):
        return False
    print(account)
    return account


def get_url(user_acc):
    '''
    str -> str
    Function for creating GET request
    '''
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': user_acc, 'count': '5'})
    return url


def get_data(url):
    '''
    str -> str
    Function for getting user data from url.
    '''
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    return data


def write_data(file, data):
    '''
    str, str -> str
    Function for writing data to json file.
    '''
    with open(file, "w") as file:
        file.write(data)


def main():
    user = user_account()
    data = get_data(get_url(user))
    return write_data('data.json', data)


if __name__ == '__main__':
    main()
