import pandas as pd
import numpy as np

bio_data={'firstname':['Shoaib','Ali','Sania','Fahad','Sohail','Rabia','Fahad','Ali'],
          'lastname':['Naqvi','Khan','Ali','Mustafa','Khan','Anum','Mustafa','Kamran'],
          'gender':['Male','Male','Female','Male','Male','Female','Male','Male'],
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
# print(bio_data_frame['Age'].value_counts(normalize=True))
# print(bio_data_frame.groupby("gender")["Weight"].mean())
# print(bio_data_frame.groupby("gender")["Weight"].agg([min,max,sum]))
# print(bio_data_frame.groupby(["gender","Age"])[["Weight","Height"]].mean())
# store = np.array([7, 8, 4, 6])
# cost  = np.array([76, 87, 68, 88])
# np_cols =np.column_stack((store, cost))
# print(np_cols)
# np_heights = np.array([[1.60,1.75],[1.56,1.70],[1.49,1.68]])
# print(np.corrcoef(np_heights[:,0], np_heights[:,1]))
x = np.array([3.6, 3.99, 3.91])
print(np.std(x))