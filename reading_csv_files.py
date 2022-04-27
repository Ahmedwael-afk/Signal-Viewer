import  pandas  as  pd
import matplotlib.pyplot as plt

# read only 10 rows from csv file
df = pd.read_csv("emg - Copy.csv", nrows=20)
#print(df.columns.tolist(),df)
chunks = []
print(len(df))
# print(chunks,type(chunks))
for chunk in pd.read_csv("top_secret.csv",chunksize = 50):
	i = chunk
	chunks.append(i)


print(chunks[2])
for j in range(len(chunks)):
	plt.plot(chunks[j])
	plt.draw()
	plt.pause(0.3)

								# for i,chunk in enumerate(pd.read_csv('emg - Copy.csv', chunksize=500)):
								#     chunk.to_csv('chunk{}.csv'.format(i), index=False)


# skip first 5 rows and read only 10 rows from csv file
# df = pd.read_csv("emg - Copy.csv", nrows=10, skiprows=5)