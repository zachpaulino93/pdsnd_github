import time
import pandas as pd
import numpy as np

# city month and days list
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTHS = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']



def get_filters():

    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city=''
    while city not in ['washington', 'new york city', 'chicago']:
        city = input("enter a valid city: Washington, New York City, Chicago, : " ).lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month=''
    while month not in MONTHS:
         month = input("Enter a valid month: January, February, March, April, May, June, or all : " ).lower().strip()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=''
    while day not in DAYS:
        day = input("Enter a valid day: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all : ").lower().strip()

    print("\ncity is: ", city, ", Month is: ", month, ", Day is: ",day)
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day

    """
    # converting data to_datetime
    print("pulling in city data........")
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['dayofweek'] = df['Start Time'].dt.dayofweek

    # filtering by month
    if month != 'all':
         month = MONTHS.index(month)
         df = df[df['month'] == month]
         print('Requested month is', MONTHS[month])
    else:
        df['month']

    # filtering by day
    if day != 'all':
        day = (DAYS.index(day)) - 1
        df = df[df['dayofweek'] == day]
        print('Requested day is', DAYS[day])

    else:
         df['dayofweek']


    print("city data has been pulled in for: ", city)
    return df

print(load_data)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    start = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    cm = start.dt.month_name().mode()[0]
    print('Most common month is' ,cm)

    # TO DO: display the most common day of week
    cd = start.dt.weekday_name.mode()[0]
    print('Most common day of the week is' , cd)

    # TO DO: display the most common start hour
    ch = start.dt.hour.mode()[0]
    print('Most common start hour is' , ch)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # ss is for Start station for easy format
    ss = df['Start Station']
    # es end station for easy format
    es = df['End Station']

    # TO DO: display most commonly used start station
    print('Most commonly used Start Station is {}\n'.format(ss.mode()[0]))

    # TO DO: display most commonly used end station
    print('Most commonly used End Station is {}\n'.format(es.mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    mostcom =  df.groupby(['Start Station','End Station']).size().nlargest(1)


    print('Most common start and end station combo\n',mostcom)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    # converting trip duration to time
    td = sum(df['Trip Duration'])
    s1 = td // 60
    h1 = s1 // 60
    d1 = h1 // 24
    # TO DO: display total travel time
    print('\nTotal trip durationsin in, min {}, hrs {} and days {},'.format(s1, h1, d1))

    # TO DO: display mean travel time
    td2 = int(df['Trip Duration'].mean())
    # converting trip duration to time
    s2 = td2 // 60
    h2 = s2 // 60
    d2 = h2 // 24
    print('\nAverage time of trips in min {}, hrs {} and days {},'.format(s2, h2, d2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usr = df['User Type'].value_counts()
    sub = usr['Subscriber']
    cx = usr['Customer']

    print("\nDisplaying total user counts,\n \nThere are {} Subscribers and {} normal Customers.".format(sub, cx))

    if 'Gender' in df.columns:
        gender = df['Gender'].fillna(0)
     # TO DO: Display counts of gender
        gndr = gender.value_counts()
        fmale = gndr['Female']
        male = gndr['Male']

        print("\nThere are {} Females, and {} Males useing bikeshare here!".format(fmale, male))
    else:
        print('\n Sorry but there is no gender data at this time.')

    if 'Birth Year' in df.columns:
    # TO DO: Display earliest, most recent, and most common year of birth
        bday = df['Birth Year']
        # earliest birth year
        eb = int(min(bday))
 #  print('\nThe earliest Birth Year is {}'.format(eb))
        # most recent birth year
        mr = int(max(bday))
        print('\nThe most recent Birth Year is {}'.format(mr))
     # most common birth year
        mcb = int(bday.mode()[0])
        print('\nThe most common Birth Year is {}'.format(mcb))

    else:
       print('\n Sorry but there is no birth year data at this time.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):


    count = 0
    n = count

    while True:
        answer = str(input('Type yes to see 5 lines of raw data, if not type no : ').lower().strip())
        if answer == str(('yes')):
            count += 5
            print(df.iloc[0:].head(count))
        else:
            answer == str(('no'))
            break
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks for using our bikeshare data services, have a great day!')
            break


if __name__ == "__main__":
	main()
