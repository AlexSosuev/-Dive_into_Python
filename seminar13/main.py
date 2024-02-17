from my_func import create_user_list

if __name__ == '__main__':
    user_list = create_user_list('workers.json')
    
    for user in user_list:
        print(user)