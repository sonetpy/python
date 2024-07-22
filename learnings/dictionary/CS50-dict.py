# If I make a return type as list then you can modify data
def main():
    student = get_student()
    if student["name"] == "Virat":
        student["house"] = "India"
    print (f"{student["name"]} from {student["house"]}")

def get_student():
    name=input("Name: ")
    house=input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()