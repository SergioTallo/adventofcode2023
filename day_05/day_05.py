import os
from functools import reduce
from adventofcodeutils import measure_time
from aoc_challenge import AocChallenge


class NewAocChallenge(AocChallenge):
    def test(self, inputfile='test1.txt'):
        print("\n############## Tests ##############\n")
        print(f"Testing star one, day {self.day}...")
        assert self.function(1, inputfile) == self.value_1, \
            f"Star one failed, should be {self.value_1} but is {self.function(1, self.test_file1)}"
        print("Test 1 passed")
        print(f"Testing star two, day {self.day}...")
        assert self.function(2, inputfile) == self.value_2, \
            f"Star two failed, should be {self.value_2} but is {self.function(2, self.test_file2)}"
        print("Test 2 passed")

    def challenge(self, inputfile='input_day5.txt'):
        print("\n############## Challenge ##############\n")
        print(f"Score 1: {self.function(1, inputfile)}")
        print(f"Score 2: {self.function(2, inputfile)}")


def correspond(val, maps):
    _, *maps = maps.split('\n')
    for instruction in maps:
        dst, src, dist = map(int, instruction.split())
        steps = dst - src
        if src <= val < src + dist:
            return val + steps
    return val


@measure_time
def stars(starnumber: int, inputfile: str):
    seeds, *maps = open(inputfile).read().split('\n\n')
    if starnumber == 1:
        return min(reduce(correspond, maps, int(seed)) for seed in seeds.split()[1:])
    elif starnumber == 2:
        pairs = [(int(seeds.split()[1:][i]), int(seeds.split()[1:][i]) + int(seeds.split()[1:][i + 1])) for i in
                 range(0, len(seeds.split()[1:]), 2) if i + 1 < len(seeds.split()[1:])]

        for instruction in maps:
            _, *map_ = instruction.split('\n')
            new_pairs = []
            while pairs:
                pair = pairs.pop()
                append = True
                for inst in map_:
                    left = int(inst.split()[1])
                    right = int(inst.split()[1]) + int(inst.split()[2])
                    steps = int(inst.split()[0]) - left

                    if left <= pair[0] and pair[1] <= right:
                        new_pairs.append((pair[0] + steps, pair[1] + steps))
                        append = False
                        break
                    elif pair[0] < left < pair[1] <= right:
                        new_pairs.append((left + steps, pair[1] + steps))
                        pairs.append((pair[0], left))
                        append = False
                        break
                    elif left < pair[0] < right <= pair[1]:
                        new_pairs.append((pair[0] + steps, right + steps))
                        pairs.append((right, pair[1]))
                        append = False
                        break
                    elif pair[0] < left and pair[1] > right:
                        new_pairs.append((left + steps, right + steps))
                        pairs.append((pair[0], left))
                        pairs.append((right, pair[1]))
                        append = False
                        break
                if append:
                    new_pairs.append(pair)

            pairs = new_pairs.copy()
            new_pairs.clear()

        return min(pair[0] for pair in pairs)


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    NewAocChallenge(day, 2023, 35, 46, stars)


if __name__ == "__main__":
    main()
