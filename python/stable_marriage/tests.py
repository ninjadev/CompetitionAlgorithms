from stable_marriage import stable_marriage


def main():

    # test set from http://rosettacode.org/wiki/Stable_marriage_problem

    mens_preferences = [
        [0, 4, 2, 8, 9, 3, 5, 1, 7, 6],
        [2, 7, 0, 3, 4, 5, 1, 9, 8, 6],
        [7, 4, 0, 3, 1, 5, 8, 6, 2, 9],

        [8, 5, 3, 6, 7, 4, 9, 1, 2, 0],
        [9, 3, 1, 2, 5, 4, 0, 8, 7, 6],
        [1, 0, 3, 6, 4, 8, 2, 9, 7, 5],

        [6, 4, 8, 1, 2, 0, 3, 7, 9, 5],
        [0, 4, 7, 5, 8, 2, 9, 1, 6, 3],
        [7, 2, 3, 6, 1, 0, 5, 8, 9, 4],

        [0, 5, 9, 6, 4, 1, 3, 2, 8, 7],
    ]

    womens_preferences = [
        [1, 5, 9, 6, 8, 0, 3, 4, 2, 7],
        [1, 0, 2, 5, 6, 3, 8, 4, 9, 7],
        [5, 1, 4, 6, 7, 2, 8, 0, 3, 9],

        [5, 9, 2, 0, 8, 7, 6, 3, 1, 4],
        [9, 7, 5, 3, 0, 6, 2, 4, 8, 1],
        [1, 0, 4, 8, 9, 3, 5, 6, 2, 7],

        [9, 6, 7, 5, 1, 0, 2, 4, 3, 8],
        [6, 9, 1, 0, 8, 3, 7, 4, 2, 5],
        [8, 2, 7, 6, 5, 1, 0, 4, 9, 3],

        [4, 7, 6, 0, 1, 9, 2, 8, 5, 3],
    ]

    mens_partners, womens_partners = stable_marriage(
        mens_preferences, womens_preferences)

    print 'mens_partners', mens_partners
    print 'womens_partners', womens_partners

    for man, mans_preferences in enumerate(mens_preferences):
        for woman in mans_preferences:
            if woman == mens_partners[man]:
                break
            for rival_womans_man in womens_preferences[woman]:
                if rival_womans_man == womens_partners[woman]:
                    break
                if rival_womans_man == man:
                    print 'Error!'
                    print ('man', man, 'woman', woman,
                           'rival_womans_man', rival_womans_man)
                    return

    print 'test complete'

main()
