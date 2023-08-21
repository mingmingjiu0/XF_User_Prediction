# 特征工程
## 分析用户特征和行为特征
if zero_list:
    df_split[f'{col}_split_0'] = df_split[col].apply(lambda x: 1 if x in zero_list else 0)
if one_list:
    df_split[f'{col}_split_1'] = df_split[col].apply(lambda x: 1 if x in one_list else 0)
# 模型选择
## 使用catboost能够缓解过拟合情况，但目前仍未解决0.98-0.83
model = CatBoostClassifier(
    loss_function="Logloss",colsample_bylevel=0.8,subsample=0.8,l2_leaf_reg=5,scale_pos_weight = 6,
                           eval_metric="AUC",
                           learning_rate=0.1,
                           iterations=1000,
                           random_seed=3047,
                           early_stopping_rounds=100,
)
