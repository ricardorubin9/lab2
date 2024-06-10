#Creat a dictionary

def Show_info(Info_Student):
    #STEP 4
    var_firstname=Info_Student['full_name'].split(' ')
    var_name=var_firstname[0]
    print (f"My name is {Info_Student['full_name']}, but you can call me Sir {var_name}.\nMy student ID is {Info_Student['student_id']}")



def Toppings(Info_Student,topping):
    #STEP 5
    Info_Student["pizza_toppings"].append (topping) 
    print(Info_Student)
    
    
def Show_pizzaTopping(Info_Student):
    #STEP 6
    list_Topping=Info_Student['pizza_toppings']
    print("\nMy favourite pizza toppings are:\n")
    for i in range(len(list_Topping)):
        print(f" -- {list_Topping[i].lower()}")

def Show_movieGenere(Info_Student):
    #STEP 7
    list_Genre=Info_Student['movies_genre']
    print("\nI like to watch: ")
    for i in range(len(list_Genre)):
        print(f"{list_Genre[i]}")
        if i<(len(list_Genre)-2):
            print(",")
        elif(i==len(list_Genre)-2):
            print(" and ")

def Show_movieTitles(Info_Student):
    #STEP 8
    list_Title=Info_Student['movies_title']
    print("\nSome of my favourite movies are: ")
    for i in range(len(list_Title)):
        print(f"{list_Title[i].capitalize()}")
        if i<(len(list_Title)-2):
            print(",")
        elif(i==len(list_Title)-2):
            print("and ")



def main():
    Info_Student = {
        "full_name": "Ricardo Yael Rubin Uriostegui",
        "student_id": "10340560",
        "pizza_toppings": ["PEPPERONI", "BACON", "CHILI"],
        "movies_title": ["exorcist", "conjure", "batman"],       
        "movies_genre": ["Horror", "Action", "Comedy"] 
    }  #STEP 2
    print(Info_Student)
    Info_Student["movies_title"].append ("Fast-Fourious")  #STEP 3
    Show_info(Info_Student)
    new_topping="PINEAPPLE"
    Toppings(Info_Student,new_topping)
    new_topping="SAUSAGE"
    Toppings(Info_Student,new_topping)
    new_topping="HOT_PEPPERS"
    Toppings(Info_Student,new_topping)
    Info_Student["pizza_toppings"].sort()  #Sort all pizza toppings
    print(Info_Student["pizza_toppings"])  #Show all pizza toppings sorted
    Show_pizzaTopping(Info_Student) #STEP 6
    Show_movieGenere(Info_Student)  #STEP 7
    Show_movieTitles(Info_Student)  #STEP 8
    
    
if __name__ =='__main__':
      main()    #STEP 1
    

