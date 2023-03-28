import sqlite3


def sql_connection():
    con = sqlite3.connect("vanilla.db")
    return con


def sql_table(con):
    cursorObj = con.cursor()
    cursorObj.execute("CREATE TABLE IF NOT EXISTS data_buttons (id integer PRIMARY KEY,\
    data_type text, locator text, locator_type text)")
    con.commit()


con = sql_connection()
sql_table(con)

my_buttons = [(1, "Login", "btnActive", "ID"),
              (2, "Home", "//a[@title='Home']", "XPATH"),
              (3, "Sales", "groupNode_sales", "ID"),
              (4, "Service Request","#itemNode_sales_service_requests", "CSS_SELECTOR"),
              (5, "Create Service Request", "//button[@title='Create Service Request']", "XPATH"),
              (6, "Save and Close", "//button[@title='Save and Close']", "XPATH"),
              (7, "list arrow", "(//a[@class='x1kr'])[1]", "XPATH"),
              (8, "Create Appointment", "//a[.='Create Appointment']", "XPATH"),
              (9, "Save and close","//button[.='Save and Close']", "XPATH")]


def sql_insert(con, entities):
    cursorObj = con.cursor()
    cursorObj.executemany("INSERT INTO data_buttons (id, data_type, locator, locator_type) VALUES(?, ?, ?, ?)", entities)
    con.commit()

sql_insert(con, my_buttons)

con = sqlite3.connect("vanilla.db")
cursorObj = con.cursor()
cursorObj.execute("SELECT * FROM data_buttons")
buttons = cursorObj.fetchall()
for button in buttons:
    print(buttons)
