#Comma Code

def fn(*list):
    for i in range(len(list)):
        if i<(len(list)-1):
            print(list[i], end= ",")
        else:
            print("and", list[i])
fn(*['apples', 'bananas', 'tofu', 'cats', 'rwrerge', '34qtw4tw'])
