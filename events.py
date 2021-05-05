import pandas as pd
import datetime

# Features that are needed to be implemented are

# * the ability to enter a new event(done)
# * the ability to edit an event(done)
# * the ability to delete an event(done)
# * the ability to search for events by a person's name(done)
# * the ability to search for events by event type(done)
# * show upcoming events - e.g., events in the next 7 days(done)

# Extra features that needs to be implemented are

# * feature that notifies you of events two or more days in advance
# * add a feature that suggests what you can buy or send them for that event, e.g., flowers for an aunt's anniversary, etc

df = pd.read_csv("events_log.csv", header=None, index_col=None)
df.columns = ["name", "time", "event_type"]


def event():
    """Takes input for the following fields such as name , time and type of event"""

    name = input("Please Enter the name : ")
    time = input("Please Enter the time in the format of %y-%m-%d : ")
    event_type = input("Please Enter the event type : ")

    return name, time, event_type


def edit_event_details():
    """Takes input for the following fields for editing an event such as name , time and type of event"""

    edited_name = str(input("Please Enter the name that needs to be edited : "))
    edited_time = input(
        "Please Enter the time in the format of %y-%m-%d that needs to be edited : "
    )
    edited_event_type = input("Please Enter the event type that needs to be edited : ")

    return edited_name, edited_time, edited_event_type


def enter_new_events(df):

    """
    Add new events to the databse

    :df     : dataframe
    :return : dataframe

    """

    # df=pd.read_csv('events_log.csv',header=None)

    new_person_name, new_date, new_event = event()

    # df['name']=new_person_name
    # df['time']=new_date
    # df['event_type']=new_event

    new_event_data = {
        "name": f"{new_person_name}",
        "time": f"{new_date}",
        "event_type": f"{new_event}",
    }
    df = df.append(new_event_data, ignore_index=True)

    df.to_csv("events_log.csv", header=None, index=None)
    print(
        f"Event created for {new_person_name} at {new_date} on the occassion of {new_event}"
    )

    return df


def edit_event(df):
    """
    Edit new events to the databse

    :df     : dataframe
    :return : dataframe

    """

    name, date, event_type = edit_event_details()

    new_name, new_date, new_event_type = event()
    print(new_name)
    print(df.head())

    # df.append(df['name'].replace(['new_name'],'name'))

    edit_data = {"name": f"{name}", "time": f"{date}", "event_type": f"{event_type}"}
    df = df.append(edit_data, ignore_index=True)
    print(df.head())

    df_to_be_removed = df[df["name"] == f"{new_name}"]
    print(df_to_be_removed)

    df = df.drop(df_to_be_removed.index, axis=0)
    print(df)

    df.to_csv("events_log.csv", header=None, index=None)

    return df


# print(edit_event(df))


def delete_event(df):
    """
    Delete events from the databse

    :df     : dataframe
    :return : dataframe

    """

    name_to_be_deleted, year_to_be_deleted, event_to_be_deleted = event()

    print(df)

    df_to_be_deleted = df[df["name"] == f"{name_to_be_deleted}"]
    print(df_to_be_deleted)

    df = df.drop(df_to_be_deleted.index, axis=0)
    print(df)

    return df


def search_event_using_person_name(df):

    """
    Search event using person name

    :df     : dataframe
    :return : dataframe

    """

    person_name = input("Please enter the person name to be searched : ")

    event_name = df[df["name"] == f"{person_name}"]

    print(event_name["event_type"])

    return df


def search_event_using_event_name(df):

    """
    Search event using event name

    :df     : dataframe
    :return : dataframe

    """

    event_name = input("Please enter the event name to be searched : ")

    event_name = df[df["event_type"] == f"{event_name}"]

    print(event_name["name"])

    return df


def upcoming_events_in_the_next_7_days(df):

    """
    Upcoming events in the next 7 days

    :df     : dataframe
    :return : dataframe

    """

    fmt = "%Y-%m-%d"

    current_date = pd.datetime.now().date()

    for i in df["time"]:
        d1 = datetime.datetime.strptime(str(i), fmt)
        d2 = datetime.datetime.strptime(str(current_date), fmt)
        print(d1)
        print(d2)

        if str((d2 - d1).days) >= "7":
            print(f"Event is approcahing at {d2}")
        else:
            pass
    return df


if __name__ == "__main__":
    choosen_number = int(input("Please enter a number from 1 to 6 : "))

    # 1 : enter new events
    # 2 : edit events
    # 3 : delete events
    # 4 : search event using persons name
    # 5 : search event using using name
    # 6 : upcoming events in the next 7 days

    if choosen_number == 1:
        print(enter_new_events(df))
    elif choosen_number == 2:
        print(edit_event(df))
    elif choosen_number == 3:
        print(delete_event(df))
    elif choosen_number == 4:
        print(search_event_using_person_name(df))
    elif choosen_number == 5:
        print(search_event_using_event_name(df))
    elif choosen_number == 6:
        print(upcoming_events_in_the_next_7_days(df))
