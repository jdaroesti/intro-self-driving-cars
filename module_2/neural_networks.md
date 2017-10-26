level 1 (single pixel)
2 possibilities (fire or not) among a continum.
input [0, 1] (range from 0 to 1 with resolution (minimum jump from value to value))
i.e.
[0, 0.2, 0.4, 0.6, 0.8, 1] # range [0, 1] resolution 0.2

output true or false

level 2
4 inputs (booleans)
8 outputs

a) solid
0 0
0 0

b) solid
x x
x x

c) top horizontal line
x x
0 0

d) bottom horizontal line
0 0
x x

e) left vertical line
x 0
x 0

f) right vertical line
0 x
0 x

g) forward diagonal line
x 0
0 x

g) backward diagonal line
0 x
x 0

level 3 (neurons needed level^2(inputs)) (information encoding 2^level(outputs))
1
x 0 0
0 0 0
0 0 0
2
0 x 0
0 0 0
0 0 0
3
0 0 x
0 0 0
0 0 0
4
0 0 0
x 0 0
0 0 0
5
0 0 0
0 x 0
0 0 0
6
0 0 0
0 0 x
0 0 0
7
0 0 0
0 0 0
x 0 0
8
0 0 0
0 0 0
0 x 0
9
0 0 0
0 0 0
0 0 x
10
x x 0
0 0 0
0 0 0
11
0 x x
0 0 0
0 0 0
12
0 0 0
x x 0
0 0 0
13
0 0 0
0 x x
0 0 0
14
0 0 0
0 0 0
x x 0
15
0 0 0
0 0 0
0 x x
16
x 0 0
x 0 0
0 0 0
17
0 0 0
x 0 0
x 0 0
18
0 x 0
0 x 0
0 0 0
19
0 0 0
0 x 0
0 x 0
20
0 0 x
0 0 x
0 0 0
21
0 0 0
0 0 x
0 0 x
22
x 0 0
0 x 0
0 0 0
23
0 0 0
0 x 0
0 0 x
24
0 x 0
0 0 x
0 0 0
25
0 0 0
x 0 0
0 x 0
26
0 0 x
0 x 0
0 0 0
27
0 0 0
0 x 0
x 0 0
28
0 x 0
x 0 0
0 0 0
29
0 0 0
0 0 x
0 x 0
30
x x x
0 0 0
0 0 0
31
0 0 0
x x x
0 0 0
32
0 0 0
0 0 0
x x x
33
x 0 0
x 0 0
x 0 0
34
0 x 0
0 x 0
0 x 0
35
0 0 x
0 0 x
0 0 x
36
0 0 x
0 x 0
x 0 0
37
x 0 0
0 x 0
0 0 x
38
x x 0
x 0 0
0 0 0
39
0 0 0
x 0 0
x x 0
40
0 0 0
0 0 x
0 x x
41
0 x x
0 0 x
0 0 0
42
x 0 0
x x 0
0 0 0
43
0 0 0
x x 0
x 0 0
44
0 0 0
0 x 0
x x 0
45
0 0 0
0 x 0
0 x x
46
0 0 0
0 x x
0 0 x
47
0 0 x
0 x x
0 0 0
47
0 x x
0 x 0
0 0 0
48
x x 0
0 x 0
0 0 0
38
x x 0
x x 0
0 0 0
39
0 x x
0 x x
0 0 0
40
0 0 0
x x 0
x x 0
41
0 0 0
0 x x
0 x x
42
x x 0
x 0 0
x 0 0
43
x 0 0
x 0 0
x x 0
44
0 0 0
x 0 0
x x x
45
0 0 0
0 0 x
x x x
46
0 0 x
0 0 x
0 x x
47
0 x x
0 0 x
0 0 x
48
0 0 x
0 x 0
x x 0
49
0 0 x
x x 0
x 0 0
50
x 0 0
0 x x
0 0 x
51
x 0 0
0 x 0
0 x x
52
x x x
0 x 0
0 0 0
53
0 0 0
0 x 0
x x x
54
x 0 0
x x x
0 0 0
55
0 x 0
x x x
0 0 0
56
0 0 x
x x x
0 0 0
57
0 0 0
x x x
x 0 0
58
0 0 0
x x x
0 x 0
59
0 0 0
x x x
0 0 x
60
x x 0
0 x 0
0 x 0
61
0 x 0
x x 0
0 x 0
62
0 x 0
0 x 0
x x 0
63
0 x 0
0 x 0
0 x x
64
0 x 0
0 x x
0 x 0
65
0 x x
0 x 0
0 x 0
66
x 0 0
x x 0
x 0 0
67
0 0 x
0 x x
0 0 x


level 9 (81 neurons) (512 outputs combinations)
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

level 10 (100 neurons) (1024 outputs)
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

1, 2
2, 8
3, 16
