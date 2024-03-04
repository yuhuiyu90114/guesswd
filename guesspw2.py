n = 3
pw = 'a123456'
while n > 0:
    n = n - 1
    user = input('please input your password!')
    if user == pw:
        print('sucess!')
        break
    else:
        if n > 0:
            print('wrong!you have ', n, 'times')
        else:
            print('wrong! you have no chance!')
        