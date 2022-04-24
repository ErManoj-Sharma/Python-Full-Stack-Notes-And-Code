from itertools import zip_longest
name=['abd','dhoni','virat','rohit']
run=[700,200,220,450]
country=['sa','ind','ind','ind']
iplf=['rcb','csk']

player_info=list(zip_longest(name,run,country,iplf) )
#filvalue='#'
print(player_info)