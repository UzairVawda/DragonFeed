import sqlite3
from sqlite3 import Error

def create_connection(): 
    try: 
        db_connection = sqlite3.connect("db.sqlite3")
        return db_connection
    except Error as e:
        print("ATTENTION: AN ERROR HAS OCCURRED\n\t",e)

def get_search_type(): 
    search_type = input("Search Type:").casefold().upper()
    return search_type

def get_keyword(): 
    keyword = input("Keyword:").casefold()
    return keyword

def get_events(db_connection,search_type,keyword): 
    event_names = []
    if search_type == "":
        search_type = "Title"

    cursor = db_connection.cursor()

    if keyword == "":
        try:
            cursor.execute("SELECT * FROM "+search_type)
        except Error as e:
            print("ATTENTION: AN ERROR HAS OCCURRED\n\t",e)
    else:
        try:
            cursor.execute("SELECT * FROM  WHERE "+search_type+" MATCH word = ?",[keyword])
        except Error as e:
            print("ATTENTION: AN ERROR HAS OCCURRED\n\t",e)
    event_names = cursor.fetchall()
    return event_names 

def mr_clean(text): 
    return ''.join( chr for chr in text if chr.isalnum() )

''' Uzair, I have commented out this section while I resolve the explicit issue.
def magic_words(text): #This function checks the text for "special" words, such as "help","manual","how to,",etc. and only adds events to the main feed which match it.
    if text.casefold() == ("manual" or "help" or "info" or "information" or "data" or "about"):
        return "manual"
    else:
        return text
'''

def main():
    event_names =[]
    db_connection = create_connection()
    search_type = mr_clean(get_search_type())
    keyword = mr_clean(get_keyword())
    with db_connection:
        event_names = get_events(db_connection,search_type,keyword)
 
if __name__ == '__main__':
    main()