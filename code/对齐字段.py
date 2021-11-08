
# 字段查询内容对齐
def get_info_from_df(df_p):
    df_p.loc[1, :] = df_p.columns
    df1 = df_p.applymap(lambda x: str(x))
    df2 = df1.applymap(lambda x: len(x) + 1)
    df1.loc[2, :] = df2.max(axis=0)
    df1 = df1.T

    str_format = ''
    for i in range(df1.shape[0]):
        str_format += "{:<" + str(df1[2][i]) + "s}|"
    data_info = str_format.format(*list(df1[0].values))
    col_name_info = str_format.format(*list(df1[1].values))
    
    list_total = []
    list_total.append(col_name_info)
    list_total.append(data_info)
    return list_total

