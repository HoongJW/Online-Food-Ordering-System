def welcome():
    print("\n*----------------------------------------------------------------------------------*")
    print("               Welcome to the Spider Man Online Food Service                      ")
    print("*----------------------------------------------------------------------------------*")
    print("     1. Admin       2. Login as Customer       3. View as Guest       4. Exit")
    print("*----------------------------------------------------------------------------------*")
    option = input("Enter Option: ")
    while True:
        if option == "1":
            admin_login()  #F
        elif option == "2":
            Customer_login()  #F
        elif option == "3":
            Guest_Homepage()  #F
        elif option == "4":
            exit()
        else:
            print("Incorrect credentials. Please try again.")
            welcome()  #F


def admin_login():
    print("\n*----------------------------------------------------------------------------------*")
    print("*                   Welcome to the admin login page                                *")
    print("*               Please login to access the admin system                            *")
    print("*----------------------------------------------------------------------------------*")
    username = input("Username: ")
    password = input("Password: ")
    for line in open("admin.txt", "r").readlines():  # Read the lines
        login_info = line.split()  # Split on the space, and store the results in a list of two strings
        if username == login_info[0] and password == login_info[1]:
            print("Correct credentials!")
            admin_menu()  #F
        else:
            print("Incorrect credentials!")
            while True:
                dec = input("Enter M for main menu or R for admin login again: ")
                if dec.upper() == "M":
                    welcome()  #F
                elif dec.upper() == "R":
                    admin_login()  #F
                else:
                    print("Incorrect credentials. Please try again.")


def admin_menu():
    print("\n*----------------------------------------------------------------------------------*")
    print("*                                  Admin Homepage                                  *")
    print("*----------------------------------------------------------------------------------*")
    while True:
        print("1. Add Records Food in Category: A. Main Dish   B. Beverages    C. Desserts\n")
        print("2. Modify Item in Category     : A. Main Dish   B. Beverages    C. Desserts\n")
        print("3. Delete Item in Category     : A. Main Dish   B. Beverages    C. Desserts\n")
        print("4. Display All Records of      : A. Food Category      B. Food Item Category-Wise")
        print("                                 C. Customer Orders    D. ""Customer Payments\n")
        print("5. Search Specific Record of   : A. Customer Order     B. Customer Payment\n")
        print("6. Login Option Selection Page\n")
        print("7. Exit \n")
        print("*----------------------------------------------------------------------------------*")

        choice = input("Please enter the number of choice followed by alphabet (if exist):\n")
        if choice.upper() == "1A":
            add_item("MainDishes.txt", "Main Dish Category")  #F
        elif choice.upper() == "1B":
            add_item("Beverages.txt", "Beverages Category")  #F
        elif choice.upper() == "1C":
            add_item("Desserts.txt", "Desserts Category")  #F
        elif choice.upper() == "2A":
            modify_item("MainDishes.txt", "Main Dishes")  #F
        elif choice.upper() == "2B":
            modify_item("Beverages.txt", "Beverages")  #F
        elif choice.upper() == "2C":
            modify_item("Desserts.txt", "Desserts")  #F
        elif choice.upper() == "3A":
            delete_record_item("MainDishes.txt", "Main Dish")  #F
        elif choice.upper() == "3B":
            delete_record_item("Beverages.txt", "Beverages")  #F
        elif choice.upper() == "3C":
            delete_record_item("Desserts.txt", "Desserts")  #F
        elif choice.upper() == "4A":
            display_food_category()  #F
        elif choice.upper() == "4B":
            display_food_item_category_wise()  #F
        elif choice.upper() == "4C":
            display_customer_information("Customers_Orders.txt", "Customer Order")  #F
        elif choice.upper() == "4D":
            display_customer_information("Customers_Payment_Details.txt", "Customer Payment")  #F
        elif choice.upper() == "5A":
            search_customer_information("Customers_Orders.txt", "Customer Orders")  #F
        elif choice.upper() == "5B":
            search_customer_information("Customers_Payment_Details.txt", "Customer Payment")  #F
        elif choice == "6":
            welcome()  #F
        elif choice == "7":
            exit()
        else:
            print("Incorrect credentials. Please try again.!")


def add_item(filename, category):
    print("*----------------------------------------------------------------------------------*")
    print(f"                           Adding Records In {category}                         ")
    print("                      Fill up the form accordingly to add record                  ")
    print("*----------------------------------------------------------------------------------*")
    while True:
        decide = input(f"Click Y to add record in {category} or M for admin menu: \n")
        if decide.upper() == "Y":
            food_code = input("Item Code: ")
            food_name = input("Item Name: ")
            food_price = float
            while True:
                try:
                    food_price = float(input("Item Price: "))
                    break
                except ValueError:
                    print("Only integers allowed")
                    continue
            food_code_list = []
            food_code_valid = False
            f = open(filename, "r")
            for line in f:
                food_code1 = line.split()
                food_code_list.append(food_code1[0])
            with open(filename, "a") as file1:
                for i in food_code_list:
                    if food_code != i:
                        food_code_valid = True
                    else:
                        food_code_valid = False
                        break
                if food_code_valid:
                    file1.write("\n")
                    file1.write("{:<16}".format(food_code.upper()))
                    file1.write("{:<36}".format(food_name))
                    file1.write("~" + "{:.2f}".format(food_price))
                    print("Item Code \t\t Item Name \t\t Item Price")
                    print(food_code.upper() + "\t\t\t " + food_name + "\t\t\t " + str(food_price))
                    print(f"Record has been added into {category} list")
                else:
                    print("Food code already exists. Please choose a new food code.")
                    add_item(filename, category)  #F
            while True:
                dec = input("Press A to add more record or M to back to main menu:\n")
                if dec.upper() == "A":
                    add_item(filename, category)  #F
                elif dec.upper() == "M":
                    admin_menu()  #F
                else:
                    print("Incorrect credentials. Please try again.")
        elif decide.upper() == "M":
            admin_menu()  #F
        else:
            print("Incorrect credentials. Please try again.")


def modify_item(filename, category):
    print("*----------------------------------------------------------------------------------*")
    print(f"                       Modifying {category} Record Page                          ")
    print("*----------------------------------------------------------------------------------*")
    while True:
        decide = input(f"Enter Y to modify {category} record or M for admin menu: \n")
        if decide.upper() == "Y":
            item_id = input("Please enter the item code that you want to modify:\n")
            check_bool = False
            with open(filename) as my_file:
                for num, line in enumerate(my_file, 1):
                    if item_id.upper() in line:
                        print("Found at line: ", num - 1)
                        valid = num
                        print("Is this the data you want to modify?")
                        print("Item Code		Item Name			                Price (RM)")
                        print(line)
                        while True:
                            dec = input("Enter Y for confirmation or N to search for another item code:\n")
                            if dec.upper() == "Y":
                                new_item_code = input("Enter the new item code: ")
                                new_name = input("Enter the new item name: ")
                                while True:
                                    try:
                                        new_price = float(input("Enter the new item price: "))
                                        break
                                    except ValueError:
                                        print("Only integers allowed")
                                        continue
                                check_bool = True
                                break
                            elif dec.upper() == "N":
                                modify_item(filename, category)  #F
                            else:
                                print("Incorrect credentials. Please try again.")
            if check_bool:
                new_list = "{:<16}".format(new_item_code.upper()) + \
                           "{:<36}".format(new_name) + "~" + "{:.2f}".format(new_price)
                my_file = open(filename, "r")
                data = my_file.read()
                li = data.splitlines()
                li[(valid - 1)] = new_list
                my_file.close()
                my_file1 = open(filename, "w")
                for line in li:
                    if line in li[0:-1]:
                        my_file1.writelines(line+"\n")
                    if line in li[-1]:
                        my_file1.writelines(line)
                my_file1.close()
                print("Item Code		Item Name			                Price (RM)")
                print(li[(valid -1)])
                print("Record has been successfully modified.")
                while True:
                    dec1 = input("Enter A to modify another record / M for admin menu / E for exit:\n")
                    if dec1.upper() == "A":
                        modify_item(filename, category)  #F
                    elif dec1.upper() == "M":
                        admin_menu()  #F
                    if dec1.upper() == "E":
                        exit()
                    else:
                        print("Incorrect credentials. Please try again.")
            else:
                print("Incorrect credentials. Please try again.")
                while True:
                    dec1 = input("Enter A to modify another record / M for admin menu / E for exit:\n")
                    if dec1.upper() == "A":
                        modify_item(filename, category)  #F
                    elif dec1.upper() == "M":
                        admin_menu()  #F
                    elif dec1.upper() == "E":
                        exit()
                    else:
                        print("Incorrect credentials. Please try again.")
        if decide.upper() == "M":
            admin_menu()  #F
        else:
            print("Incorrect credentials. Please try again.")


def display_food_category():
    print("*----------------------------------------------------------------------------------*")
    print("*                      Displaying All Item Category                                *")
    print("*----------------------------------------------------------------------------------*")
    file = open("ItemCategory.txt", "r")
    content = file.read()
    print(content)
    while True:
        decide = input("Enter M for admin menu or E for exit:\n")
        if decide.upper() == "M":
            admin_menu()  #F
        if decide.upper() == "E":
            exit()  #F
        else:
            print("Incorrect credentials. Please try again.")


def display_food_item_category_wise():
    print("*----------------------------------------------------------------------------------*")
    print("*               Displaying All Records in Food Item Category-Wise                  *")
    print("*----------------------------------------------------------------------------------*")
    file = open("ItemCategory.txt", "r")
    content = file.read()
    print(content)
    while True:
        category = input("Please enter which category to view all the records / M for main menu / E for Exit:\n")
        if category.upper() == "M":
            admin_menu()
        elif category.upper() == "E":
            exit()
        elif category == "1":
            file1 = "MainDishes.txt"
            break
        elif category == "2":
            file1 = "Beverages.txt"
            break
        elif category == "3":
            file1 = "Desserts.txt"
            break
        else:
            print("Incorrect credentials. Please try again.")
    file2 = open(file1, "r")
    content1 = file2.read()
    print(content1)
    while True:
        decide = input("Enter M for admin menu / B for previous page / E for Exit:\n")
        if decide.upper() == "M":
            admin_menu()  #F
        elif decide.upper() == "B":
            display_food_item_category_wise()  #F
        elif decide.upper() == "E":
            exit()  #F
        else:
            print("Incorrect credentials. Please try again.")


def display_customer_information(filename, category):
    print("*----------------------------------------------------------------------------------*")
    print(f"                Displaying All the Records of {category}                      ")
    print("*----------------------------------------------------------------------------------*")
    file = open(filename, "r")
    content = file.read()
    print(content)
    while True:
        decide = input("Enter M for admin menu or E for exit:\n")
        if decide.upper() == "M":
            admin_menu()  #F
        elif decide.upper() == "E":
            exit()  #F
        else:
            print("Incorrect credentials. Please try again.")


def search_customer_information(filename, category):
    print("*----------------------------------------------------------------------------------*")
    print(f"                  Searching for Specific Record of {category}                ")
    print("*----------------------------------------------------------------------------------*")
    while True:
        decide = input(f"Enter Y to search {category} record or M for admin menu: \n")
        if decide.upper() == "Y":
            order_id = input("Please enter the customer order ID that you are searching for:\n")
            file = open(filename, "r")
            check_bool = False
            print("Order ID        Username        Item Code       Quantity")
            for line in file:
                check = line.split()
                if order_id.upper() != check[0]:
                    continue
                check_bool = True
                print(line.strip())
            if not check_bool:
                print("\nInvalid Order ID. Please try again")
            while True:
                decide = input("\nEnter Y for another search / M for admin menu / E for exit:\n")
                if decide.upper() == "Y":
                    search_customer_information(filename, category)  #F
                elif decide.upper() == "M":
                    admin_menu()  #F
                elif decide.upper() == "E":
                    exit()  #F
                else:
                    print("Incorrect credentials. Please try again.")
        elif decide.upper() == "M":
            admin_menu()  #F
        else:
            print("Incorrect credentials. Please try again")


def delete_record_item(filename, category):
    print("*----------------------------------------------------------------------------------*")
    print(f"                  Deleting the Specific Record of {category}                ")
    print("*----------------------------------------------------------------------------------*")
    while True:
        decide = input(f"Enter Y to delete {category} record or M for admin menu: \n")
        if decide.upper() == "Y":
            item_id = input(f"Enter the {category} code to be deleted: ")
            check_bool = False
            with open(filename, "r") as a_file:
                for num, line in enumerate(a_file, 1):
                    if item_id.upper() in line:
                        print("Found at line:", num)
                        valid = num
                        print(line)
                        dec = input("Enter Y for confirmation or M to search for another item code:\n")
                        if dec.upper() == "Y":
                            check_bool = True
                            break
                        elif dec.upper() == "M":
                            delete_record_item(filename, category)  #F
                        else:
                            print("Incorrect credentials. Please try again.")
                            delete_record_item(filename, category)  #F
            if check_bool:
                my_file = open(filename, "r")
                lines = my_file.read()
                li = lines.splitlines()
                del li[(valid - 1)]
                my_file.close()
                my_file1 = open(filename, "w+")
                for line in li:
                    if line in li[0:-1]:
                        my_file1.writelines(line + "\n")
                    if line in li[-1]:
                        my_file1.writelines(line)
                my_file1.close()
                print("Record has been successfully deleted.")
                while True:
                    dec1 = input("Enter A to delete another record / M for admin menu / E for exit:\n")
                    if dec1.upper() == "A":
                        delete_record_item(filename, category)  #F
                    elif dec1.upper() == "M":
                        admin_menu()  #F
                    elif dec1.upper() == "E":
                        exit()  #F
                    else:
                        print("Incorrect credentials. Please try again")
            else:
                print("Incorrect Credentials. Please try again")
                while True:
                    dec1 = input("Enter A to delete another record / M for admin menu / E for exit:\n")
                    if dec1.upper() == "A":
                        delete_record_item(filename, category)  #F
                    elif dec1.upper() == "M":
                        admin_menu()  #F
                    elif dec1.upper() == "E":
                        exit()  #F
                    else:
                        print("Incorrect Credentials. Please try again")
        elif decide.upper() == "M":
            admin_menu()  #F
        else:
            print("Incorrect credentials. Please try again")


def Customer_login():
    print("\n*----------------------------------------------------------------------------------*")
    print("*                               CUSTOMER LOGIN PAGE                                *")
    print("*----------------------------------------------------------------------------------*")
    print("                    Please login to access the customer homepage                    ")
    print("*----------------------------------------------------------------------------------*")
    username = input("Username: ")
    password = input("Password: ")
    with open("Customer.txt", 'r') as f:
        for line in f:
            login_info = line.split()
            if username == login_info[0] and password == login_info[1]:
                acc_valid = True
                break
            else:
                acc_valid = False

    if acc_valid:
        print(f"Correct credentials! Welcome Back {username}!")
        Customer_Homepage(username)  #F
    else:
        print("\nInvalid username or Password! Do you want to try again? Y/N")
        while True:
            choice = input("Enter option here: ")
            if choice.upper() == 'Y':
                Customer_login()  #F
            elif choice.upper() == 'N':
                welcome()  #F
            else:
                print("Invalid value, please try again.")


def Customer_Homepage(active_user):
    print("\n*----------------------------------------------------------------------------------*")
    print("*                               CUSTOMER HOMEPAGE                                  *")
    print("*----------------------------------------------------------------------------------*")
    print(f" user: {active_user}                                                                ")
    print("                    Select a choice from main menu to proceed                       ")
    print("                    1. View Available Food Category                                 ")
    print("                    2. Order Food Items                                             ")
    print("                    3. View Shopping Cart                                           ")
    print("                    4. Logout                                                       ")
    print("*----------------------------------------------------------------------------------*")
    while True:
        choice = input("Enter option: ")
        if choice == '1':
            FoodCategory(active_user)  #F
        elif choice == '2':
            Customer_Food_Menu(active_user)  #F
        elif choice == '3':
            Shopping_Cart(active_user)  #F
        elif choice == '4':
            welcome()  #F
        else:
            print("Incorrect credentials! Please try again: ")


def FoodCategory(active_user):
    print("\n*----------------------------------------------------------------------------------*")
    print("*                                   FOOD CATEGORY                                  *")
    print("*----------------------------------------------------------------------------------*")
    print("Spider Man Online Food Services specialize in three food categories:")
    with open("ItemCategory.txt", "r") as f:
        f_content = f.read()
        print(f_content + "\n")
    print("Do you want to start ordering now? Y/N")
    print("*----------------------------------------------------------------------------------*")

    while True:
        option = input("Enter option here: ")
        if option.upper() == 'Y':
            Customer_Food_Menu(active_user)  #F
        elif option.upper() == 'N':
            Customer_Homepage(active_user)  #F
        else:
            print("Incorrect credentials! Please try again: ")


def Customer_Food_Menu(active_user):
    print()
    print("\n*----------------------------------------------------------------------------------*")
    print("*                                   FOOD MENU                                      *")
    print("*----------------------------------------------------------------------------------*")
    print(f" user: {active_user}                                                                ")
    print("                     Select a choice from Food Menu to add your order               ")
    print("                     Go to:                                                         ")
    print("                     1. Main Dishes                                                 ")
    print("                     2. Beverages                                                   ")
    print("                     3. Desserts                                                    ")
    print("                     Press M to back to main menu                                   ")
    print("*----------------------------------------------------------------------------------*")

    while True:
        choice = input("Enter option here: ")
        if choice == '1':
            with open('MainDishes.txt', 'r') as m:
                m_contents = m.read()
                print("\n*----------------------------------------------------------------------------------*")
                print("*                                Main Dish                                         *")
                print("*----------------------------------------------------------------------------------*")
                print(m_contents)
                Add_To_Cart(active_user)  #F
        elif choice == '2':
            with open('Beverages.txt', 'r') as m:
                m_contents = m.read()
                print("\n*----------------------------------------------------------------------------------*")
                print("*                                Beverages                                         *")
                print("*----------------------------------------------------------------------------------*")
                print(m_contents)
                Add_To_Cart(active_user)  #F
                break
        elif choice == '3':
            with open('Desserts.txt', 'r') as m:
                m_contents = m.read()
                print("\n*----------------------------------------------------------------------------------*")
                print("*                                Desserts                                         *")
                print("*----------------------------------------------------------------------------------*")
                print(m_contents)
                Add_To_Cart(active_user)  #F
                break
        elif choice.upper() == 'M':
            Customer_Homepage(active_user)  #F
        else:
            print("Incorrect credentials. Please try again.")


def Add_To_Cart(active_user):
    print("*----------------------------------------------------------------------------------*")
    print(f" user: {active_user}")
    with open('Customer_Cart.txt', 'a') as m:
        while True:
            order_choice = input(" Enter Item Code or F to return to food menu here: ")
            order_choice = order_choice.upper()[0] + order_choice[1:4]
            item_code_check = Item_Code_Validation(order_choice)
            if order_choice.upper() == 'F':
                Customer_Food_Menu(active_user)  #F
            if item_code_check:
                while True:
                    try:
                        quantity = int(input(" Enter Quantity: "))
                        break
                    except ValueError:
                        print(" Only integers allowed.")

                m.write("{:<16}".format(active_user))
                m.write("{:<16}".format(order_choice))
                m.write(str(quantity) + "\n")
                break
            else:
                print(" Incorrect credentials! Please try again.")
                continue

    print(" Do you want to add another item into your cart? Y/N")
    while True:
        choice = input(" Enter option here: ")
        if choice.upper() == 'Y':
            Customer_Food_Menu(active_user)  #F
        elif choice.upper() == 'N':
            print(" Do you want to confirm payment now? Y/N")
            choice = input(" Enter option here: ")
            if choice.upper() == 'Y':
                Shopping_Cart(active_user)  #F
            if choice.upper() == 'N':
                Customer_Homepage(active_user)  #F
        else:
            print(" Incorrect credentials! Please try again.")


def Shopping_Cart(active_user):
    customer_order_list, item_code_list, price_list, food_name_list, food_name = [], [], [], [], []

    print("\n*----------------------------------------------------------------------------------*")
    print("*                               Shopping Cart                                      *")
    print("*----------------------------------------------------------------------------------*")
    print(f" user: {active_user}")
    print()
    print(" Item Code	 	 Item Name			                 Price (RM)      Quantity       ")
    with open('Customer_Cart.txt', 'r') as m:
        for i in m:
            line = i.split()
            if active_user == line[0]:
                customer_order_list.append(line)

    with open("MainDishes.txt", 'r') as code1, open("Desserts.txt", 'r') as code2, open("Beverages.txt", 'r') as code3:
        line1, line2, line3 = code1.readlines()[1:], code2.readlines()[1:], code3.readlines()[1:]
        total_line = line1 + line2 + line3
        for line in total_line:
            order = line.split('~')
            item_code_list.append(line[0:4])
            price_list.append(float(order[-1].strip('\n')))

        official_total_line = []
        for element in total_line:
            official_total_line.append(element.strip())
        total = 0

        for i in customer_order_list:
            for j in range(len(official_total_line)):
                if item_code_list[j] == i[1]:
                    print(" " + official_total_line[j] + "\t\t\t\t" + i[2])
                    price = price_list[j] * float(i[2])
                    total += price

        total = round(total, 2)
        print()
        print(f" Total: RM{total}")
        if total == 0:
            print(" Currently there are not items in your cart. Press M to go back to main menu.")
            print("*----------------------------------------------------------------------------------*")
            while True:
                choice = input("Enter Option: ")
                if choice.upper() == "M":
                    Customer_Homepage(active_user)  #F
                else:
                    print("Incorrect credentials. Please try again.")

        else:
            print("\n Press D to Delete Item. Press Q to change order quantity.\n"
                  " Press P to Pay now. Press M to go back to main menu. ")
            print("*----------------------------------------------------------------------------------*")
            while True:
                choice = input("Enter Option: ")
                if choice.upper() == 'P':
                    Checkout(active_user, total)  #F
                elif choice.upper() == 'D':
                    Delete_Shopping_Cart(active_user, customer_order_list)
                    Shopping_Cart(active_user)  #F
                elif choice.upper() == 'M':
                    print("We will redirect you to the customer homepage.")
                    Customer_Homepage(active_user)  #F
                elif choice.upper() == 'Q':
                    Modify_Quantity(active_user, customer_order_list)
                    Shopping_Cart(active_user)  #F
                else:
                    print("Incorrect credentials. Please try again.")


def Checkout(active_user, total):
    print("\n*----------------------------------------------------------------------------------*")
    print("                                 Checkout Page                                       ")
    print("*----------------------------------------------------------------------------------*")
    print("\n Payment Method:\n"
          "  1. Credit Card\n"
          "  2. Cash\n"
          "  3. Online Banking\n"
          "  4. SpiderPay\n"
          " Enter M to cancel payment.\n")
    print("*----------------------------------------------------------------------------------*")

    while True:
        option = input("Enter option here: ")
        if option == '1':
            payment_method = 'Credit Card'
            Add_Customer_Order_Details(active_user, payment_method, total)  #F
            break
        elif option == '2':
            payment_method = 'Cash'
            Add_Customer_Order_Details(active_user, payment_method, total)  #F
            break
        elif option == '3':
            payment_method = 'Online Banking'
            Add_Customer_Order_Details(active_user, payment_method, total)  #F
            break
        elif option == '4':
            payment_method = 'SpiderPay'
            Add_Customer_Order_Details(active_user, payment_method, total)  #F
            break
        elif option.upper() == 'M':
            Customer_Homepage(active_user)  #F
            break
        else:
            print("Incorrect credentials. Please try again.")

    print("*----------------------------------------------------------------------------------*")
    print("                 Transaction successful! Enjoy your meal !!")
    print("*----------------------------------------------------------------------------------*")
    Customer_Homepage(active_user)  #F


def Item_Code_Validation(order):
    item_code_list = []
    with open("MainDishes.txt", 'r') as code1, open("Desserts.txt", 'r') as code2, open("Beverages.txt", 'r') as code3:
        line1, line2, line3 = code1.readlines()[1:], code2.readlines()[1:], code3.readlines()[1:]
        for itemCode in line1:
            item_code_list.append(itemCode[0:4])
        for itemCode in line2:
            item_code_list.append(itemCode[0:4])
        for itemCode in line3:
            item_code_list.append(itemCode[0:4])

        for test in item_code_list:
            if order == test:
                return True
        return False


def Add_Customer_Order_Details(active_user, payment_method, total):
    with open("Customer_Cart.txt", 'r') as cart, open("Customers_Orders.txt", 'a') as order, \
            open("Customers_Payment_Details.txt", 'a') as pay:
        lines = cart.readlines()[1:]
        order_id = Generate_order_id()
        for line in lines:
            rec = line.split()
            if active_user == rec[0]:
                order.writelines("{:16}".format(order_id) + "{:16}".format(line))
        pay.writelines("{:16}".format(order_id)
                       + "{:16}".format(active_user) + "{:16}".format(payment_method)
                       + "{:16}".format(total))
        pay.write("\n")

        with open("Customer_Cart.txt", 'w') as delete_cart:
            delete_cart.write("Username        ItemCode        Quantity\n")
            for line in lines:
                rec = line.split()
                if active_user != rec[0]:
                    delete_cart.write(line)  #F


def Generate_order_id():
    with open("Customers_Orders.txt", 'r') as read:
        latest_rec = read.readlines()[-1]
        if "OrderID" in latest_rec:
            new_id = "T001"
            return new_id
        latest_id = latest_rec[:5].strip('T')
        tmp = str(int(latest_id) + 1)
        new_id = "T" + "00" + tmp
    return new_id


def Delete_Shopping_Cart(active_user, delete_record):
    print("\n*----------------------------------------------------------------------------------*")
    print("                         Which order do you want to delete?")
    print("*----------------------------------------------------------------------------------*")
    with open("Customer_Cart.txt", 'r') as cart:
        lines = cart.readlines()

    while True:
        option = input("Enter ItemCode or C to return to cart: ")
        if option.upper() == 'C':
            return
        option = option.upper()[0] + option[1:4]
        valid = Item_Code_Validation(option)
        if valid:
            for line in delete_record:
                if option in line:
                    with open("Customer_Cart.txt", 'w') as cart:
                        for num, line2 in enumerate(lines):
                            if option == line2.strip('\n').split()[1] and active_user == line2.split()[0]:
                                continue
                            cart.write(line2)
                        print("Your record has been deleted. ")
                        return
            print("No searched ItemCode exist in your cart. Please try again.")
        else:
            print("Incorrect credentials. Please try again.")


def Modify_Quantity(active_user, modify_record):
    print("\n*----------------------------------------------------------------------------------*")
    print("                      Which order do you want to change its quantity?")
    print("*----------------------------------------------------------------------------------*")
    with open("Customer_Cart.txt", 'r') as cart:
        lines = cart.readlines()

    while True:
        option = input("Enter ItemCode or C to return to cart: ")
        if option.upper() == 'C':
            return
        option = option.upper()[0] + option[1:4]
        valid = Item_Code_Validation(option)
        if valid:
            for line in modify_record:
                if option in line:
                    while True:
                        try:
                            quantity = int(input("Enter quantity: "))
                            if quantity == 0:
                                print("Minimum quantity is 1. Please try again.")
                                continue
                            break
                        except ValueError:
                            print("Incorrect credentials. Please try again.")
                    with open("Customer_Cart.txt", 'w') as cart:
                        for line2 in lines:
                            if option == line2.strip('\n').split()[1] and active_user == line2.split()[0]:
                                cart.write("{:16}".format(active_user))
                                cart.write("{:16}".format(option))
                                cart.write(str(quantity) + '\n')
                                continue
                            cart.write(line2)
                        print("Your record has been modified. ")
                        return
            print("No searched ItemCode exist in your cart. Please try again.")
        else:
            print("Incorrect credentials. Please try again.")


def Guest_Homepage():
    print("\n*----------------------------------------------------------------------------------*")
    print("*                                GUEST HOMEPAGE                                    *")
    print("*----------------------------------------------------------------------------------*")
    print("                         Select a choice from to proceed:                           ")
    print("                         1. View Food Category and Food Items                       ")
    print("                         2. Register New Account                                    ")
    print("                         3. Return to Welcome page                                  ")
    print("*----------------------------------------------------------------------------------*")

    while True:
        option = input("Enter option here: ")
        if option == '1':
            Guest_FoodItems()  #F
        if option == '2':
            Guest_Create_Customer_Acc()  #F
        if option == '3':
            welcome()  #F
        else:
            print("Incorrect credentials. Please try again.")


def Guest_FoodItems():
    print("\n*----------------------------------------------------------------------------------*")
    print("*                                Food Menu                                         *")
    print("*----------------------------------------------------------------------------------*")
    print("                     Select a choice from Food Menu to proceed.                     ")
    print("                                View Details of:                                    ")
    print("                                1. Main Dishes                                      ")
    print("                                2. Beverages                                        ")
    print("                                3. Desserts                                         ")
    print("                         Press M to go back to Guest homepage                       ")
    print("*----------------------------------------------------------------------------------*")

    while True:
        choice = input("Enter option here: ")
        if choice == '1':
            with open('MainDishes.txt', 'r') as m:
                m_contents = m.read()
                print("\n*----------------------------------------------------------------------------------*")
                print("*                                Main Dish                                         *")
                print("*----------------------------------------------------------------------------------*")
                print(m_contents)
                Guest_Page_Options()  #F
        if choice == '2':
            with open('Beverages.txt', 'r') as m:
                m_contents = m.read()
                print("\n*----------------------------------------------------------------------------------*")
                print("*                                Beverages                                         *")
                print("*----------------------------------------------------------------------------------*")
                print(m_contents)
                Guest_Page_Options()  #F
        if choice == '3':
            with open('Desserts.txt', 'r') as m:
                m_contents = m.read()
                print("\n*----------------------------------------------------------------------------------*")
                print("*                                Desserts                                         *")
                print("*----------------------------------------------------------------------------------*")
                print(m_contents)
                Guest_Page_Options()  #F
        if choice.upper() == 'M':
            Guest_Homepage()  #F
        else:
            print("Incorrect credentials! Please try again: ")


def Guest_Create_Customer_Acc():
    print()
    print("*----------------------------------------------------------------------------------*")
    print("*                               Register New Account                               *")
    print("*----------------------------------------------------------------------------------*")
    print("                    Hello! Register New account to start ordering!                  ")
    print("*----------------------------------------------------------------------------------*")
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    username_list = []
    username_valid = False
    with open("Customer.txt", 'r') as f:
        for line in f:
            _username = line.split()
            username_list.append(_username[0])

        with open("Customer.txt", 'a') as addRec:
            for i in username_list:
                if new_username != i:
                    username_valid = True
                else:
                    username_valid = False
                    break

            if username_valid:
                addRec.write('\n' + new_username)
                addRec.write(' ' + new_password)
                print(f"Successfully registered! Please login again to access to Customer Homepage.")
                addRec.close()
                return welcome()

            print("\nUsername already exists. Do you want to try again? Y/N")
            while True:
                option = input("Enter option here: ")
                if option.upper() == 'Y':
                    Guest_Create_Customer_Acc()  #F
                if option.upper() == 'N':
                    Guest_Homepage()  #F
                else:
                    print("Incorrect credentials. Please try again.")


def Guest_Page_Options():
    print("*----------------------------------------------------------------------------------*")
    print("Select option and we will redirect you to a new page: \n"
          "H - Go to Customer homepage\n"
          "F - Go to Food Menu\n"
          "C - Register a New account\n"
          "W - Return to Welcome page")

    while True:
        option = input("Enter option here: ")
        if option.upper() == 'H':
            Guest_Homepage()  #F
        if option.upper() == 'F':
            Guest_FoodItems()  #F
        if option.upper() == 'C':
            Guest_Create_Customer_Acc()  #F
        if option.upper() == 'W':
            welcome()  #F
        else:
            print("Incorrect credentials. Please try again. ")


welcome()
