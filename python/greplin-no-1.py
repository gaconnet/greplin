# challenge.greplin.com

from collections import defaultdict

def palindrome(corpus):
    """Find the longest palindrome in the given `corpus`"""
    index = defaultdict(list)
    for i, c in enumerate(corpus):
        index[c].append(i)

    longest = ''

    for forward in xrange(len(corpus) / 2):
        for backward in reversed(index[corpus[forward]]):
            start, end = forward, backward
            while corpus[forward] == corpus[backward]:
                if backward - forward < 2:
                    candidate = corpus[start:end+1]
                    if len(candidate) > len(longest):
                        longest = candidate

                forward, backward = forward + 1, backward - 1

            forward = start

    return longest


if __name__ == '__main__':
    msg = "Ireallyreallyloveracecarsthatgoooosofast"  # short one for debug
    msg = "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

    longest = palindrome(msg)
    print longest
