#!/usr/bin/python -tt

####
# Textsträngar

# Given ett antal bananer, skriv en funktion som returnerar en textsträng med
# formen "Apan har <count> bananer", där "<count>" är värdet av den givna
# variabeln "count". Om antalet är 10 eller fler så ska textsträngen "Apan har
# många bananer" returneras istället.
def bananas(count):
    if count < 10:
        return('Apan har '+str(count)+' bananer')
    else:
        return('Apan har många bananer')


# Given en textsträng, skriv en funktion returnerar de två första och två sista
# tecknen i ursprungssträngen. Om strängen är kortare än 2 tecken returnera istället
# en tom sträng.
def both_ends(s):
    if len(s) > 2:
        return(s[0] + s[1] + s[-2] + s[-1])
    else:
        return('')


####
# Listor

# Given en lista med strängar, returnera antalet strängar som är längre än 2 tecken.
def match_lengths(words):
    strAn = 0
    for i in range(len(words)):
        if len(words[i]) > 2:
            strAn = strAn + 1
    return strAn

####
# Följande kod används för att testa dina lösningar för att se
# om dina lösningar på ovanstående problem är korrekta eller inte.

def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))

def main():
    print("bananas")
    test(bananas(2), "Apan har 2 bananer")
    test(bananas(4), "Apan har 4 bananer")
    test(bananas(10), "Apan har många bananer")
    test(bananas(99), "Apan har många bananer")
    print("")
    print("both_ends")
    test(both_ends("Hello, World"), "Held")
    test(both_ends("Hello"), "Helo")
    test(both_ends("a"), "")
    test(both_ends("xyz"), "xyyz")
    print("")
    print("match_lengths")
    test(match_lengths(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_lengths(['', 'x', 'xy', 'xyx', 'xx']), 1)

if __name__ == '__main__':
  main()
