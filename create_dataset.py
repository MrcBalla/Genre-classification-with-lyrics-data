import pandas as pd
import os
import re
import numpy as np
import re
import math

def get_label(df):
    '''
    Function for get the main genre of a song given
    a list of genre. the main genre are 3: pop, rock, 
    rap
    '''

    genre_dict={}
    genre_dict['rock']=np.zeros(len(df['genre']))
    genre_dict['pop']=np.zeros(len(df['genre']))
    genre_dict['rap']=np.zeros(len(df['genre']))
    genre_dict['electro']=np.zeros(len(df['genre']))

    pattern=['rock', 'pop', 'rap', 'metal', 'hip','punk', 'disco', 'dance', 'trap', 'r&b', 'boy band', 'boyband', 'soul', 'reb', 'edm', 'house']

    for index,elem in enumerate(df['genre']):
        for word in elem.split():
            for chair in pattern:
                if word.find(chair)!=-1:
                    if chair=='punk':
                        genre_dict['rock'][index]=genre_dict['rock'][index]+1
                    elif chair=='hip':
                        genre_dict['rap'][index]=genre_dict['rap'][index]+1
                    elif chair=='metal':
                        genre_dict['rock'][index]=genre_dict['rock'][index]+1
                    elif chair=='disco':
                        genre_dict['pop'][index]=genre_dict['pop'][index]+1
                    elif chair=='house':
                        genre_dict['pop'][index]=genre_dict['pop'][index]+1   
                    elif chair=='dance':
                        genre_dict['pop'][index]=genre_dict['pop'][index]+1 
                    elif chair=='trap':
                    	genre_dict['rap'][index]=genre_dict['rap'][index]+1 
                    elif chair=='blues':
                    	genre_dict['rock'][index]=genre_dict['rock'][index]+1 
                    elif chair=='boyband':
                    	genre_dict['pop'][index]=genre_dict['pop'][index]+1 
                    elif chair=='boy band':
                    	genre_dict['pop'][index]=genre_dict['pop'][index]+1
                    elif chair=='r&b':
                    	genre_dict['rock'][index]=genre_dict['rock'][index]+1  
                    elif chair=='soul':
                    	genre_dict['pop'][index]=genre_dict['pop'][index]+1 
                    elif chair=='reb':
                    	genre_dict['rock'][index]=genre_dict['rock'][index]+1 
                    elif chair=='edm':
                     	genre_dict['pop'][index]=genre_dict['pop'][index]+1 
                    else:
                        genre_dict[chair][index]=genre_dict[chair][index]+1
    genre_label={}
    for elem in df.index:
        genre_label[elem]=None
        
    saved_value=0

    for elem in df.index:
        for key in genre_dict.keys():
            if genre_dict[key][elem]>saved_value:
                genre_label[elem]=key
                saved_value=genre_dict[key][elem]
            
        if saved_value==0:
            
            for key in genre_dict.keys():
            	if re.search("\\w*{}\\w*\\b".format(key), file)!=None:
                    print(key)
                    genre_label[elem]=key
                    break
            
        
        saved_value=0

    df['genre_label']=genre_label
    
    return df

path=os.getcwd()

for index,file in enumerate(os.listdir(path+"/dataset/data")):
    print(file)
    if index==0:
        df_a=pd.read_csv(path+"/dataset/data/"+file)
        print(df_a)
        df_a=get_label(df_a)
    else:
        df_tmp=pd.read_csv(path+"/dataset/data/"+file)
        df_tmp=get_label(df_tmp)
        df_a=pd.concat([df_a, df_tmp])


df_a.to_csv("spotify_data.csv")

print('----------')

for index,file in enumerate(os.listdir(path+"/dataset/lyrics")):
    print(file)
    if index==0:
        df_b=pd.read_csv(path+"/dataset/lyrics/"+file)
    else:
        df_tmp=pd.read_csv(path+"/dataset/lyrics/"+file)
        df_b=pd.concat([df_b, df_tmp])

pd.merge(df_a, df_b, on='track_uri').to_csv('final_df.csv')

df_b.to_csv("spotify_lyrics.csv")
