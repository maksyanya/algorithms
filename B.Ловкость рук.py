''' 
B.Ловкость рук.  



'''

def scoring_points(target, field, symbol='123456789', players=2):
    return sum(
        0 < field.count(number) <= target * players for number in symbol
    )

if __name__ == '__main__':
    print(scoring_points(
        int(input()),
        input() + input() + input() + input()))
    
