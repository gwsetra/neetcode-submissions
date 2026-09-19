class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        print(people)
        lp = 0
        rp = len(people)-1
        trip = 0

        while lp <= rp:
            tmplimit = limit
            # if tmplimit - people[rp] >= 0:
            tmplimit -= people[rp]
            rp -= 1
            if tmplimit - people[lp] >= 0:
                lp += 1
            trip += 1

        return(trip)