#Editor Muhammad Syifa Ridhoni (220535604679)
#S1 Teknik Informatika Offering C
#Tugas Algoritma Pemrograman
name = input("? ").strip()

match name:
    case "Hello"|"Hello, Newman":
        print("$0")
    case "How you doing?":
        print("20$")
    case "What's happening?":
        print("100")
    case _:
        print("???")