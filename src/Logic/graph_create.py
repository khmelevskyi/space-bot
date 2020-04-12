import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


def main():
    date_df = pd.read_csv('~/repos/space-bot/datetime.csv')
    print(date_df['date'])
    #x_axis = pd.to_datetime(date_df['date'])
    #plt.hist(x_axis, bins=10)
    date_df['date'] = date_df['date'].astype('datetime64')
    for z in range(len(date_df)):
        if date_df.at[z, 'specialization'] == 'startup':
            date_df.at[z, 'startup'] = 1
        elif date_df.at[z, 'specialization'] == 'mentor':
            date_df.at[z, 'mentor'] = 1
        elif date_df.at[z, 'specialization'] == 'partner':
            date_df.at[z, 'partner'] = 1
    date_df[['startup', 'mentor', 'partner']].groupby([date_df['date'].dt.day, date_df['date'].dt.month]).count().plot(kind="bar")
    plt.savefig('graph.png', bbox_inches='tight')


if __name__ == '__main__':
    main()
