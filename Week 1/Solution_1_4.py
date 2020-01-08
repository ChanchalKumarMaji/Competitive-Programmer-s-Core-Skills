# python3

def solve(cards):
    suit = set()
    for card in cards:
        suit.add(card[1])
    if len(suit) != 1:
        return "NO"
    flush1 = []
    d1 = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,}
    flush2 = []
    d2 = {'A': 1, 'K': 13, 'Q': 12, 'J': 11, 'T': 10,}
    for card in cards:
        if card[0].isdigit():
            flush1.append(int(card[0]))
            flush2.append(int(card[0]))
        else:
            flush1.append(int(d1[card[0]]))
            flush2.append(int(d2[card[0]]))
    flush1.sort()
    flush2.sort()
    if flush1[4]-flush1[0]==4 or flush2[4]-flush2[0]==4:
        return "YES"
    return "NO"


if __name__ == '__main__':
    cards = input().split()
    print(solve(cards))
