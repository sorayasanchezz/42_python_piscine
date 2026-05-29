def achievement_analytics(alice: set, bob: set, charlie: set) -> None:
    print("\n=== Achievement Analytics ===")

    # all achievements
    total = alice.union(bob).union(charlie)
    print("All unique achievements:", total)
    print("Total unique achievements:", len(total))

    # find the coommon achievements of players
    common = alice.intersection(bob).intersection(charlie)
    print("\nCommon to all players:", common)

    # find the unique achievements
    shared = alice.intersection(bob).union(
        bob.intersection(charlie).union(
            charlie.intersection(alice)))
    rare = total.difference(shared)
    print("Rare achievements (1 player):", rare)

    # alice vs bob
    print("\nAlice vs Bob common", alice.intersection(bob))
    print("Alice unique:", alice.difference(bob))
    print("Bob unique:", bob.difference(alice))


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")

    # handle sets used to store achevements (without duplicates)
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}

    print("Player alice achievements:", alice)
    print("Player bob achievements", bob)
    print("Player charlie achievements", charlie)

    achievement_analytics(alice, bob, charlie)
