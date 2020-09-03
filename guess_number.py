"""
猜词游戏
"""
import random


def guess_game():
    msg_start = '我想好了一个正整数！猜猜它是几：'
    msg_gt = '哥，大了大了！！再猜一次吧：'
    msg_lt = "哎，小了，小了~~再给你一次机会："
    msg_eq = "猜对了，你是我肚子里的蛔虫吗？但是没有奖励哦~~\n要不要再玩一次?（“好”/“不”）："
    msg_thx = "欢迎下次再来哦~~"
    num = random.randint(1, 100)
    guess_num = int(input(msg_start))
    while 1:
        if guess_num > num:
            guess_num = int(input(msg_gt))
        elif guess_num < num:
            guess_num = int(input(msg_lt))
        else:
            if input(msg_eq) == '好':
                num = random.randint(0, 100)
                guess_num = int(input(msg_start))
            else:
                break
    print(msg_thx)


if __name__ == '__main__':
    guess_game()
