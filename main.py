import pandas as pd

# import a csv from the world wide web
soccer_url = "https://raw.githubusercontent.com/BriChavez/FIFAWorldCup/master/squads.csv"
# read it into our trusty pandas df so we can clean it
df = pd.read_csv(soccer_url)

# set index as player name
df = df.set_index('Player')
# set column names
df.columns = ['Jersey_Num',
              'Position',
              'DOB_Age',
              'Caps',
              'Club',
              'Country',
              'ClubCountry',
              'Cup_Year']

# replace non integer values, in the column Caps, with 0
df['Caps'] = df['Caps'].str.replace('[^\w\s]', '0')
# extract words and numbers surrounded by parens. aka 'aged' and age value, in this instance
Age = df.DOB_Age.str.extract(r"\(([A-Za-z0-9 _]+)\)")
# assign the extracted aged info as a column to mess with further
df = df.assign(Age=Age)
# reassign our new column the extracted integers from that column, aka just the ages
df = df.assign(Age=lambda x: x['Age'].str.extract('(\d+)'))
# reassign as birthday the dob datetime object from inside parens
df = df.assign(Birthday=lambda x: x['DOB_Age'].str.extract(r"\(([0-9 _-]+)\)"))
# sorry boys, ya b-day is backward and i dont have time to figure that out
df = df.drop(
    # dropping the backward birthday boys
    index=['Walter Weiler', 'Samir Shaker Mahmoud', 'Medhi Lacen'])
# fill null numeric values with 0
df = df.fillna(0)
# fill null values from nonnumeric columns with n/a
df = df.fillna('n/a')
# force my will and turn my age column as an int
df.Age = df.Age.astype(int, errors='ignore')
# force my Caps column to turn into a int column, no matter what it says
df.Caps = df.Caps.astype(int, errors='ignore')
# set birthday as a datetime
df.Birthday = pd.to_datetime(df.Birthday)
# change cup year to a datetime
df.Cup_Year = pd.to_datetime(df.Cup_Year, format='%Y')
# dropping the wordy column as we got what we wanted from it.
df = df.drop(['DOB_Age'], axis = 1)
# check to see we did it right
df.info()
# write our df to a csv
df.to_csv('data/world_cup.csv')
