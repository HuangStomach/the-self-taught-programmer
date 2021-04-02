def s(x):
    """
    返回x的平方
    :param x:int
    """
    return x * x;

def p(x):
    """
    打印x
    :param x:string
    """
    print(x)

def select(a, b, c, x = 1, y = 2):
    """
    可选参数
    """
    return 1;

def a(x):
    """
    x除以2
    :param x:int
    """
    return x / 2
def b(x):
    """
    x乘以4
    :param x:int
    """
    return x * 4

def c(x):
    """
    x转换为float
    :param x:float
    """
    try:
        float(x)
    except (ValueError):
        print("Error")

print(b(a(2)))