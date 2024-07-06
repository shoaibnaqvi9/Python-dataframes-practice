import pandas as pd

bio_data={'firstname':['Shoaib','Ali','Ahmed','Fahad','Sohail','Rabia'],
          'lastname':['Naqvi','Khan','Ali','Mustafa','Khan','Anum'],
          'gender':['Male','Male','Male','Male','Male','Female'],
          'Age':[23,21,30,22,25,43],
          'Height':[6.1,5.7,5.2,5.8,5.7,5.4],
          'Weight':[70,75,66,80,98,102]
          }

bio_data_frame=pd.DataFrame(bio_data)

print(bio_data_frame)
print("Mean:\nHeight:",bio_data_frame['Height'].mean(),"Weight:",bio_data_frame['Weight'].mean(),"Age:",bio_data_frame['Age'].mean())
print("Mode:\nHeight:",bio_data_frame['Height'].mode(),"Weight:",bio_data_frame['Weight'].mode(),"Age:",bio_data_frame['Age'].mode())
print("Min:\nHeight:",bio_data_frame['Height'].min(),"Weight:",bio_data_frame['Weight'].min(),"Age:",bio_data_frame['Age'].min())
print("Max:\nHeight:",bio_data_frame['Height'].max(),"Weight:",bio_data_frame['Weight'].max(),"Age:",bio_data_frame['Age'].max())
print()
