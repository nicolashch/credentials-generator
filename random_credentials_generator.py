import random
import string

class RandomCredentialsGenerator():

    def __init__(self,email_lenght,password_lenght):
        self.email_lenght = email_lenght
        self.password_lenght = password_lenght

    def email_generator(self):

        to_join = lambda x,y:x+y

        lower_letters = list(string.ascii_lowercase)
        digits = list(string.digits)

        characters_list = to_join(lower_letters,digits)
        new_email = []

        for i in range(self.email_lenght):
            random_char = random.choice(characters_list)
            new_email.append(random_char)

        new_email= "".join(new_email)
        email = new_email + '@test.com'
        return email

    def password_generator(self):

        characters_list = list(string.printable)
        del characters_list[-10:]
        new_password = []

        for i in range(self.password_lenght):
            random_char = random.choice(characters_list)
            new_password.append(random_char)

        new_password= "".join(new_password)
        return new_password

class Validation():
    def __init__(self,credential):
        self.credential = credential
        pass

    def input_lenght_validation(self,a,b):
        while True:
            credential_lenght = int(input(f'Please input {self.credential} lenght (between {a} and {b}): '))
    
            if a <= credential_lenght <= b:
                break
            else:
               print(f'Invalid {self.credential} lenght')
               True

        return credential_lenght   

class Console():

    def __init__(self):
        pass

    def welcome(self):

        print('WELCOME')
        print('This program will help you create ramdom email and password for your testing')
        print('______________________________________________________________________________')
    
    def goodbye(self,new_email,new_password):
        print('Your new email is: ' + new_email)
        print('Your new password is:' + new_password)


if __name__ == '__main__':

    Console().welcome()

    email_lenght = Validation('email').input_lenght_validation(1,10)
    password_lenght = Validation('password').input_lenght_validation(6,16)
    
    credentials = RandomCredentialsGenerator(email_lenght,password_lenght)
    new_email = credentials.email_generator()
    new_password = credentials.password_generator()

    Console().goodbye(new_email, new_password)



     