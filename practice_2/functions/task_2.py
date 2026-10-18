def check_winners(scores, student_score):
    top_three = sorted(scores, reverse=True)[:3]

    if student_score in top_three:
        print('Вы в тройке победителей!')
    else:
        print('Вы не попали в тройку победителей.')
