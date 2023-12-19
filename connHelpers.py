def isPerfect(lines):

    return 1 if len(lines) == 4 else 0



def isFail(lines):

    return 1 if len(set(lines[-1])) != 1 else 0


def isClutch(lines):

    if len(lines) == 7 and not isFail(lines) : 
        return 1 
    else:
        return 0

def isWin(lines):
    numCorrect = 0

    # newMessage = '\n'.join(lines)
    for x in lines:
        if len(set(x)) == 1:
            numCorrect += 1

    return 1 if numCorrect == 4 else 0


def getStats(message):

    lines = message.split('\n')
    lines = lines[2:]

    return isPerfect(lines), isFail(lines), isClutch(lines), isWin(lines)


def printStats(mention, totalPerfect, totalFails, totalClutches, totalWins):
    statsString : str = (
        f"**{mention} STATS:**\n"
        f"All Time Perfects: {totalPerfect}\n"
        f"All Time Fails: {totalFails}\n"
        f"All Time Clutches: {totalClutches}\n"
        f"All Time Wins: {totalWins}\n"
    )
    return statsString
