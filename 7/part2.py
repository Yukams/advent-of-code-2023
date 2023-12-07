from utils.dataReader import read_data


def isFiveK(hand):
    return hand.count(hand[0]) == 5


def isFourK(hand):
    cnt = hand.count(hand[0])
    return cnt == 4 or cnt == 1 and hand.count(hand[1]) == 4


def isFull(hand):
    cnt = hand.count(hand[0])
    return (cnt == 2 or cnt == 3) and len(set(hand)) == 2


# As we use it after checking a Full, no need to check if the two other numbers are differents
def isThreeK(hand):
    return hand.count(hand[0]) == 3 or hand.count(hand[1]) == 3 or hand.count(hand[2]) ==3


def isTwoPair(hand):
    setOfNumbers = set(hand)
    return len(setOfNumbers) == 3 and len(list(filter(lambda x: hand.count(x) == 2, setOfNumbers))) == 2


def isPair(hand):
    return len(set(hand)) == 4


def addSubScore(hand, score):
    for value in hand:
        if value == 'A':
            score += 'e'
        elif value == 'K':
            score += 'd'
        elif value == 'Q':
            score += 'c'
        elif value == 'J':
            score += '1'
        elif value == 'T':
            score += 'a'
        else:
            score += value

    return score


def calculate_score(hand):
    score = '0'
    hasJoker = hand.count('J') != 0
    lettersInHand = list(set(hand.replace('J', '')))
    if len(lettersInHand) == 0:
        lettersInHand.append('K')
    nbCalc = 1 if not hasJoker else len(lettersInHand)
    
    for i in range(nbCalc):
        tmpHand = hand
        if hasJoker:
            tmpHand = tmpHand.replace('J', lettersInHand[i])
        print(tmpHand)
        
        tmpScore = '0'
        if isFiveK(tmpHand):
            tmpScore = '6'
        elif isFourK(tmpHand):
            tmpScore = '5'
        elif isFull(tmpHand):
            tmpScore = '4'
        elif isThreeK(tmpHand):
            tmpScore = '3'
        elif isTwoPair(tmpHand):
            tmpScore = '2'
        elif isPair(tmpHand):
            tmpScore = '1'

        print(tmpScore)

        if int(tmpScore) > int(score):
            score = tmpScore

    return addSubScore(hand, score)


# data = read_data('baseData.txt')
# data = read_data('testData.txt')
data = read_data('challengeData.txt')
data = sum([bid*(idx+1) for idx, (bid, score) in enumerate(
                  sorted([(int(bid), int(calculate_score(hand), 16)) for hand, bid in (hand.strip().split(" ") for hand in data.split("\n"))], key=lambda x: x[1])
              )])

print(data)
