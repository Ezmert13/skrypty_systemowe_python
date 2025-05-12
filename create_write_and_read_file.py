with open("Testowy_plik.txt", "w") as f:
    f.write("Co to był za dzień, ostatnia debata stanowskiego")
    
with open("Testowy_plik.txt", "r") as f:
          data = f.read()

print(f"Tekst z pliku: {data}")
