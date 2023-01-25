import pandas as pd

def max_common_my(df_a, df_b):
    result = df_a.copy()
    adder = df_b.copy()
    for ind in result.columns:
        adder['other_' + ind] = result[ind]
        if adder.columns.__contains__(ind):
            result[ind] = adder[[ind, 'other_' + ind]].max(axis=1)

    return result

def max_common(df_a, df_b):
    print(pd.concat([df_a, df_b]))
    print(pd.concat([df_a, df_b]).filter(items=df_a.columns))
    print(pd.concat([df_a, df_b]).filter(items=df_a.columns).groupby(level=0))
    print(pd.concat([df_a, df_b]).filter(items=df_a.columns).groupby(level=0).count())
    return pd.concat([df_a, df_b]).filter(items=df_a.columns).groupby(level=0).max()

df_a = pd.DataFrame(data=[[2.5, 2.0, 2.0], [2.0, 2.0, 2.0]], columns=list('ABC'))
df_b = pd.DataFrame(data=[[1.0, 6.0, 7.0, 1.0], [8.5, 1.0, 9.0, 1.0]], columns=list('CBDE'))
# df_out = pd.DataFrame(data=[[2.5, 6.0, 2.0], [2.0, 2.0, 8.5]], columns=list('ABC'))
print(max_common(df_a, df_b))