#Editor Muhammad Syifa Ridhoni (220535604679)
#S1 Teknik Informatika Offering C
#Tugas Algoritma Pemrograman

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
