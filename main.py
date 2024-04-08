# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. 
# Сможете ли вы это сделать без get_dummies?

# //////////////////////////////////////////////////////////////////////////////

# import pandas as pd
# # Создаем исходные данные
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})

# # Создаем словарь для one hot кодирования
# categories = list(set(data['whoAmI']))
# one_hot_encoding = {category: (data['whoAmI'] == category).astype(int) for category in categories}

# # Создаем DataFrame из словаря
# one_hot_df = pd.DataFrame(one_hot_encoding)

# one_hot_df.head()

# ///////////////////////////////////////////////////////////////////////////