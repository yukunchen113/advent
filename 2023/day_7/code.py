from collections import defaultdict, Counter
from advent import mark

def parse_input(data_file):
    with open(data_file) as f:
        lines = [i.replace("\n", "") for i in f.readlines()]
    return lines

ORDER_PT2 = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2","J"]

def scoring(card):
    card, _ = card
    num_j = len([i for i in card if i == "J"])
    counts = defaultdict(lambda: 0)
    for i in card:
        if i != "J":
            counts[i] += 1
    if not len(counts.values()):
        return ((5,0), [-ORDER_PT2.index("J") for _ in range(5)])
    max_val = max(counts.values()) + num_j
    j_conv = [c for c,i in counts.items() if i == max(counts.values())][0]
    counts[j_conv]+=num_j
    if max_val == 2:
        okind = (max_val, len([i for i in counts.values() if i == 2]))
    elif max_val == 3:
        okind = (max_val, len([i for i in counts.values() if i == 2]))
    else:
        okind = (max_val, 0)
    return (okind, [-ORDER_PT2.index(i) for i in card])

@mark.solution(test=5905)
def pt2(data_file):
    data = parse_input(data_file)
    cards = []
    for line in data:
        a, b = line.split()
        cards.append((a, int(b)))
    cards = sorted(cards, key=scoring)
    assert len(set(i for i in cards)) == len(cards)
    return sum(b*idx for idx,(_,b) in enumerate(cards,1))

ORDER = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

def scoring_pt1(card):
    card, _ = card
    counts = defaultdict(lambda: 0)
    for i in card:
        counts[i] += 1
    max_val = max(counts.values())
    if max_val == 2:
        okind = (max_val, len([i for i in counts.values() if i == 2]))
    elif max_val == 3:
        okind = (max_val, len([i for i in counts.values() if i == 2]))
    else:
        okind = (max_val, 0)
    return (okind, [-ORDER.index(i) for i in card])

@mark.solution(test=6440)
def pt1(data_file):
    data = parse_input(data_file)
    cards = []
    for line in data:
        a, b = line.split()
        cards.append((a, int(b)))
    cards = sorted(cards, key=scoring_pt1)
    assert len(set(i for i in cards)) == len(cards)
    return sum(b*idx for idx,(_,b) in enumerate(cards,1))


@mark.solution(test=6440)
def pt1_clean(data_file):
    order = "AKQJT98765432"
    data = parse_input(data_file)
    cards = sorted(
        [tuple(line.split()) for line in data], 
        key=lambda card: (
            tuple(i for _,i in Counter(card[0]).most_common(2)),
            [-order.index(i) for i in card[0]]
        )
    )
    return sum(int(b)*idx for idx,(_,b) in enumerate(cards,1))


@mark.solution(test=5905)
def pt2_clean(data_file):
    order = "AKQT98765432J"
    def scoring_eff_pt2(card):
        counts = Counter(card[0])
        num_j = counts.pop("J", 0)
        counts["J" if not len(counts) else counts.most_common(1)[0][0]]+=num_j
        return (tuple(i for _,i in counts.most_common(2)), [-order.index(i) for i in card[0]])
    data = parse_input(data_file)
    cards = sorted([line.split() for line in data], key=scoring_eff_pt2)
    return sum(int(b)*idx for idx,(_,b) in enumerate(cards,1))

