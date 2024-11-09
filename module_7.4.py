team1_num = 10
team2_num = 10
score_1 = 50
score_2 = 50
team1_time = 1552.512
team2_time = 1552.512

def challenge_result():
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result

def tasks_total():
    return score_1 + score_2

def time_avg():
    return (team1_time+team2_time)/tasks_total()



print('В команде Мастера кода участников: %s!' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num,team2_num))
print('Команда "Волшебники данных" решила задач: {}'.format(score_2))
print('Волшебники данных решили задачи за {} с!'.format(team1_time))
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result()}')
print(f'Сегодня было решено {tasks_total()} задач, в среднем по {time_avg()} секунды на задачу!')
