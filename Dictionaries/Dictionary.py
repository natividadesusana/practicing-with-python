users = {}
print(users)

users = {
    'chaves' : { 'Chaves do 8', '14/02/2022', 'Recep_01'},
    'quico' : {'Quico das Flores', '10/02/2022', 'Raiox_03'}
}
print(users)

users['florinda'] = ['Dona Florinda', '14/02/2022', 'Raiox_01']
print(users)

print('####----####')
print(users.get('quico'))