#Tugas Algoritma Pemrograman
#Muhammad Syifa Ridhoni (220535604579)


def greeting(bismillah):
    bismillah = bismillah.strip().lower()
    if "hello" in bismillah:
        print("$0")
    elif bismillah[0] == "h":
        print("$20")
    else:
        print("$100")

alhamdulillah = input("Input Greeting: ")
greeting(alhamdulillah)