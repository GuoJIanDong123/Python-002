
# 自定义python函数，实现map函数功能

def new_map(func,data):
    res = []
    for i in data:
        res.append(func(i))
    return list(res)

if __name__ == '__main__':
    data01 = [1,2,3,4,5,6]
    result = new_map(lambda x:x+1,data01)
    print(result)