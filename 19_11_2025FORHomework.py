phrases = []
filtered_phrases = []

for i in range(10):
    phrase = input(f"Введите фразу {i+1}: ")
    phrases.append(phrase)

N = int(input("Введите целое число N: "))

for phrase in phrases:
    if len(phrase) >= N:
        filtered_phrases.append(phrase)

print("\nФразы длиной ≥", N)
for phrase in filtered_phrases:
    print(phrase)