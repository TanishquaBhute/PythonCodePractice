def verify_login(user_name, password):
    """
    accepts user_name password and checks with internal user details
    :param user_name: username
    :param password:  password
    :return: bool true/false
    """

    with open('credentials.txt', 'r') as file:
        user_details = file.readlines()
    user_concat = f"{user_name}:{password}"   # Tanishqua:tanishqua123
    return user_concat in user_details


if __name__ == '__main__':
    print(verify_login('Tanishqua', 'tanishqua'))
"""
{
  'Tanishqua':{ 'password':'tanishqua123', 'user_type':'admin'
               },
}
"""