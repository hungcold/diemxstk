import pandas as pd
data_frame = {"a":[-1,-5,6,3,9],"b":[-1,-5,6,3,7],"c":[-1,-5,6,3,7],"d":[-1,-5,6,3,7]}
df=pd.DataFrame(data_frame)

print(df)
print("In ra cột đầu")
print(df["a"])
print("In ra hàng đầu tiên")
print(df.loc[0])

