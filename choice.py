# 入力した選択肢を選択する


import random

try:
    user_choice =  int(input('選択肢の数を入力してください：'))
except ValueError:
    print('数字を入力してください。')

print('\n選択肢の数は「{}」\n'.format(user_choice))


# ランダム
r = random.randint(0,int(user_choice - 1))


# 選択肢
choice_l = []
choice_d = {}

while int(user_choice) > 0:
    for i in range(user_choice):
        choice = input('選択肢{}：'.format(i + 1))
        user_choice -= 1

        choice_l.append(choice)
        choice_d[i] = choice_l[i]


# 解答
for key,value in choice_d.items():
    if user_choice == 1:
        print('\n今回の結果は、「{}」です。'.format(value))
    elif key == r:
        answer = value
        print('\n今回の結果は、「{}」です。'.format(answer))
    else:
        continue