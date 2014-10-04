# -*- coding: utf-8 -*-

"""
function stable_marriage {
    Initialize all m ∈ M and w ∈ W to free
    while ∃ free man m who still has a woman w to propose to {
       w = m's highest ranked woman to whom he has not yet proposed
       if w is free
         (m, w) become engaged
       else some pair (m', w) already exists
         if w prefers m to m'
           (m, w) become engaged
           m' becomes free
         else
           (m', w) remain engaged
    }
}
"""


def stable_marriage(mens_preferences, womens_preferences):
    # a mans preferences are reversed to avoid a pop(0)
    mens_preferences = [deepcopy[::-1] for deepcopy in mens_preferences]
    womens_preferences = [deepcopy[:] for deepcopy in womens_preferences]
    number_of_men = len(mens_preferences)
    number_of_women = len(womens_preferences)

    FREE = -1
    men = [FREE] * number_of_men
    women = [FREE] * number_of_women

    instable = True

    while instable:
        instable = False
        for man, man_engaged_to in enumerate(men):
            if man_engaged_to == FREE and len(mens_preferences[man]) > 0:
                instable = True
                candidate_woman = mens_preferences[man].pop()
                if women[candidate_woman] == FREE:
                    women[candidate_woman] = man
                    men[man] = candidate_woman
                else:
                    rival_man = women[candidate_woman]
                    for preferred_man in womens_preferences[candidate_woman]:
                        if preferred_man == man:
                            women[candidate_woman] = man
                            men[man] = candidate_woman
                            men[rival_man] = FREE
                            break
                        elif preferred_man == rival_man:
                            break
    return men, women
