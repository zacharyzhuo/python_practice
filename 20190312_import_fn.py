# 匯入整個模組
import pizza

pizza.make_pizza(16, 'pepperoni')

# 匯入特定的函式
from pizza import make_pizza

make_pizza(16, 'pepperoni')

# 使用as為函式指定別名
from pizza import make_pizza as mp

mp(16, 'pepperoni')

# 使用as為模組指定別名
import pizza as p

p.make_pizza(16, 'pepperoni')