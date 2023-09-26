def kwargs_to_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        try:
            result[value] = key
        except:
            result[str(value)] = key
    return result


print(kwargs_to_dict(name='Лиза', age=19,
                     has_work=True, commands=['ККН', 'LM', 'DP'],
                     growth=1.72, nicks={'STONE', '17th'}))