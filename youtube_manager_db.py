import sqlite3
conn=sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )    
               
''')

def list_videos():
    cursor.execute('''
    SELECT * FROM videos           
''')
    for row in cursor.fetchall():
        print(row)
    

def add_video(name, time):
    cursor.execute("INSERT INTO videos(name, time) VALUES(?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id=?", (new_name, time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id =?", (video_id,))
    conn.commit()

def main():
    while True:
        print(50*"-")
        print("\n Youtube Manager with Database")
        print("\n1. List Videos")
        print("\n2. Add Videos")
        print("\n3. Update Videos")
        print("\n4. Delete Videos")
        print("\n5. Exit app")
        choice = input("\nEnter Your Choice: ")

        if choice =='1':
            list_videos()
        
        elif choice =='2':
            name = input("Enter video Name: ")
            time = input("Enter video Duration: ")
            add_video(name, time)

        elif choice =='3':
            video_id=input("\nEnter Video ID to update")
            name = input("Enter video Name: ")
            time = input("Enter video Duration: ")
            update_video(video_id, name, time)

        elif choice =='4':
            video_id=input("\nEnter Video ID you want to Delete")
            delete_video(video_id)

        elif choice =='5':
            break

        else:
            print("Invalid Choice")
    
    conn.close()

if __name__ == "__main__":
    main()

#by Partha Mitra
# This Python Code will automatically create a sqlite3 database named "youtube_videos.db"
# And Perform The CRUD(Create, Update, Delete) operation
# Learned From Hitesh Choudhary
