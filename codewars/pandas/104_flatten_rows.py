import pandas as pd

def flatten(dataframe, A):
    df = dataframe.copy()
    df = df.drop(df.index)
    for index, row in dataframe.iterrows():
        if isinstance(row[A], list):
            for l in row[A]:
                bla = row.copy()
                bla[A] = l
                df = df.append(bla, ignore_index=True)
        else:
            df = df.append(row, ignore_index=True)
            pass
    return df

d = pd.DataFrame(data=[[[1, 2],5], [['a', 'b', 'c'], 6], [77, 3]], columns=list('AB'))
column = 'A'
print(flatten(d, column))