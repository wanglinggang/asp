#This is python program for finding max and min number
def max_min(a,l):
    ans ={'max' : 0, 'min':0}
    ans_b1 = {'max': 0, 'min': 0}
    ans_b2 = {'max': 0, 'min': 0}
    half_l = l//2
    if l == 1:
        return {'max' : a[0] , 'min':a[0]}
    else:
        ans_b1 = max_min(a[:half_l],len(a[:half_l]))
        ans_b2 =max_min(a[half_l:],len(a[half_l:]))
        if ans_b1['max'] >=ans_b2['max']:
            ans['max'] = ans_b1['max']
        else:
            ans['max'] = ans_b2['max']
        if ans_b1['min'] <= ans_b2['min']:
            ans['min'] = ans_b1['min']
        else:
            ans['min'] = ans_b2['min']
        return ans

a = [-100 , 12 , 9 , -5 , 7 , 1, 0 ]
l = len(a)
ans = max_min(a , l)
print("max_number is:",ans['max'],"min_number is:",ans['min'])