from datetime import date

users = [
    {
        'email' : 'ana@gmail.com',
        'first_name' : 'Ana',
        'last_name' : 'Ibarra',
        'password' : '123456789',
        'birthdate' :  date(2000,10,9),
        'bio' : 'Hello people',
        'country' : 'Mexico',
        'city' : 'Cuernavaca',
    },
    {
        'email' : 'memo@gmail.com',
        'first_name' : 'Alfonso',
        'last_name' : 'Aveiro',
        'password' : 'Iwantmoney',
        'birthdate' :  date(1984,2,5),
        'bio' : 'I don\'t have',
        'country' : 'Portugal',
        'city' : 'Funchal',
    },
    {
        'email' : 'leonardo@gmail.com',
        'first_name' : 'Leonardo',
        'last_name' : 'DiCaprio',
        'password' : 'MYOSCAR!',
        'birthdate' :  date(1974,11,11),
        'bio' : 'Where is my second oscar',
        'country' : 'Unites States',
        'city' : 'California',
    },
    {
        'email' : 'leila@gmail.com',
        'first_name' : 'Leila',
        'last_name' : 'Mendoza',
        'password' : 'pipiypopo',
        'birthdate' :  date(2017,2,3),
        'country' : 'Unites States',
        'city' : 'California',
    },
    {
        'email' : 'casinomiro@outlook.com',
        'first_name' : 'casinomiro',
        'last_name' : 'enlasnoches',
        'password' : 'django',
        'birthdate' :  date(2017,2,3),
        'country' : 'Canada',
        'city' : 'Vancouver',
    }
]

from posts.models import User

for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk,': ', obj.email)