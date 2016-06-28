from collections import defaultdict

sr = {0: 0.0,
      8: 2.8284271247461903,
      2: 1.4142135623730951,
      4: 2.0,
      6: 2.449489742783178
      }

text = input("What is your favorite number between 0 and 10: ")
n = int(text)

# ans = "UNKNOWN"
# if n in sr:
#     ans = sr[n]

ans = sr.get(n, "UNKNOWN")

sr2 = defaultdict(default_factory=-1)
sr2.update(sr)
# data = [
#     sr.get(n, -1)
#     for n in sr.keys()
#     if sr.get(n, -1) > 2
# ]
data = [
    sr2[n]
    for n in sr2.keys()
    if sr2[n] > 2
]
print(data)

print("Cool, the square root of {} is {}".format(
    n, ans
))
