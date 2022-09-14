#Editor Muhammad Syifa Ridhoni (220535604679)
#S1 Teknik Informatika Offering C
#Tugas Algoritma Pemrograman
name = input("What do you want to type? (Hello/Hello, Newman/How are you doing?/What's happening?) ").strip()

match name:
    case "Hello"|"Hello, Newman":
        print("$0")
    case "How are you doing?":
        print("$20")
    case "What's happening?":
        print("$100")
    case _:
        print("???")
