from tkinter import *
import pandas
from tkinter import ttk
from tkinter import messagebox
import csv


NAVY_BLUE = "#364F6B"
WHITE = "#FFFFFF"
BOOK_LIMIT = 0
checkout_ids = []
library_members_list = []
reservation_id = []
title_id = []
days = 10
reserve_title_id = []



class ApplicationWindow():
    def __init__(self):
        try:
            self.library_members_data = pandas.read_csv("library_members.csv")
        except FileNotFoundError:
            self.library_members_data = pandas.read_csv("library_members - Sheet1 (1).csv")
            self.library_members_list = self.library_members_data["NAMES"].to_list()
        else:
            self.library_members_list = self.library_members_data["NAMES"].to_list()

        try:
            self.books_data = pandas.read_csv("List_of_books")
        except FileNotFoundError:
            self.books_data = pandas.read_csv("List of Books - Sheet1 (3).csv")


        self.login_window = Tk()
        self.login_window.title("CASA DE COMMUNIDAD")
        self.login_window.config(padx=20, pady=20, highlightthickness=0, bg=NAVY_BLUE)
        self.main_logo = Canvas(width=743, height=336, bg=NAVY_BLUE, highlightthickness=0)
        self.logo = PhotoImage(file="image/icon-removebg-preview.png")
        self.main_logo.create_image(371, 168, image=self.logo)
        self.main_logo.grid(column=0, row=0, rowspan=2)

        self.bookshelf_logo = Canvas(width=756, height=310, bg=NAVY_BLUE, highlightthickness=0)
        self.bookshelf_logo_icon = PhotoImage(file="image/bookslogo.png")
        self.bookshelf_logo.create_image(378, 155, image=self.bookshelf_logo_icon)
        self.bookshelf_logo.grid(column=0, row=4, rowspan=4)

        self.account_logo = Canvas(width=109, height=96, bg=NAVY_BLUE, highlightthickness=0, )
        self.account_logo_icon = PhotoImage(file="image/account logo.png")
        self.account_logo.create_image(54.5, 48, image=self.account_logo_icon)
        self.account_logo.grid(column=3, row=1, columnspan=2, rowspan=2)

        self.enter_your_name_here = Label(text="Enter your name here:", fg=WHITE, bg=NAVY_BLUE, font=("Roboto Slab", 9))
        self.enter_your_name_here.grid(column=3, row=2, rowspan=2)

        self.name_login = StringVar()
        self.enter_name = Entry(width=30, textvariable=self.name_login)
        self.enter_name.grid(column=3, row=2, rowspan=3)

        self.sign_in = Button(text="SIGN IN", fg=WHITE, bg="#3FC1C9", width=31, height=2, activebackground="#3FC1C9",
                         command=self.login)
        self.sign_in.grid(column=3, row=4, rowspan=2)

        self.register_now = Button(text="REGISTER NOW", fg=WHITE, bg="#FC5185", width=31, height=2,
                              activebackground="#FC5185",command=self.register
                        )
        self.register_now.grid(column=3, row=5, rowspan=1)


        self.login_window.mainloop()

    def login(self):
        self.name_login.set(self.name_login.get().upper())
        if self.enter_name.get() in self.library_members_list:
            self.login_window.destroy()
            self.borrow_or_return_page = Tk()
            self.borrow_or_return_page.title("CASA DE COMMUNIDAD")
            self.borrow_or_return_page.config(padx=20, pady=20, highlightthickness=0, bg=NAVY_BLUE)
            logo_2 = Canvas(width=756, height=330, bg=NAVY_BLUE, highlightthicknes=0)
            logo_2_icon = PhotoImage(file="image/logo_2-removebg-preview.png")
            logo_2.create_image(378, 165, image=logo_2_icon)
            logo_2.grid(column=1, row=0)

            borrow_button_logo = PhotoImage(file="image/borrow_logo.png")
            return_button_logo = PhotoImage(file="image/return_logo.png")

            empty = Label(text="---", fg=NAVY_BLUE, bg=NAVY_BLUE)
            empty.grid(column=1, row=1)
            borrow_button = Button(image=borrow_button_logo, command=self.borrow_book)
            borrow_button.grid(column=1, row=2, sticky="w", rowspan=2)
            return_button = Button(image=return_button_logo, command=self.return_book_page)
            return_button.grid(column=1, row=2, sticky="e", rowspan=2)

            self.borrow_or_return_page.mainloop()
        else:
            messagebox.showerror(title="Incorrect Credentials",message="You are not yet a library member, please do register")

    def register(self):
        self.login_window.destroy()
        self.register_page = Tk()
        self.register_page.title("Register Form")
        self.register_page.config(padx=20, pady=20, highlightthickness=0, bg=NAVY_BLUE)

        user_registration = Canvas(width=954, height=144, bg=NAVY_BLUE, highlightthickness=0)
        user_registration_logo = PhotoImage(file="image/user_registration-removebg-preview.png")
        user_registration.create_image(450, 75, image=user_registration_logo)
        user_registration.grid(column=0, row=0)

        please_enter_the_following_informations = Label(text="Please enter the following informations.",
                                                   font=("Roboto", 20,), fg=WHITE, bg=NAVY_BLUE)
        please_enter_the_following_informations.grid(column=0, row=1)

        name_label = Label(text="Name:", font=("Roboto", 10,), fg=WHITE, bg=NAVY_BLUE)
        name_label.grid(column=0, row=2)

        self.name = Entry(width=60)
        self.name.insert(END, string="Please enter your name")
        self.name.grid(column=0, row=3)
        empty = Label(text="---", fg=NAVY_BLUE, bg=NAVY_BLUE)
        empty.grid(column=0, row=4)
        register_button = Button(text="REGISTER", fg=WHITE, bg="#FC5185", width=31, height=2,
                        activebackground="#FC5185", command=self.register_clicked)
        register_button.grid(column=0, row=5)
        self.register_page.mainloop()

    def register_clicked(self):
        please_pay = Label(text="❗Please pay ₱5 at the counter❗", font=("Roboto", 15,), fg=WHITE, bg=NAVY_BLUE)
        please_pay.grid(column=0, row=6)
        awaiting_payment = Label(text="Awaiting payment...", font=("Roboto", 15,), fg=WHITE, bg=NAVY_BLUE)
        awaiting_payment.grid(column=0, row=7)
        confirm_payment = Button(text="Confirm payment", fg=WHITE, bg=NAVY_BLUE, width=31, height=2,
                           activebackground=NAVY_BLUE, command=self.confirmed_payment)
        confirm_payment.grid(column=0, row=8)

    def confirmed_payment(self):
        global library_members_list
        register_user = self.name.get()
        register_user.upper()
        library_members_list.append(register_user)
        latest_members_list = [x.upper() for x in library_members_list]
        new_data = pandas.DataFrame(latest_members_list, columns=["NAMES"])
        new_data.to_csv("library_members.csv", index=False, mode="a")
        try:
            library_members_data = pandas.read_csv("library_members.csv")
        except FileNotFoundError:
            library_members_data = pandas.read_csv("library_members - Sheet1 (1).csv")
            library_members_list = library_members_data["NAMES"].to_list()
        else:
            library_members_list = library_members_data["NAMES"].to_list()
        self.register_page.destroy()
        ApplicationWindow()
        self.register_page.mainloop()

    def borrow_book(self):
        self.borrow_or_return_page.destroy()
        self.main_page = Tk()
        self.main_page.title("Main page")
        self.main_page.config(padx=20, pady=20, highlightthickness=0, bg=WHITE)

        search_book_by = Label(text="Search book by: ", fg=NAVY_BLUE, bg=WHITE,
                               font=("Roboto Slab", 14, "bold"))
        search_book_by.grid(column=0, row=0)
        title = Label(text="Title: ", fg=NAVY_BLUE, bg=WHITE, font=("Roboto Slab", 12))
        title.grid(column=0, row=1, sticky="e")
        author = Label(text="Author: ", fg=NAVY_BLUE, bg=WHITE, font=("Roboto Slab", 12))
        author.grid(column=0, row=2, sticky="e")
        subject_category = Label(text="Subject Category: ", fg=NAVY_BLUE, bg=WHITE, font=("Roboto Slab", 12))
        subject_category.grid(column=0, row=3, sticky="e")
        publication_date = Label(text="Publication Date: ", fg=NAVY_BLUE, bg=WHITE, font=("Roboto Slab", 12))
        publication_date.grid(column=2, row=2, sticky="e")

        self.title_entry = Entry(width=97, relief="groove", bg=WHITE)
        self.title_entry.grid(column=1, row=1, sticky="w", columnspan=3)
        self.author_entry = Entry(width=40, relief="groove", bg=WHITE)
        self.author_entry.grid(column=1, row=2, columnspan=2, sticky="w")
        self.subject_category_entry = Entry(width=40, relief="groove", bg=WHITE)
        self.subject_category_entry.grid(column=1, row=3, sticky="w")
        self.publication_date_entry = Entry(width=24, relief="groove", bg=WHITE)
        self.publication_date_entry.grid(column=3, row=2)
        self.reserve_button = Button(text="RESERVE", fg=WHITE, bg=NAVY_BLUE, width=20, command=self.reserve)
        self.reserve_button.grid(column=5, row=5)
        self.checkout_button = Button(text="CHECKOUT", fg=WHITE, bg="#6DA5A9", width=20, command=self.checkout)
        self.checkout_button.grid(column=0, row=5, sticky="w")
        self.search_button = Button(text="SEARCH", fg=WHITE, bg="pink", width=20, command=self.search)
        self.search_button.grid(column=3, row=3)
        self.add_to_cart = Button(text="ADD TO CART", fg=WHITE, bg="#7E370C", width=20, command=self.add_to_cart_f)
        self.add_to_cart.grid(column=7, row=5, sticky="e")
        self.my_reservations = Button(text="MY RESERVATIONS", fg=WHITE, bg="#97BFB4", width=20, command=self.my_reservations_page)
        self.my_reservations.grid(column=1,row=5,sticky="w")
        self.tree = ttk.Treeview()
        try:
            self.books_data = pandas.read_csv("List_of_books")
        except FileNotFoundError:
            self.books_data = pandas.read_csv("List of Books - Sheet1 (3).csv")
        self.books_data.columns = self.books_data.columns.str.replace(' ', '_')
        df_column = self.books_data.columns.values
        self.tree["column"] = list(self.books_data.columns)
        self.tree["show"] = "headings"
        vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview())
        vsb.grid(column=8, row=4, sticky="ns")
        self.tree.configure(yscrollcommand=vsb.set)

        for column in self.tree['column']:
            self.tree.column(column,anchor=CENTER)
            self.tree.heading(column, text=column)

        df_rows = self.books_data.to_numpy().tolist()
        for row in df_rows:
            self.tree.insert("", "end", values=row)
        self.tree.grid(column=0, row=4, columnspan=8)

    def checkout(self):
        global book_id
        global checkout_ids
        self.main_page.destroy()
        self.checkout_page = Tk()
        self.checkout_page.title("Checkout Page")
        self.checkout_page.config(padx=20, pady=20, bg="white")
        confirm_checkout_button = Button(text="CONFIRM AND CHECKOUT", fg=WHITE, bg=NAVY_BLUE, width=31,
                                         height=2, command=self.thank_you_page)
        confirm_checkout_button.grid(column=7, row=0, sticky="e")
        self.checkout_tree = ttk.Treeview()
        self.build_df = self.books_data.copy()
        df_column = self.books_data.columns.values
        self.checkout_tree["column"] = list(self.books_data.columns)
        self.checkout_tree["show"] = "headings"
        vsb = ttk.Scrollbar(orient="vertical", command=self.checkout_tree.yview())
        vsb.grid(column=8, row=1, sticky="ns")
        self.checkout_tree.configure(yscrollcommand=vsb.set)

        for column in self.checkout_tree['column']:
            self.checkout_tree.column(column,anchor=CENTER)
            self.checkout_tree.heading(column, text=column)
        for x in checkout_ids:
            build_df = self.build_df[self.build_df.IDENTIFICATION_NO == (x)]
            df_rows = build_df.to_numpy().tolist()
            for row in df_rows:
                self.checkout_tree.insert("", "end", values=row)

        self.checkout_tree.grid(column=0,row=1, columnspan=8)

        self.checkout_page.mainloop()

    def thank_you_page(self):
        self.checkout_page.destroy()
        self.thank_you = Tk()
        self.thank_you.title("Thank you page")
        self.thank_you.config(padx=20, pady=20, bg=NAVY_BLUE)
        thank_you_canvas = Canvas(width=504, height=348, highlightthickness=0)
        thank_you_image = PhotoImage(file="thank_you.png")
        thank_you_canvas.create_image(252, 174, image=thank_you_image)
        thank_you_canvas.grid(column=1, row=0)
        return_to_main_page_button = Button(text="RETURN TO LOGIN PAGE", fg=WHITE, bg="#6DA5A9", width=31, height=2,
                                            command=self.return_to_main)
        return_to_main_page_button.grid(column=0,row=1)
        exit_button = Button(text="EXIT", fg=WHITE,bg="red", width=31, height=2, command=self.exit)
        exit_button.grid(column=2,row=1)

        self.thank_you.mainloop()

    def thank_you_page_2(self):
        self.return_page.destroy()
        def thank_you_page2():
            self.thank_you = Tk()
            self.thank_you.title("Thank you page")
            self.thank_you.config(padx=20, pady=20, bg=NAVY_BLUE)
            thank_you_canvas = Canvas(width=504, height=348, highlightthickness=0)
            thank_you_image = PhotoImage(file="thank_you.png")
            thank_you_canvas.create_image(252, 174, image=thank_you_image)
            thank_you_canvas.grid(column=1, row=0)
            return_to_main_page_button = Button(text="RETURN TO LOGIN PAGE", fg=WHITE, bg="#6DA5A9", width=31, height=2,
                                                command=self.return_to_main)
            return_to_main_page_button.grid(column=0, row=1)
            exit_button = Button(text="EXIT", fg=WHITE, bg="red", width=31, height=2, command=self.exit)
            exit_button.grid(column=2, row=1)

            self.thank_you.mainloop()
        thank_you_page2()

    def reserve(self):
        global book_id
        global checkout_ids
        selected = self.tree.item(self.tree.focus())


        if selected['values']:
            book_item = selected['values'][4]
            if book_item < 1:
                book_title = selected['values'][0]
                book_id = selected['values'][3]
                reserve_title_id.append(book_title)
                book_id_val = self.books_data.loc[self.books_data['IDENTIFICATION_NO'] == book_id, 'BOOK_ITEM'].to_numpy().tolist()[0]
                reservation_id.append(book_id)
                self.books_data.loc[self.books_data['IDENTIFICATION_NO'] == book_id, 'BOOK_ITEM'] = book_id_val - 1
                self.search()
                self.books_data.to_csv("List_of_books", index=False)
                try:
                    self.books_data = pandas.read_csv("List_of_books")
                except FileNotFoundError:
                    self.books_data = pandas.read_csv("List of Books - Sheet1 (3).csv")
            else:
                messagebox.showerror(title="Book still available", message="The book is still available, please use the checkout method instead.")

    def search(self):
        self.tree.delete(*self.tree.get_children())
        entries = [
            self.title_entry,
            self.author_entry,
            self.subject_category_entry,
            self.publication_date_entry
        ]
        build_df = self.books_data
        if entries[0].get():
            build_df = build_df[build_df.TITLE.str.contains(entries[0].get())]
        if entries[1].get():
            build_df = build_df[build_df.AUTHOR == (entries[1].get())]
        if entries[2].get():
            build_df = build_df[build_df.SUBJECT_CATEGORY.str.contains(entries[2].get())]
        if entries[3].get():
            build_df = build_df[build_df.PUBLICATION_DATE == (int(entries[3].get()))]

        df_rows = build_df.to_numpy().tolist()
        for row in df_rows:
            self.tree.insert("", "end", values=row)

    def add_to_cart_f(self):
        global BOOK_LIMIT
        global book_id
        global checkout_ids
        global title_id
        selected = self.tree.item(self.tree.focus())
        if selected['values']:
            book_id = selected['values'][3]
            book_title = selected['values'][0]
            book_id_val = \
            self.books_data.loc[self.books_data['IDENTIFICATION_NO'] == book_id, 'BOOK_ITEM'].to_numpy().tolist()[0]
            if book_id_val < 1:
                return 0
            else:
                if BOOK_LIMIT >= 5:
                    messagebox.showerror(title="You already possess 5 books", message="You already exceed the limit per customer")
                else:
                    BOOK_LIMIT += 1
                    checkout_ids.append(book_id)
                    title_id.append(book_title)

                    self.books_data.loc[self.books_data['IDENTIFICATION_NO'] == book_id, 'BOOK_ITEM'] = book_id_val - 1
                    self.search()
                    self.books_data.to_csv("List_of_books", index=False)
                    try:
                        self.books_data = pandas.read_csv("List_of_books")
                    except FileNotFoundError:
                        self.books_data = pandas.read_csv("List of Books - Sheet1 (3).csv")

    def return_book_page(self):
        global days

        self.borrow_or_return_page.destroy()
        self.return_page = Tk()
        self.return_page.title("Return page")
        self.return_page.config(padx=20,pady=20,bg=WHITE)
        list_of_books_to_return = Label(text="List of books to return: ", fg=NAVY_BLUE, bg=WHITE,
                                        font=("Viga", 32, "bold"))
        list_of_books_to_return.grid(column=0,row=1, sticky="w")
        please_text = Label(text="(Please check your library fines before returning the books)",
                            fg=NAVY_BLUE, bg=WHITE, font=("viga", 12,))
        please_text.grid(column=0, row=3, sticky="w")
        check_fines = Button(text="LIBRARY FINES", fg=WHITE, bg=NAVY_BLUE, width=31, height=2,
                             activebackground=NAVY_BLUE, command=self.library_fines)
        check_fines.grid(column=2, row=3, columnspan=2)
        return_books = Button(text="RETURN BOOKS", fg=WHITE, bg="#6DA5A9", width=31, height=2,
                              activebackground="#6DA5A9", command=self.return_book)
        return_books.grid(column=5, row=3, columnspan=2)
        confirm_button = Button(text="CONFIRM & RETURN", fg=WHITE, bg="#6DA5A9", width=31, height=2,
                                activebackground="#6DA5A9", command=self.thank_you_page_2)
        confirm_button.grid(column=7, row=3, columnspan=2)

        time = Label(text=f"{days} days left.", fg=NAVY_BLUE, bg=WHITE,
                     font=("Viga", 32, "bold"))
        time.grid(column=7, row=0, sticky="e")
        return_to_mainpage2 = Button(text="RETURN TO MAIN PAGE", fg=WHITE, bg=NAVY_BLUE, width=40,height=2,command=self.return_to_main2)
        return_to_mainpage2.grid(column=0,row=0, sticky="w")
        def timer_clock():
            global days
            days -= 1
            if days == 0:
                messagebox.showwarning(title="Please Return Book", message="Your borrowed sessions has expired, please "
                                                                           "return the books immediately")
            else:
                time.config(text=f"{days} days left. ")



        self.return_book_tree = ttk.Treeview()
        self.build_df = self.books_data.copy()
        df_column = self.books_data.columns.values
        self.return_book_tree["column"] = list(self.books_data.columns)
        self.return_book_tree["show"] = "headings"
        vsb = ttk.Scrollbar(orient="vertical", command=self.return_book_tree.yview())
        vsb.grid(column=8, row=2, sticky="ns")
        self.return_book_tree.configure(yscrollcommand=vsb.set)
        borrow_dictionary = {
            self.name_login.get(): title_id,

        }
        pandas.DataFrame.from_dict(borrow_dictionary).to_csv("system borrowed books.csv", index=False,mode="a")


        for column in self.return_book_tree['column']:
            self.return_book_tree.column(column,anchor=CENTER)
            self.return_book_tree.heading(column, text=column)

        for x in borrow_dictionary[self.name_login.get()]:
            build_df = self.build_df[self.build_df.TITLE == (x)]
            df_rows = build_df.to_numpy().tolist()
            for row in df_rows:
                self.return_book_tree.insert("", "end", values=row)

        self.return_book_tree.grid(column=0, row=2, columnspan=8)
        self.return_page.after(10000, timer_clock)

        self.return_page.mainloop()

    def exit(self):
        self.thank_you.destroy()

    def return_to_main(self):
        self.thank_you.destroy()
        ApplicationWindow()

    def return_book(self):
        global book_id
        global checkout_ids
        selected = self.return_book_tree.selection()[0]
        book_id_val = \
        self.books_data.loc[self.books_data['IDENTIFICATION_NO'] == book_id, 'BOOK_ITEM'].to_numpy().tolist()[0]
        self.books_data.loc[self.books_data['IDENTIFICATION_NO'] == book_id, 'BOOK_ITEM'] = book_id_val + 1
        self.return_book_tree.delete(selected)
        self.books_data.to_csv("List_of_books", index=False)
        try:
            self.books_data = pandas.read_csv("List_of_books")
        except FileNotFoundError:
            self.books_data = pandas.read_csv("List of Books - Sheet1 (3).csv")

    def my_reservations_page(self):
        global reservation_id
        self.main_page.destroy()
        self.reservation_page = Tk()
        self.reservation_page.title("YOUR RESERVATIONS")
        self.reservation_page.config(padx=20,pady=20,bg="white")
        your_reservations = Label(text="Your Reservations: ", fg=NAVY_BLUE, bg=WHITE,
                                        font=("Viga", 32, "bold"))
        your_reservations.grid(column=0,row=1, sticky="w")
        return_to_main_page = Button(text="RETURN TO MAIN PAGE", fg=WHITE, bg=NAVY_BLUE, width=40,height=2,command=self.return_to_main_page)
        return_to_main_page.grid(column=0,row=0, sticky="w")

        self.reservation_tree = ttk.Treeview()
        self.build_df = self.books_data.copy()
        self.reservation_tree["column"] = list(self.books_data.columns)
        self.reservation_tree["show"] = "headings"
        vsb = ttk.Scrollbar(orient="vertical", command=self.reservation_tree.yview())
        vsb.grid(column=8, row=1, sticky="ns")
        self.reservation_tree.configure(yscrollcommand=vsb.set)
        reserve_dict = {
            self.name_login.get(): reserve_title_id,

        }
        pandas.DataFrame.from_dict(reserve_dict).to_csv("system reserve books.csv", index=False, mode="a")


        for column in self.reservation_tree['column']:
            self.reservation_tree.column(column, anchor=CENTER)
            self.reservation_tree.heading(column, text=column)
        for x in reservation_id:
            build_df = self.build_df[self.build_df.IDENTIFICATION_NO == (x)]
            df_rows = build_df.to_numpy().tolist()
            for row in df_rows:
                self.reservation_tree.insert("", "end", values=row)

        self.reservation_tree.grid(column=0,row=2,columnspan=8)

        self.reservation_page.mainloop()

    def return_to_main_page(self):
        self.reservation_page.destroy()
        def borrow_page2():
            self.main_page = Tk()
            self.main_page.title("Main page")
            self.main_page.config(padx=20, pady=20, highlightthickness=0, bg=WHITE)

            search_book_by = Label(text="Search book by: ", fg=NAVY_BLUE, bg=WHITE,
                                   font=("Roboto Slab", 14, "bold"))
            search_book_by.grid(column=0, row=0)
            title = Label(text="Title: ", fg=NAVY_BLUE, bg=WHITE, font=("Roboto Slab", 12))
            title.grid(column=0, row=1, sticky="e")
            author = Label(text="Author: ", fg=NAVY_BLUE, bg=WHITE, font=("Roboto Slab", 12))
            author.grid(column=0, row=2, sticky="e")
            subject_category = Label(text="Subject Category: ", fg=NAVY_BLUE, bg=WHITE, font=("Roboto Slab", 12))
            subject_category.grid(column=0, row=3, sticky="e")
            publication_date = Label(text="Publication Date: ", fg=NAVY_BLUE, bg=WHITE, font=("Roboto Slab", 12))
            publication_date.grid(column=2, row=2, sticky="e")

            self.title_entry = Entry(width=97, relief="groove", bg=WHITE)
            self.title_entry.grid(column=1, row=1, sticky="w", columnspan=3)
            self.author_entry = Entry(width=40, relief="groove", bg=WHITE)
            self.author_entry.grid(column=1, row=2, columnspan=2, sticky="w")
            self.subject_category_entry = Entry(width=40, relief="groove", bg=WHITE)
            self.subject_category_entry.grid(column=1, row=3, sticky="w")
            self.publication_date_entry = Entry(width=24, relief="groove", bg=WHITE)
            self.publication_date_entry.grid(column=3, row=2)
            self.reserve_button = Button(text="RESERVE", fg=WHITE, bg=NAVY_BLUE, width=20, command=self.reserve)
            self.reserve_button.grid(column=5, row=5)
            self.checkout_button = Button(text="CHECKOUT", fg=WHITE, bg="#6DA5A9", width=20, command=self.checkout)
            self.checkout_button.grid(column=0, row=5, sticky="w")
            self.search_button = Button(text="SEARCH", fg=WHITE, bg="pink", width=20, command=self.search)
            self.search_button.grid(column=3, row=3)
            self.add_to_cart = Button(text="ADD TO CART", fg=WHITE, bg="#7E370C", width=20, command=self.add_to_cart_f)
            self.add_to_cart.grid(column=7, row=5, sticky="e")
            self.my_reservations = Button(text="MY RESERVATIONS", fg=WHITE, bg="#97BFB4", width=20,
                                          command=self.my_reservations_page)
            self.my_reservations.grid(column=1, row=5, sticky="w")
            self.tree = ttk.Treeview()
            try:
                self.books_data = pandas.read_csv("List_of_books")
            except FileNotFoundError:
                self.books_data = pandas.read_csv("List of Books - Sheet1 (3).csv")
            self.books_data.columns = self.books_data.columns.str.replace(' ', '_')
            df_column = self.books_data.columns.values
            self.tree["column"] = list(self.books_data.columns)
            self.tree["show"] = "headings"
            vsb = ttk.Scrollbar(orient="vertical", command=self.tree.yview())
            vsb.grid(column=8, row=4, sticky="ns")
            self.tree.configure(yscrollcommand=vsb.set)

            for column in self.tree['column']:
                self.tree.heading(column, text=column)

            df_rows = self.books_data.to_numpy().tolist()
            for row in df_rows:
                self.tree.insert("", "end", values=row)
            self.tree.grid(column=0, row=4, columnspan=8)
        borrow_page2()

    def return_to_borrow_page(self):
        self.library_fines_page.destroy()
        def return_page_2():
            global days
            self.return_page = Tk()
            self.return_page.title("Return page")
            self.return_page.config(padx=20, pady=20, bg=WHITE)
            list_of_books_to_return = Label(text="List of books to return: ", fg=NAVY_BLUE, bg=WHITE,
                                            font=("Viga", 32, "bold"))
            list_of_books_to_return.grid(column=0, row=1, sticky="w")

            time = Label(text=f"{days} days left.", fg=NAVY_BLUE, bg=WHITE,
                         font=("Viga", 32, "bold"))
            time.grid(column=7, row=0, sticky="e")
            return_to_mainpage2 = Button(text="RETURN TO MAIN PAGE", fg=WHITE, bg=NAVY_BLUE, width=40, height=2,
                                         command=self.return_to_main2)
            return_to_mainpage2.grid(column=0, row=0, sticky="w")

            def timer_clock():
                global days
                days -= 1
                if days == 0:
                    messagebox.showwarning(title="Please Return Book",
                                           message="Your borrowed sessions has expired, please "
                                                   "return the books immediately")
                else:
                    time.config(text=f"{days} days left. ")

            please_text = Label(text="(Please check your library fines before returning the books)",
                                fg=NAVY_BLUE, bg=WHITE, font=("viga", 12,))
            please_text.grid(column=0, row=3, sticky="w")
            check_fines = Button(text="LIBRARY FINES", fg=WHITE, bg=NAVY_BLUE, width=31, height=2,
                                 activebackground=NAVY_BLUE, command=self.library_fines)
            check_fines.grid(column=2, row=3, columnspan=2)
            return_books = Button(text="RETURN BOOKS", fg=WHITE, bg="#6DA5A9", width=31, height=2,
                                  activebackground="#6DA5A9", command=self.return_book)
            return_books.grid(column=5, row=3, columnspan=2)
            confirm_button = Button(text="CONFIRM & RETURN", fg=WHITE, bg="#6DA5A9", width=31, height=2,
                                    activebackground="#6DA5A9", command=self.thank_you_page_2)
            confirm_button.grid(column=7, row=3, columnspan=2)

            self.return_book_tree = ttk.Treeview()
            self.build_df = self.books_data.copy()
            df_column = self.books_data.columns.values
            self.return_book_tree["column"] = list(self.books_data.columns)
            self.return_book_tree["show"] = "headings"
            vsb = ttk.Scrollbar(orient="vertical", command=self.return_book_tree.yview())
            vsb.grid(column=8, row=2, sticky="ns")
            self.return_book_tree.configure(yscrollcommand=vsb.set)
            borrow_dictionary = {
                self.name_login.get(): title_id,

            }
            pandas.DataFrame.from_dict(borrow_dictionary).to_csv("system borrowed books.csv", index=False, mode="a")

            for column in self.return_book_tree['column']:
                self.return_book_tree.column(column, anchor=CENTER)
                self.return_book_tree.heading(column, text=column)

            for x in borrow_dictionary[self.name_login.get()]:
                build_df = self.build_df[self.build_df.TITLE == (x)]
                df_rows = build_df.to_numpy().tolist()
                for row in df_rows:
                    self.return_book_tree.insert("", "end", values=row)

            self.return_book_tree.grid(column=0, row=2, columnspan=8)
            self.return_page.after(10000, timer_clock)

            self.return_page.mainloop()
        return_page_2()

    def library_fines(self):
        self.return_page.destroy()
        self.library_fines_page = Tk()
        self.library_fines_page.title("Library Fines")
        self.library_fines_page.config(padx=20,pady=20,bg=WHITE)
        self.library_fines_tree = ttk.Treeview()
        self.df_lf = pandas.read_csv("LIBRARY FINES - Sheet1.csv")
        self.library_fines_tree["column"] = list(self.df_lf.columns)
        self.library_fines_tree["show"] = "headings"
        self.return_to_main_page = Button(text="RETURN TO MAIN PAGE", fg=WHITE, bg=NAVY_BLUE, width=40,height=2,command=self.return_to_borrow_page)
        self.return_to_main_page.grid(column=0,row=0, sticky="w")
        for column in self.library_fines_tree['column']:
            self.library_fines_tree.column(column, anchor=CENTER)
            self.library_fines_tree.heading(column, text=column)

        with open('LIBRARY FINES - Sheet1.csv') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                violation = row['VIOLATION']
                fine = row['FINE']
                self.library_fines_tree.insert("", 0, values=(violation, fine))

        self.library_fines_tree.grid(column=0,row=1,columnspan=8)




        self.library_fines_page.mainloop()

    def return_to_main2(self):
        self.return_page.destroy()
        ApplicationWindow()




















