import os
from functools import reduce
from adventofcodeutils import AocChallenge as OriginalAOCChallenge, measure_time


class NewAocChallenge(OriginalAOCChallenge):
    def test(self, inputfile='test.txt'):
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


def correspond_2(val, maps):
    new_val = val
    for instruction in reversed(maps):
        _, *map_ = instruction.split('\n')
        for inst in map_:
            left = int(inst.split()[1])
            right = int(inst.split()[1]) + int(inst.split()[2])
            steps = int(inst.split()[0]) - left
            if (val - steps) in range(left, right):
                new_val = val - steps
                break
        val = new_val
    return new_val


@measure_time
def stars(starnumber: int, inputfile: str):
    seeds, *maps = open(inputfile).read().split('\n\n')
    if starnumber == 1:
        return min(reduce(correspond, maps, int(seed)) for seed in seeds.split()[1:])
    elif starnumber == 2:
        seed = 1
        pairs = [(seeds.split()[1:][i], seeds.split()[1:][i + 1]) for i in range(0, len(seeds.split()[1:]), 2) if
                 i + 1 < len(seeds.split()[1:])]
        while True:
            value = correspond_2(seed, maps)
            for pair in pairs:
                if value in range(int(pair[0]), int(pair[0]) + int(pair[1])):
                    return seed
            seed += 1
            if seed % 10000 == 0:
                print(seed)


def main():
    day = int(os.path.basename(__file__).split('_')[1].split('.')[0])
    NewAocChallenge(day, 2023, 35, 46, stars)


if __name__ == "__main__":
    main()
