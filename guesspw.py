n = 3
pw = 'a123456'
while True:
    n = n - 1
    user = input('please input your password!')
    if user == pw:
        print('sucess!')
        break
    else:
        print('wrong!you have ', n, 'times')
        if n == 0:
            break
                