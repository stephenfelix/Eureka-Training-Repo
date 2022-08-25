"""
Hello
"""

class Solution:
    """
    Hi
    """
    def __init__(self):
        pass

    def alice_or_bob(self, alice, bob, r_piles):
        """
        Hey
        """
        if len(r_piles) == 1:
            return alice, bob+r_piles[0]

        if len(r_piles)%2==0:
            alice_1, bob_1 = self.alice_or_bob(alice, bob, r_piles[1:])
            alice_1 += r_piles[0]
            alice_2 , bob_2 = self.alice_or_bob( alice, bob, r_piles[:-1])
            alice_2 += r_piles[-1]
            print(r_piles)
            if alice_1 > alice_2:
                print(alice_1, bob_1)
                return alice_1, bob_1
            print(alice_2, bob_2)
            return alice_2, bob_2

        alice_1, bob_1 = self.alice_or_bob( alice, bob, r_piles[1:])
        bob_1 += r_piles[0]
        alice_2 , bob_2 = self.alice_or_bob( alice, bob, r_piles[:-1])
        bob_2 += r_piles[-1]
        print(r_piles)
        if bob_1 > bob_2:
            print(alice_1, bob_1)
            return alice_1, bob_1
        print(alice_2, bob_2)
        return alice_2, bob_2


    def stone_game(self, r_piles: list[int]) -> bool:
        """
        Hi again
        """
        alice, bob = self.alice_or_bob(0, 0 , r_piles)
        print(alice, bob)
        return alice>bob

if __name__ == '__main__':
    piles = [1, 2, 1, 1]

    soln = Solution()
    print(soln.stone_game(piles))
