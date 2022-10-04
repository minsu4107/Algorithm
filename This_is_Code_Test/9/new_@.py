from itertools import product


def solution(users, emoticons):
    answer = [0, 0]

    # for percents in list(product([10, 20, 30, 40], repeat=len(emoticons))):
    for percents in [[40, 40, 20, 40]]:
        total_price = 0
        total_plus = 0

        saled_emo = [emoticons[idx] * (100 - per) / 100 for idx, per in enumerate(percents)]

        for idx, (per_cut, price_cut) in enumerate(users):
            user_price = 0
            for p_idx, per in enumerate(percents):
                if per >= per_cut:
                    user_price += saled_emo[p_idx]
            if user_price >= price_cut:
                total_plus += 1
            total_price += user_price
            print(user_price)
        if total_plus > answer[0]:
            answer[0] = total_plus
            answer[1] = total_price
        elif total_plus == answer[0] and total_price > answer[1]:
            answer[1] = total_price

    return answer

asdf = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
emo = [1300, 1500, 1600, 4900]
print(solution(asdf, emo))