import requests
import random



print("help")
idlist = ["25","329","531","551","30533","530","541","552","33303","30759","350"]
password = random.choice(idlist)
names = ["Charlie","Dave","Jeff","Carmen","Karen","Jeb","Sophia","Patty","Andy","Julia","Millie","Rob","Duncan","Larry"]
name = random.choice(names)
code = random.randint(1,5000)
database = False
run = True

while run:

    start = input("Enter...")
    if start == "help":
        print("use end to end game \n use access to get database \n use help to get id codes to use in database,"
              " \n use get to get information in database \n use leave to exit database \n"
              "use directive to get your goal \n"
              "use done to complete goals \n use login to login to notepad \n"
              "Hint: Don't use spaces")
    elif start == "hi":
        print("Hello there...")
    elif start == "end":
        run = False
    elif start == "access":
        database = True
        while database:
            data = input("In database...")
            if data == "help":
                for i in idlist:
                    print(str(i))

            elif data == "leave":
                database = False
                print("Exiting database...")
            elif data == "get":

                #Id to get
                id = input("id")

                #Url for getting
                url = "https://health.gov/myhealthfinder/api/v3/topicsearch.json?topicId=" + str(id)

                #turning data from url into dictionary in python
                response = requests.request("GET", url)
                list = response.json()

                if list["Result"]["Total"] <= 0:
                    print("Error")
                else:
                    print(list["Result"]["Resources"]["Resource"][0])
                    if list["Result"]["Resources"]["Resource"][0]["Id"] == password:
                        print("Favorite: Yes")
                    else:
                        print("Favorite: No")

    elif start == "directive":
        print("Your goal is to hack into this system and get the access codes to the planetary defense system(PDS). \n "
              "The person who had the code is now gone, their name is "+name+". \n "
            "The code was in their notepad so find their password. \n"
            "Their password is the id of their favorite database.")

    elif start == "login":
        username = input("Username...")
        notepassword = input("Password...")
        if username == name:
            if notepassword == password:
                print("Access granted... \n"
                      "Grocery list: \n"
                      "     Egg \n"
                      "     Milk \n"
                      "     More Egg \n"
                      "     Big Egg \n"
                      "     Bread \n"
                      "Codes: \n"
                      "     Safe: 1452 \n"
                      "     House: 4180 \n"
                      "     PDS: "+str(code))
            else:
                print("Wrong password...")
        else:
            print("No user detected...")
    elif start == "done":
        if code == int(input("Enter code...")):
            print("Mission complete...")
            run = False
        else:
            print("Error, wrong code...")
