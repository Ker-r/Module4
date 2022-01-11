from dataset import users, countries

users_wrong_password = []

for user in users:
    if user['password']. isdigit():
        users_wrong_password.append({'name': user['name'], 'mail': user['mail']})
    

girls_drivers = []

for user in users:
    friends = user.get('friends', [])
    for friend in friends:
      if friend['sex'] == 'F' and friend.get('cars'):
          girls_drivers.append(friend['name'])


max_salary = 0
best_occupation = []

for user in users:
    friends = user.get('friends', [])
    for friend in friends:
        job = friend['job']
        salary = job['salary']
        if salary > max_salary:
            max_salary = salary
            best_occupation.append({'occupation': job['occupation'], 'salary': job['salary']})


vip_user = []

for user in users:
    friends_total_salary = 0
    friends = user.get('friends', [])
    for friend in friends:
        friends_total_salary += friend['job']['salary']
        vip_user = user['name']


avg_flights = []
friends_with_car = 0
total_journeys = 0

for user in users:
    friends = user.get('friends', [])
    for friend in friends:
        if friend.get('cars'):
            friends_with_car += 1
            total_journeys += len(friend.get('flights', []))

avg_flights = round(total_journeys / friends_with_car, 5)

i = 0
while i < len(users):
    need_remove = False
    friends = users[i].get('friends', [])
    for friend in friends:
      flights = friend.get('flights', [])
      for flight in flights:
          if flight['country'] in countries:
              need_remove = True
              break
      if need_remove:
        break
    if need_remove:
        del users[i]
    else:
        i += 1



