import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import random
import mysql.connector
from socket import *
import requests
from bs4 import BeautifulSoup
import pickle

HOST = 'localhost'
PORT = 8745

ADDRESS = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)

s.connect(ADDRESS)


root = tk.Tk()
root.title("Royal Traders App")
root.configure(background="#D7A5A5")
style = ttk.Style()

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='1234',
    database="trading"
)
mycursor = mydb.cursor()


def sign():
    global user_entry
    global pass_entry
    global card_entry
    global repass_entry

    sign = tk.Toplevel(root)
    Tops = Frame(sign, width=500, height=900, bd=8, bg="#D7A5A5")
    Tops.grid(row=0, column=0, columnspan=2)
    fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
    fla.grid(row=0, column=0, columnspan=2)

    sign = Image.open("logo-1.png")
    sign = sign.resize((350, 350))
    pic = ImageTk.PhotoImage(sign)
    label = tk.Label(fla, image=pic)
    label.grid(row=0, column=0, padx=0, pady=10, columnspan=2)

    text_label = tk.Label(fla, text="Create A New Account", font=('Italic Outline Arts', 25, 'bold'), bd=0, fg="black",
                          bg="#EF7676")
    text_label.grid(row=1, column=0, columnspan=2, padx=0, pady=10)

    user_label = tk.Label(fla, text="Username:", font=('arial', 10, 'bold'), bd=0, fg="black", bg="#EF7676")
    user_label.grid(row=2, column=0, padx=0, pady=10)
    user_entry = tk.Entry(fla, font=('arial', 10, 'bold'), bd=1, width=20)
    user_entry.grid(row=2, column=1, padx=0, pady=10)

    pass_label = tk.Label(fla, text="Password:", font=('arial', 10, 'bold'), bd=0, fg="black", bg="#EF7676")
    pass_label.grid(row=3, column=0, padx=0, pady=10)
    pass_entry = tk.Entry(fla, font=('arial', 10, 'bold'), bd=1, width=20, show='*')
    pass_entry.grid(row=3, column=1, padx=0, pady=10)

    repass_label = tk.Label(fla, text="Re-enter password:", font=('arial', 10, 'bold'), bd=0, fg="black", bg="#EF7676")
    repass_label.grid(row=4, column=0, padx=0, pady=10)
    repass_entry = tk.Entry(fla, font=('arial', 10, 'bold'), bd=1, width=20, show='*')
    repass_entry.grid(row=4, column=1, padx=0, pady=10)

    card_label = tk.Label(fla, text="Card Number:", font=('arial', 10, 'bold'), bd=0, fg="black", bg="#EF7676")
    card_label.grid(row=5, column=0, padx=0, pady=10)
    card_entry = tk.Entry(fla, font=('arial', 10, 'bold'), bd=1, width=20)
    card_entry.grid(row=5, column=1, padx=0, pady=10)
    style.configure("my.TButton", padding=6, background="#FF8E9B", foreground="black", font=("Arial", 15),
                    borderwidth=0, bordercolor="#FF8E9B")
    sign = ttk.Button(fla, text="Submit", style="my.TButton", command=home_sign)
    sign.grid(row=6, column=0, pady=20, columnspan=2)

    '''pass1=str(pass_entry.get())
    pass2=str(repass_entry.get())
    if pass1 != pass2:
           error=tkinter.messagebox.showinfo("Error","Passwords are not matching!!")'''

    sign.mainloop()


def login():
    global username_entry
    global password_entry
    sign = tk.Toplevel(root)
    Tops = Frame(sign, width=500, height=900, bd=8, bg="#D7A5A5")
    Tops.grid(row=0, column=0, columnspan=2)
    fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
    fla.grid(row=0, column=0, columnspan=2)
    login = Image.open("logo-1.png")
    login = login.resize((350, 350))
    pic = ImageTk.PhotoImage(login)
    label = tk.Label(fla, image=pic)
    label.grid(row=0, column=0, padx=0, pady=25, columnspan=2)

    text_label = tk.Label(fla, text="Login", font=('arial', 30, 'bold'), bd=0, fg="black", bg="#EF7676")
    text_label.grid(row=1, column=0, columnspan=2, padx=0, pady=20)

    username_label = tk.Label(fla, text="Username:", font=('arial', 15, 'bold'), bd=0, fg="black", bg="#EF7676")
    username_label.grid(row=2, column=0, padx=0, pady=10)
    username_entry = tk.Entry(fla, font=('arial', 15, 'bold'), bd=1, width=20)
    username_entry.grid(row=2, column=1, padx=0, pady=10)

    password_label = tk.Label(fla, text="Password:", font=('arial', 15, 'bold'), bd=0, fg="black", bg="#EF7676")
    password_label.grid(row=3, column=0, padx=0, pady=10)
    password_entry = tk.Entry(fla, font=('arial', 15, 'bold'), bd=1, width=20, show='*')
    password_entry.grid(row=3, column=1, padx=0, pady=10)

    style.configure("my.TButton", padding=6, background="#FF8E9B", foreground="black", font=("Arial", 25),
                    borderwidth=0, bordercolor="#FF8E9B")
    login = ttk.Button(fla, text="Submit", style="my.TButton", command=home_log)
    login.grid(row=6, column=0, pady=25, columnspan=2)
    login.mainloop()


def home_sign():
    global user
    user = str(user_entry.get())
    password = str(pass_entry.get())
    card = int(card_entry.get())
    userid = 'A' + str(random.randint(1000, 9999))
    re = str(repass_entry.get())

    if password != re:
        error_msg = tkinter.messagebox.showinfo("Error", "Passwords are not matching!!")

    else:
        sql = f"insert into login values ( '{userid}','{user}','{password}',{card});"
        mycursor.execute(sql)
        mydb.commit()

        home = tk.Toplevel(root)
        Tops = Frame(home, width=500, height=900, bd=8, bg="#D7A5A5")
        Tops.grid(row=0, column=0, columnspan=2)
        fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
        fla.grid(row=0, column=0, columnspan=2)
        login = Image.open("logo-1.png")
        login = login.resize((350, 350))
        pic = ImageTk.PhotoImage(login)
        label = tk.Label(fla, image=pic)
        label.grid(row=0, column=0, padx=0, pady=25, columnspan=2)

        style.configure("my.TButton", padding=6, background="#FF8E9B", foreground="black", font=("Arial", 25),
                        borderwidth=0, bordercolor="#FF8E9B")
        int_plan = ttk.Button(fla, text="Investment Plans", style="my.TButton", command=plans)
        int_plan.grid(row=1, column=0, pady=25, columnspan=2)

        prof = ttk.Button(fla, text="View Profile", style="my.TButton",command=profile)
        prof.grid(row=2, column=0, pady=25, columnspan=2)

        buy = ttk.Button(fla, text="Buy/Sell", style="my.TButton", command=trade)
        buy.grid(row=3, column=0, pady=25, columnspan=2)
        home.mainloop()

def homepage():
        home = tk.Toplevel(root)
        Tops = Frame(home, width=500, height=900, bd=8, bg="#D7A5A5")
        Tops.grid(row=0, column=0, columnspan=2)
        fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
        fla.grid(row=0, column=0, columnspan=2)
        login = Image.open("logo-1.png")
        login = login.resize((350, 350))
        pic = ImageTk.PhotoImage(login)
        label = tk.Label(fla, image=pic)
        label.grid(row=0, column=0, padx=0, pady=25, columnspan=2)
        style.configure("my.TButton", padding=6, background="#FF8E9B", foreground="black", font=("Arial", 25),borderwidth=0, bordercolor="#FF8E9B")
        int_plan = ttk.Button(fla, text="Investment Plans", style="my.TButton", command=plans)
        int_plan.grid(row=1, column=0, pady=25, columnspan=2)

        prof = ttk.Button(fla, text="View Profile", style="my.TButton",command=profile)
        prof.grid(row=2, column=0, pady=25, columnspan=2)

        buy = ttk.Button(fla, text="Buy/Sell", style="my.TButton", command=trade)
        buy.grid(row=3, column=0, pady=25, columnspan=2)
        home.mainloop()
def home_log():
    global user
    user = str(username_entry.get())
    password = str(password_entry.get())

    sql = f"select username,password from login where username='{user}' or password='{password}';"
    mycursor.execute(sql)
    d = mycursor.fetchall()

    for i in d:
        if i[0] != user or i[1] != password:
            error = tkinter.messagebox.showinfo("Error", "Incorrect details")

        else:
            home = tk.Toplevel(root)
            Tops = Frame(home, width=500, height=900, bd=8, bg="#D7A5A5")
            Tops.grid(row=0, column=0, columnspan=2)
            fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
            fla.grid(row=0, column=0, columnspan=2)
            login = Image.open("logo-1.png")
            login = login.resize((350, 350))
            pic = ImageTk.PhotoImage(login)
            label = tk.Label(fla, image=pic)
            label.grid(row=0, column=0, padx=0, pady=25, columnspan=2)
            style.configure("my.TButton", padding=6, background="#FF8E9B", foreground="black", font=("Arial", 25),
                            borderwidth=0, bordercolor="#FF8E9B")
            int_plan = ttk.Button(fla, text="Investment Plans", style="my.TButton", command=plans)
            int_plan.grid(row=1, column=0, pady=25, columnspan=2)

            prof = ttk.Button(fla, text="View Profile", style="my.TButton",command=profile)
            prof.grid(row=2, column=0, pady=25, columnspan=2)

            buy = ttk.Button(fla, text="Buy/Sell", style="my.TButton", command=trade)
            buy.grid(row=3, column=0, pady=25, columnspan=2)
            home.mainloop()


def get_prices():
    url = "https://coinranking.com/"
    response = requests.get(url)
    soup1 = BeautifulSoup(response.content, 'html.parser')

    g_url = "https://finance.yahoo.com/quote/GC%3DF?p=GC%3DF"
    response = requests.get(g_url)
    soup2 = BeautifulSoup(response.content, 'html.parser')

    s_url = "https://finance.yahoo.com/quote/SI%3DF?p=SI%3DF"
    response = requests.get(s_url)
    soup3 = BeautifulSoup(response.content, 'html.parser')

    data = [item.text.split() for item in soup1.find_all('div', class_='valuta valuta--light')]
    Bitcoin = data[0][1]
    Bitcoin=Bitcoin.replace(",", "")
    Bitcoin=float(Bitcoin)
    Ethereum = data[2][1]
    Ethereum = Ethereum.replace(",", "")
    Ethereum = float(Ethereum)
    BNB = data[6][1]
    BNB = BNB.replace(",", "")
    BNB = float(BNB)
    Polygon = data[16][1]
    Polygon = Polygon.replace(",", "")
    Polygon = float(Polygon)
    Tether = data[4][1]
    Tether = Tether.replace(",", "")
    Tether = float(Tether)
    g = [item.text.split() for item in soup2.find_all('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)')]
    Gold = g[0][0]
    Gold = Gold.replace(",", "")
    Gold = float(Gold)
    s = [item.text.split() for item in soup3.find_all('fin-streamer', class_='Fw(b) Fz(36px) Mb(-4px) D(ib)')]
    Silver = s[0][0]
    Silver = Silver.replace(",", "")
    Silver = float(Silver)
    return {'Bitcoin': Bitcoin, 'Ethereum': Ethereum, 'BNB': BNB, 'Polygon': Polygon, 'Tether': Tether, 'Gold': Gold, 'Silver': Silver}
    
def plans():
    home = tk.Toplevel(root)
    Tops = Frame(home, width=500, height=900, bd=8, bg="#D7A5A5")
    Tops.grid(row=0, column=0, columnspan=2)
    fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
    fla.grid(row=0, column=0, columnspan=2)

    a = Frame(fla, width=350, height=100, bd=8, bg="#C03E3E")
    a.grid(row=0, column=0, columnspan=2, pady=20)
    text_label = tk.Label(a, text=f"  Investment Plans  ", font=('Italic Outline Arts', 20, 'bold'), bd=0, fg="black",
                          bg="#C03E3E")
    text_label.grid(row=0, column=0, columnspan=2, padx=0, pady=10)

    b = Frame(fla, width=350, height=50, bd=8, bg="#F14458")
    b.grid(row=1, column=0, columnspan=2, pady=3)
    c = Frame(fla, width=350, height=50, bd=8, bg="#F14458")
    c.grid(row=2, column=0, columnspan=2, pady=3)
    d = Frame(fla, width=350, height=50, bd=8, bg="#F14458")
    d.grid(row=3, column=0, columnspan=2, pady=3)
    e = Frame(fla, width=350, height=50, bd=8, bg="#F14458")
    e.grid(row=4, column=0, columnspan=2, pady=3)
    f = Frame(fla, width=350, height=50, bd=8, bg="#F14458")
    f.grid(row=5, column=0, columnspan=2, pady=3)
    g = Frame(fla, width=350, height=50, bd=8, bg="#F14458")
    g.grid(row=6, column=0, columnspan=2, pady=3)
    h = Frame(fla, width=350, height=50, bd=8, bg="#F14458")
    h.grid(row=7, column=0, columnspan=2, pady=3)
    get_prices()
    crypto = get_prices()

    text_label = tk.Label(b, text=f"            Bitcoin: ({crypto['Bitcoin']})             ",
                          font=('Italic Outline Arts', 15, 'bold'), bd=0, fg="black", bg="#F14458")
    text_label.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
    text_label = tk.Label(c, text=f"           Ethereum: ({crypto['Ethereum']})            ",
                          font=('Italic Outline Arts', 15, 'bold'), bd=0, fg="black", bg="#F14458")
    text_label.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
    text_label = tk.Label(d, text=f"                 BNB: ({crypto['BNB']})                 ",
                          font=('Italic Outline Arts', 15, 'bold'), bd=0, fg="black", bg="#F14458")
    text_label.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
    text_label = tk.Label(e, text=f"               Polygon: ({crypto['Polygon']})               ",
                          font=('Italic Outline Arts', 15, 'bold'), bd=0, fg="black", bg="#F14458")
    text_label.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
    text_label = tk.Label(f, text=f"            Tether USD: ({crypto['Tether']})             ",
                          font=('Italic Outline Arts', 15, 'bold'), bd=0, fg="black", bg="#F14458")
    text_label.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
    text_label = tk.Label(g, text=f"            GOLD: ({crypto['Gold']})                 ",
                          font=('Italic Outline Arts', 15, 'bold'), bd=0, fg="black", bg="#F14458")
    text_label.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
    text_label = tk.Label(h, text=f"              SILVER: ({crypto['Silver']})                  ",
                          font=('Italic Outline Arts', 15, 'bold'), bd=0, fg="black", bg="#F14458")
    text_label.grid(row=0, column=0, columnspan=2, padx=0, pady=10)
    style.configure("my.TButton", padding=6, background="#FF8E9B", foreground="black", font=("Italic Outline Arts", 25),
                    borderwidth=0, bordercolor="#FF8E9B")
    invest = ttk.Button(fla, text="Invest Now", style="my.TButton", command=trade)
    invest.grid(row=8, column=0, pady=20, columnspan=2)

    home.mainloop()


def trade():
    global plan_entry
    home = tk.Toplevel(root)
    Tops = Frame(home, width=500, height=900, bd=8, bg="#D7A5A5")
    Tops.grid(row=0, column=0, columnspan=2)
    fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
    fla.grid(row=0, column=0, columnspan=2)

    def message():
        global val
        val = float(amo_entry.get())
        label = tk.Label(fla,text="Thank You for Information you have entered \n Click on proceed to \n continue with the transaction",font=('arial', 12, 'bold'), bd=0, fg="black", bg="#EF7676")
        label.grid(row=7, column=0, padx=0, pady=10)
        proceed = ttk.Button(fla, text="Proceed", style="my.TButton", command=invest)
        proceed.grid(row=8, column=0, pady=20, columnspan=2)

    def amount():
        global plan
        global amo_entry
        plan = str(plan_entry.get())
        amo_label = tk.Label(fla, text="Enter the Amount you want to invest", font=('arial', 10), bd=0, fg="black",bg="#EF7676")
        amo_label.grid(row=4, column=0, padx=0, pady=10)
        amo_entry = tk.Entry(fla, font=('arial', 20, 'bold'), bd=1, width=20)
        amo_entry.grid(row=5, column=0, padx=0, pady=10)
        submit_amo = ttk.Button(fla, text="Submit", style="my.TButton", command=message)
        submit_amo.grid(row=6, column=0, pady=20, columnspan=2)

    plan_label = tk.Label(fla, text="Enter the kind of investment you want to do", font=('arial', 10), bd=0, fg="black",
                          bg="#EF7676")
    plan_label.grid(row=0, column=0, padx=0, pady=10)
    plan_entry = tk.Entry(fla, font=('arial', 20, 'bold'), bd=1, width=20)
    plan_entry.grid(row=1, column=0, padx=0, pady=10)
    submit = ttk.Button(fla, text="Submit", style="my.TButton", command=amount)
    submit.grid(row=3, column=0, pady=20, columnspan=2)
    # amo=amo_entry.get()


def success():
    home = tk.Toplevel(root)
    Tops = Frame(home, width=500, height=900, bd=8, bg="#D7A5A5")
    Tops.grid(row=0, column=0, columnspan=2)
    fla = Frame(Tops, width=350, height=700, bd=8, bg="#D7A5A5")
    fla.grid(row=0, column=0, columnspan=2)
    image = Image.open("green.png")
    image = image.resize((350, 500))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(fla, image=photo)
    label.grid(row=0, column=0, padx=0, pady=10)
    con = tk.Button(fla, text="continue", font=('arial', 13, 'bold'), bd=0, width=10, padx=10, pady=10, bg="#D7A5A5",
                    fg="red", command=transaction)
    con.grid(row=1, column=0, padx=1, pady=10)
    home.mainloop()


def fail():
    home = tk.Toplevel(root)
    Tops = Frame(home, width=500, height=900, bd=8, bg="#D7A5A5")
    Tops.grid(row=0, column=0, columnspan=2)
    fla = Frame(Tops, width=350, height=700, bd=8, bg="#D7A5A5")
    fla.grid(row=0, column=0, columnspan=2)
    image = Image.open("red.png")
    image = image.resize((350, 500))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(fla, image=photo)
    label.grid(row=0, column=0, padx=0, pady=20)
    con = tk.Button(fla, text="continue", font=('arial', 13, 'bold'), bd=0, width=10, padx=10, pady=10, bg="#D7A5A5",
                    fg="red", command=transaction)
    con.grid(row=1, column=0, padx=1, pady=10)
    home.mainloop()


def invest():
    if "bitcoin" in plan.lower():
        # client.send("How much money are you transferring?".encode())
        crypto_prices = get_prices()
        if crypto_prices['Bitcoin'] <= val:
            success()
        else:
            fail()
    elif "ethereum" in plan.lower():
        # client.send("How much money are you transferring?".encode())

        crypto_prices = get_prices()
        if crypto_prices['Ethereum']<= val:
            success()
        else:
            fail()
    elif "bnb" in plan.lower():
        # client.send("How much money are you transferring?".encode())

        crypto_prices = get_prices()
        if crypto_prices['BNB'] <= val:
            success()
        else:
            fail()
    elif "polygon" in plan.lower():
        # client.send("How much money are you transferring?".encode())

        crypto_prices = get_prices()
        if crypto_prices['Polygon'] <= val:
            success()
        else:
            fail()
    elif "tether usd" in plan.lower():
        # client.send("How much money are you transferring?".encode())

        crypto_prices = get_prices()
        if crypto_prices['Tether']<= val:
            success()
        else:
            fail()
    elif "gold" in plan.lower():
        # client.send("How much money are you transferring?".encode())

        crypto_prices = get_prices()
        if crypto_prices['Gold']<= val:
            success()
        else:
            fail()
    elif "silver" in plan.lower():
        # client.send("How much money are you transferring?".encode())

        crypto_prices = get_prices()
        if crypto_prices['Silver']<= val:
            success()
        else:
            fail()


def transaction():
    
    l = (user, val, plan)
    bin_val=pickle.dumps(l)
    s.send(bin_val)
    home = tk.Toplevel(root)
    Tops = Frame(home, width=500, height=900, bd=8, bg="white")
    Tops.grid(row=0, column=0, columnspan=2)
    fla = Frame(Tops, width=350, height=700, bd=8, bg="white")
    fla.grid(row=0, column=0, columnspan=2)
    image = Image.open("TY.png")
    image = image.resize((350, 700))
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(fla, image=photo)
    label.grid(row=0, column=0, padx=0, pady=20)
    home.mainloop()
    
def profile():
    global userid
    new = tk.Toplevel(root)
    Tops = Frame(new, width=500, height=900, bd=8, bg="#D7A5A5")
    Tops.grid(row=0, column=0, columnspan=2)
    fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
    fla.grid(row=0, column=0, columnspan=2)
    '''bin_data=s.recv(1024)
    data= pickle.loads(bin_data)
    userid=data[0][0]'''
    sql = f"SELECT userid FROM login WHERE username = '{user}'"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result:
        userid = result[0]
    sql=f"select * from transaction where userid='{userid}';"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    userid=data[0][0]
    label = tk.Label(fla,text=f"{user} \t {userid}",font=('arial', 30, 'bold'), bd=0, fg="black", bg="#C03E3E")
    label.grid(row=1, column=0, padx=0, pady=10)
    x=4
    y=5
    for i in range(len(data)):
        if i==0:
            label = tk.Label(fla,text=f"Transaction {i+1}",font=('arial', 15, 'bold'), bd=0, fg="black", bg="red")
            label.grid(row=2, column=0, padx=0, pady=10)
            label = tk.Label(fla,text=f"{data[i][1]} \n {data[i][2]} \n {data[i][3]}",font=('arial', 12, 'bold'), bd=0, fg="black", bg="#EF7676")
            label.grid(row=3, column=0, padx=0, pady=10)
        else:
            label = tk.Label(fla,text=f"Transaction {i+1}",font=('arial', 12, 'bold'), bd=0, fg="black", bg="red")
            label.grid(row=x+i, column=0, padx=0, pady=10)
            label = tk.Label(fla,text=f"{data[i][1]} \n {data[i][2]} \n {data[i][3]}",font=('arial', 12, 'bold'), bd=0, fg="black", bg="#EF7676")
            label.grid(row=y+i, column=0, padx=0, pady=10)
        x+=1
        y+=1
    x=len(data)
    h = tk.Button(fla, text="Home", font=('arial', 13, 'bold'), bd=0, width=10, padx=10, pady=10, bg="#D7A5A5", fg="red", command=homepage)
    h.grid(row=15,column=0,padx=0,pady=10)
    new.mainloop()


Tops = Frame(root, width=500, height=900, bd=8, bg="#D7A5A5")
Tops.grid(row=0, column=0, columnspan=2)
fla = Frame(Tops, width=350, height=700, bd=8, bg="#EF7676")
fla.grid(row=0, column=0, columnspan=2)
image = Image.open("logo-1.png")
image = image.resize((350, 503))
photo = ImageTk.PhotoImage(image)
label = tk.Label(fla, image=photo)
label.grid(row=0, column=0, padx=0, pady=20)
style.configure("my.TButton", padding=6, background="#FF8E9B", foreground="black", font=("Arial", 20), borderwidth=0,bordercolor="#FF8E9B")
login = ttk.Button(fla, text="login", style="my.TButton", command=login)
login.grid(row=1, column=0, pady=5)
sign = ttk.Button(fla, text="sign-up", style="my.TButton", command=sign)
sign.grid(row=2, column=0, pady=5)

root.mainloop()
s.close()
