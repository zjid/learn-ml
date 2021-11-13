## How does the machine learn?

So far I know, the machine needs these minimum requirements:
- ability to do mathematical operations
- procedure to update parameters itself
- resources to store and run multiple operation unit
- data input and feedback

### Pseudo-

Machines nowadays can do sophisticated mathematical operations in a short time.
The signals are smooth enough given floating points handling and a few bits for depth.
The calculations feel limitless, almost no overflow.
Although they seem natural for me, do they for machines themselves?

I have experience as a kid for years. (I am qualified as a human being.)
Back then, twelve times twelve equal(ed) to one hundred and four.
The answer felt right and intuitive, element-wise.
Using different notations, the answer **may** be true.
(For you who don't know, the real answer is 144.0 and the complex answer is 144.0 + j0.0.)
To get the right answer, my teacher taught me something like

``[10, 2] * [10, 2]T + [10, 2] * [2, 10]T = 104 + 40 = 144``.

Or ``sum of convolution( [10, 2], [10, 2] ) = sum of [4, 40, 100] = 144``.

(Put the answer on the left side and I'll get the left answer.)
Not really.
My teacher gave me an example by drawing columns and rows of circles and counting them.
My teacher sliced the columns and rows to show the process.

(I skip the understanding of multiplications, additions, etc.)

So,
I guess, the smallest unit of the machine (the neuron) not necessarily perform maths.
Can a machine with learning ability be built purely from comparator neurons?
Can maths emerge from a few comparators?
(Well, binary system is the result from comparators.
And I wrote this blablabla in a machine called digital computer.
Is TPU something like this?)
Hey, Captain!
