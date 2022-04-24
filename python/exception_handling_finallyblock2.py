try:
    print('inside try')
    exit()
except Exception as e:
    print('inside except ')
else:
    print('inside else')
finally:
    print('inside finally ')