from advent_of_code.utils import load_input, save_answers


INPUT = load_input(1)


def part1():
    return sum(map(lambda x: int(x) // 3 - 2, INPUT))


def part2():
    def func(x):
        x = int(x)
        total_fuel = x // 3 - 2
        extra_fuel = max(0, total_fuel // 3 - 2)

        while extra_fuel:
            total_fuel += extra_fuel
            extra_fuel = max(0, extra_fuel // 3 - 2)

        return total_fuel

    return sum(map(func, INPUT))


if __name__ == "__main__":
    answer1 = part1()
    answer2 = part2()
    print(f"Day 1 - Part 1 Answer: {answer1}")
    print(f"Day 1 - Part 2 Answer: {answer2}")
    save_answers(answer1, 1, 1)
    save_answers(answer2, 1, 2)