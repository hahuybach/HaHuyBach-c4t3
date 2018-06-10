alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
chunhapvao =input("Enter sth: ").lower()
for letter in range(len(alphabet)):
    if alphabet[letter] in chunhapvao:
        print(alphabet[letter],chunhapvao.count(alphabet[letter]))