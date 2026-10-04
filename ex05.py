# %% [markdown]
# ### [ex05] Collections: a first look at a text

# %%
TEXT = """
Litwo! Ojczyzno moja! ty jesteś jak zdrowie;
Ile cię trzeba cenić, ten tylko się dowie,
Kto cię stracił. Dziś piękność twą w całej ozdobie
Widzę i opisuję, bo tęsknię po tobie.

Panno święta, co Jasnej bronisz Częstochowy
I w Ostrej świecisz Bramie! Ty, co gród zamkowy
Nowogródzki ochraniasz z jego wiernym ludem!
Jak mnie dziecko do zdrowia powróciłaś cudem
(Gdy od płaczącej matki, pod Twoją opiekę
Ofiarowany, martwą podniosłem powiekę;
I zaraz mogłem pieszo, do Twych świątyń progu
Iść za wrócone życie podziękować Bogu),
Tak nas powrócisz cudem na Ojczyzny łono.
Tymczasem przenoś moją duszę utęsknioną
Do tych pagórków leśnych, do tych łąk zielonych,
Szeroko nad błękitnym Niemnem rozciągnionych;
Do tych pól malowanych zbożem rozmaitem,
Wyzłacanych pszenicą, posrebrzanych żytem;
Gdzie bursztynowy świerzop, gryka jak śnieg biała,
Gdzie panieńskim rumieńcem dzięcielina pała,
A wszystko przepasane jakby wstęgą, miedzą
Zieloną, na niej z rzadka ciche grusze siedzą.
"""

# %%
lines = TEXT.strip().splitlines()
print(len(lines))
print(lines[0])
print(lines[-1])
print(lines[1:3])

# %%
PUNCTUATION = "!;,.()"

words = [w.strip(PUNCTUATION).lower() for w in TEXT.split()]
words = [w for w in words if w]  # drop empty strings

print(len(words), words[:8])

# %%
unique_words = set(words)
print(len(unique_words))
print("zdrowie" in unique_words, "python" in unique_words)

# %%
counts: dict[str, int] = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1

print(counts["do"], counts["tych"], counts["cudem"])

# %%
top = sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:5]
print(top)

for word, n in top:
    print(f"{word:>6} {'#' * n}")

# %%
lengths = {w: len(w) for w in unique_words}
longest = max(lengths, key=lengths.get)
print(longest, lengths[longest])

# %%
from collections import Counter

print(Counter(words).most_common(5))

# %%
bigrams = list(zip(words, words[1:]))
print(bigrams[:4])

after_do = Counter(nxt for prev, nxt in bigrams if prev == "do")
print(after_do.most_common())
