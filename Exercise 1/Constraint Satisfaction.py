from itertools import chain, permutations
from string import digits
def solve_cryptarithm(addends, result):
    letters = ''.join(set(chain(result, *addends)))
    initial_letters = ''.join(set(chain(result[0], (a[0] for a in addends))))
    for perm in permutations(digits, len(letters)):
        decipher_table = str.maketrans(letters, ''.join(perm))
        def decipher(s):
          return s.translate(decipher_table)
        if '0' in decipher(initial_letters):
         continue 
        deciphered_sum = sum(int(decipher(addend)) for addend in addends)
        if deciphered_sum == int(decipher(result)):
            def fmt(s):
              return f"{s}({decipher(s)})"
            print(" + ".join(map(fmt, addends)), "=", fmt(result))
            break
    else:
        print(" + ".join(addends), "=", result, " : no solution")
    print('\n')
if __name__ == '__main__':
 print('\n')
 solve_cryptarithm(['SEND', 'MORE'], 'MONEY')
 solve_cryptarithm(['PUBG','CHILDREN'],'FUN')
 solve_cryptarithm(['BASE', 'BALL'], 'GAMES')
 solve_cryptarithm(['TWO', 'TWO'], 'FOUR')
 solve_cryptarithm(['CROSS', 'ROADS'], 'DANGER')
