def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def count(start, end):
        if (start > end):
            print("Harvest time!")
            return
        print(f"Day {start}")
        count(start + 1, end)

    count(1, days)
