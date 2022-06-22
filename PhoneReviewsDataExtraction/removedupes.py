import pandas as pd

#change for getting rid of the duplicates
# data = pd.read_csv('ReviewsSecondTrial.csv')
# data.drop(data.columns[0], inplace=True, axis=1)
# data.to_csv('AllReviewsFinal.csv')
# with open('AllReviewsFinal.csv','r') as in_file, open('NoDupes.csv.csv','w') as out_file:
#    # read_csv function which is used to read the required CSV file
#     seen = set() # set for fast O(1) amortized lookup
#     for line in in_file:
#         if line in seen:
#             continue # skip duplicate
#         seen.add(line)
#         out_file.write(line)


#changes for getting spceifications
#keep only id and name in a new csv
# df = pd.read_csv('AllReviewsFinal.csv')
# df = pd.DataFrame(df)
# df.drop([df.columns[0],'review_score','review_title','review_content'], inplace=True, axis=1)
# df.to_csv('droped.csv')

#remove duplicates
df = pd.read_csv('AllReviewsFinal.csv')
df.drop(df['id'])
print(df)
df.to_csv('new.csv')
#save the data
# df.to_csv('unique_name_ids.csv')