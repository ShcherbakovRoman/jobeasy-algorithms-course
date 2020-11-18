'''

'''

def fight_resolve(defender, attacker):
    player1 = ['K', 'A', 'S', 'P']
    player2 = ['k', 'a', 's', 'p']
    if defender in player1 and attacker in player1:
        return -1
    elif defender in player2 and attacker in player2:
        return -1
    else:
        if defender in player1:
            if defender == 'K' and attacker == 'a':
                return defender
            elif defender == 'A' and attacker == 's':
                return defender
            elif defender == 'S' and attacker == 'p':
                return defender
            elif defender == 'P' and attacker == 'k':
                return defender
            else:
                return attacker
        else:
            if defender == 'k' and attacker == 'A':
                return defender
            elif defender == 'a' and attacker == 'S':
                return defender
            elif defender == 's' and attacker == 'P':
                return defender
            elif defender == 'p' and attacker == 'K':
                return defender
            else:
                return attacker

'''
@test.describe("Boardgame Fight Resolve")
def fixed_tests():

    @test.it("Friendly Fire")
    def friendly_tests():
        test.assert_equals(fight_resolve('K', 'A'), -1)
        test.assert_equals(fight_resolve('S', 'A'), -1)
        test.assert_equals(fight_resolve('k', 's'), -1)
        test.assert_equals(fight_resolve('a', 'a'), -1)

    @test.it("Fight Resolve Test")
    def edge_case_tests():
        test.assert_equals(fight_resolve('k', 'A'), 'k')
        test.assert_equals(fight_resolve('K', 'a'), 'K')
'''