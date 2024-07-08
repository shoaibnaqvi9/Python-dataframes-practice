import pandas as pd

bio_data={'firstname':['Shoaib','Ali','Ahmed','Fahad','Sohail','Rabia','Fahad','Ali'],
          'lastname':['Naqvi','Khan','Ali','Mustafa','Khan','Anum','Mustafa','Kamran'],
          'gender':['Male','Male','Male','Male','Male','Female','Male','Male'],
          'Age':[21,21,30,21,25,42,30,42],
          'Height':[6.1,5.7,5.2,5.8,5.7,5.4,6.0,5.6],
          'Weight':[70,75,66,80,98,102,98,87]
          }

bio_data_frame=pd.DataFrame(bio_data)
print(bio_data_frame)
# print(bio_data_frame.head())
# print(bio_data_frame.info())
# print("Mean:\nHeight:",bio_data_frame['Height'].mean(),"Weight:",bio_data_frame['Weight'].mean(),"Age:",bio_data_frame['Age'].mean())
# print("Mode:\nHeight:",bio_data_frame['Height'].mode(),"Weight:",bio_data_frame['Weight'].mode(),"Age:",bio_data_frame['Age'].mode())
# print("Min:\nHeight:",bio_data_frame['Height'].min(),"Weight:",bio_data_frame['Weight'].min(),"Age:",bio_data_frame['Age'].min())
# print("Max:\nHeight:",bio_data_frame['Height'].max(),"Weight:",bio_data_frame['Weight'].max(),"Age:",bio_data_frame['Age'].max())
# print("Sum:\nAge:",bio_data_frame['Age'].sum())
# print("Quantile:\nAge:",bio_data_frame['Age'].quantile())
# def pct20(col):
#     return col.quantile(0.2)
# print("Aggregate:\nAge:",bio_data_frame['Age'].agg(pct20))
# print("Cummulative sum:\nAge:",bio_data_frame['Age'].cumsum())
# print("Cummulative max:\nAge:",bio_data_frame['Age'].cummax())
# print("Cummulative min:\nAge:",bio_data_frame['Age'].cummin())
# print("Cummulative prod:\nAge:",bio_data_frame['Age'].cumprod())
    # unique=bio_data_frame.drop_duplicates(subset=['firstname','lastname'])
# print(unique)
# print(bio_data_frame['Age'].value_counts(sort=True))
print(bio_data_frame['Age'].value_counts(normalize=True))

