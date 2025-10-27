
import time
import pandas as pd
import numpy as np
CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

def get_filters():
	"""First Edit by me to see that it works really good"""
	
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("Hello! Let's explore some US bikeshare data!")

    # Valid cities
    cities = ['chicago', 'new york city', 'washington']

    # Get user input for city
    while True:
        city = input("Please enter a city (chicago, new york city, washington): ").lower()
        if city in cities:
            break
        else:
            print("Invalid input. Please choose from chicago, new york city, or washington.")

    # Valid months
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    # Get user input for month
    while True:
        month = input("Enter a month (january to june) or 'all': ").lower()
        if month in months:
            break
        else:
            print("Invalid input. Please enter a valid month or 'all'.")

    # Valid days
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']

    # Get user input for day
    while True:
        day = input("Enter a day of the week (monday to sunday) or 'all': ").lower()
        if day in days:
            break
        else:
            print("Invalid input. Please enter a valid day or 'all'.")

    return city, month, day

    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """


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
    
# Load the CSV file for the selected city
    df = pd.read_csv(CITY_DATA[city])

    # Convert 'Start Time' to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new columns for month and day of week
    df['month'] = df['Start Time'].dt.month_name().str.lower()
    df['day_of_week'] = df['Start Time'].dt.day_name().str.lower()

    # Filter by month if needed
    if month != 'all':
        df = df[df['month'] == month]

    # Filter by day if needed
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print(f"Most common month: {common_month.capitalize()}")
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common month: {common_month.capitalize()}")
    # TO DO: display the most common start hour
    common_day = df['day_of_week'].mode()[0]
    print(f"Most common day of week: {common_day.capitalize()}")
"""Calculates and prints how long the function took to execute.
Prints a separator line for clarity."""

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print(f"Most commonly used start station: {common_start_station}")


    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].mode()[0]
    print(f"Most commonly used end station: {common_end_station}")


    # TO DO: display most frequent combination of start station and end station trip
    df['Trip Combination'] = df['Start Station'] + " to " + df['End Station']

    common_trip = df['Trip Combination'].mode()[0]
    print(f"Most frequent combination of start and end station trip: {common_trip}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = df['Trip Duration'].sum()
    print(f"Total travel time: {total_travel_time} seconds")


    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print(f"Mean travel time: {mean_travel_time:.2f} seconds")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    print("Counts of user types:")
    print(df['User Type'].value_counts())
    print()


    # TO DO: Display counts of gender

    if 'Gender' in df.columns:
        print("Counts of gender:")
        print(df['Gender'].value_counts())
        print()
    else:
        print("Gender data not available.\n")


    # TO DO: Display earliest, most recent, and most common year of birth

    if 'Birth Year' in df.columns:
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"Earliest year of birth: {earliest_year}")
        print(f"Most recent year of birth: {most_recent_year}")
        print(f"Most common year of birth: {most_common_year}")
    else:
        print("Birth year data not available.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    """Displays 5 rows of data at a time upon user request."""
    start_loc = 0
    while True:
        view_data = input("Do you want to see 5 rows of data? Enter yes or no: ").lower()
        if view_data != 'yes':
            break
        print(df.iloc[start_loc:start_loc + 5])
        start_loc += 5



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()