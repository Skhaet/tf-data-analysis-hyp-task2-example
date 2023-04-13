import pandas as pd
import numpy as np

import scipy.stats as st
chat_id = 270620880 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    res = st.anderson_ksamp([x, y])
    a = 0.06
    ret = True
    #ret = (res.pvalue <= a)
    return  res.pvalue <= 0.06 # Ваш ответ, True или False
