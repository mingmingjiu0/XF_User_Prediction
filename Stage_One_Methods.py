# 拆分特征
df['时间'] = pd.to_datetime(df['common_ts'],unit='ms')
df['is_unknown'] = df['udmap'].apply(lambda x: 0 if x == 'unknown' else len(eval(x)))
df['udmap'] = df['udmap'].apply(lambda x : eval(x) if x != 'unknown' else dict())
df_split = pd.concat([df, df['udmap'].apply(pd.Series)], axis = 1).drop('udmap', axis = 1)
def time_feature(data: pd.DataFrame, pred_labels: list=None) -> pd.DataFrame:
    data = data.copy() # 复制数据，避免后续影响原始数据。
    data = data.drop(columns=["uuid"]) # 去掉”序号“特征。
    data["时间"] = pd.to_datetime(data["时间"]) # 将”时间“特征的文本内容转换为 Pandas 可处理的格式。
    data["day"] = data["时间"].dt.day # 添加新特征“day”，代表”当前日期“。
    data["hour"] = data["时间"].dt.hour # 添加新特征“hour”，代表”当前小时“。
    data["dayofweek"] = data["时间"].dt.dayofweek # 添加新特征“dayofweek”，代表”当周第几日“。
    data["is_weekend"] = data["时间"].dt.dayofweek // 6 # 添加新特征“is_weekend”，代表”是否是周末“，1 代表是周末，0 代表不是周末。

    data = data.drop(columns=["时间", "common_ts"])

    if pred_labels: # 如果提供了 pred_labels 参数，则执行该代码块。
        data = data.drop(columns=[*pred_labels]) # 去掉所有待预测的标签。
    return data # 返回最后处理的数据。
# 填充缺失值
## 填充nan
C_index = ['key1','key2','key3','key4','key5','key6','key7','key8','key9',]
for col_name in C_index:
    ## 需要注意的是分类变量的mode()取值为pandas.core.series.Series类型，需要提取才可以使用
    df_split[col_name] = df_split[col_name].fillna("-1")
# 特征工程
df_time['x3'] = df_time['x3'].apply(lambda x: 1 if x==41 else 0)
