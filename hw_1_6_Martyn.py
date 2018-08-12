"""
	1. Найти результат выражения для произвольных значений a,b,c: a + b * ( c / 2 )
	2. Найти результат выражения для произвольных значений a,b: (a^2 + b^2) % 2
	3. Найти результат выражения для произвольных значений a,b,c: ( a + b ) / 12 * c % 4 + b
	4. Найти результат выражения для произвольных значений a,b,c: (a - b * c ) / ( a + b ) % c
	5. Найти результат выражения для произвольных значений a,b,c: | a - b | /( a + b)^3 - cos( c )
	6. Найти результат выражения для произвольных значений a,b,c: ( ln( 1 + c ) / -b )^4+ | a |

"""
import math
a = 3
b = 4
c = 5

print ('For a = %d, b = %d, c = %d' % (a, b, c))

# 1
count = 1
r = a + b * (c / 2)
print('%s.  a+b*(c/2) = %19.2f'
      % (count, r))

# 2
count = count+1
r = (a ** 2 + b ** 2) % 2
print('%s. (a^2+b^2)%%2 = %18.2f'
      % (count, r))

# 3
count = count+1
r = (a + b) / 12 * c % 4 + b
print('%s. (a+b)/12 * c mod 4 + b =  %6.2f'
      % (count, r))

# 4
count = count+1
r = (a - b * c) / (a + b) % c
print('%s. (a-b*c)/(a+b)mod c =  %10.2f'
      % (count, r))

# 5
count = count+1
r = math.fabs(a - b) / (a + b) ** 3 - math.cos(c)
print('%s. |a-b|/(a+b)^3-cos(c) =  %8.2f'
      % (count, r))


# 6
count = count+1
r = (math.log(1 + c) / -b) ** 4 + math.fabs(a)
print('%s. (ln(1+c)/-b)^4+|a| =  %10.2f'
      % (count, r))
