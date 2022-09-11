from posixpath import splitext
import wget
import pandas as pd

df = pd.read_csv('subreddits-csv/religiousfruitcake.csv')

# for ind in df.index:
#   splitText = (df["url"][ind].split())

# print(splitText)



for ind in df.index:
    try:
        url = df['url'][ind]
        file_name = wget.download(url, out = "religiousfruitcake/" + df['id'][ind] + '.jpg')
        print('Image Successfully Downloaded: ', file_name)
    except:
        print('Image Failed to Download: ', df['id'][ind] + '.jpg')


# url = 'https://i.redd.it/r0z490csggm91.gif'
# image_name = 'dankmemes/viplu.gif'
# # wget.download(url)

# file_name = wget.download(url, out = image_name)

# print('Image Successfully Downloaded: ', file_name)