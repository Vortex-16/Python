import cowsay

for name in cowsay.char_names:
    print(f"\n--- {name} says ---")
    cowsay.get_output_string(name, "Python is awesome!")

