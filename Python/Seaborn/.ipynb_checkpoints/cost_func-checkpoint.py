# sampleデータはnumpyで渡す？それともdf？
def cost_func(theta, data):
    """
    args:
        theta: parameter of regression
        data: sample data(target variable, feature value).allay like.
    return value of cosut function
    """
    # サンプルデータ数を定義
    m = len(data)
    
    