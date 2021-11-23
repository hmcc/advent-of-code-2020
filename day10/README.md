# Day 1
This was the first day that made me think. Part 1 was fine, but I (and everyone else I've talked to) found part 2 more interesting.

I started off by solving the problem with depth-first search. Although this was fast enough on the sample, it was far too slow when I ran it against the full input.

I was aware that it could be speeded up with caching, but where's the fun in that?

I was also aware of [this solution](https://github.com/elvinyhlee/advent-of-code-2020-python/blob/master/day10.py#L25-L26), which is far more elegant, but I didn't want to copy-paste, I wanted to write my own.

The solution I came up with takes advantage of the fact that in my input data, the voltage differences were either 1, or 3 (there were no joltage differences of 2). Since this is also the case in the examples, and in anyone else's input data that I've seen, I suspect this is universal, but I obviously can't be sure.

Since any joltage differences of 3 don't increase the number of combinations (it must be connected to the adjacent adapter), we can break down the list of joltages into a series of blocks with a joltage difference of 1:

```
1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19] ->
[1], [4, 5, 6, 7], [10, 11, 12], [15, 16], [19]
```

Then, for each of these blocks, we can find out how many different ways they can be arranged:

```
[4, 5, 6, 7]
[4, 6, 7]
[4, 5, 7]
[4, 7]
= 4 ways
```

The number of arrangements can be predicted from the number of adapters according to a formula. So the solution is the number of arrangements for each block, multiplied together.