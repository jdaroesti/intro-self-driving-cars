# Lesson 1: Introduction

## 1.1 Intro

Thomas Bayes invented Bayes law to try to prove the existance of god. Bayes law allows for uncertantaty to be accounted in the field of robotics and to be modified when more information about the world becomes available. The mathematical tool to gather information is called Statistics.

## 1.2 Course overview

1. Joy Ride (project)
2. Probability
3. Conditional Probability
4. Programming Probability in Python
5. Bayes' Rule
6. Programming Bayes' Rule and World Representations
7. Robot Localization
8. Histogram Filter in Python (project)


# Lesson 2: Joy ride


# Lesson 3: Probability

## 3.1 Uncertainty in driving

Control noise is how uncertain we are that a self driving car control will behave the way we expect. That uncertainty is unavoidable in almost all components of a car. Managing this uncertainty is a pivotal part of making a self driving car that actually works.

*When a self driving car drives down the road, which of the following quantities is it ever possible for the car to know with certainty?*

- What other traffic will do in the future?
- Where it is?
- How fast is going?
- What will happen to its own motion when it turns the steering wheel?
- **None of the above**

Everything listed here is only "knowable" in a probabilistic sense. Luckily we don't need complete certainty to make a self driving car drive safely and efficiently. In fact, humans drive (reasonably) safely with imperfect knowledge all the time!

## 3.2 Uncertainty in robotics

Using the word certain the way we'll use it in this Nanodegree, nothing in the previous question is ever certain. Let me explain.

What other traffic will do: People are impossible to predict with certainty!

Where you are: It may seem like you know where you are when you drive, but you don't. At least not with complete certainty. You may know where you are with sufficient certainty, but if I asked you how many millimeters away from the center lane you were, you wouldn't know.

How fast you're going: The same reasoning applies to knowing your speed. You can get a good idea of how fast you're going by looking at your speedometer (which measures your speed), but these measurements are never perfect.

What will happen when you turn the wheel: A car is an imperfect mechanical system. If you turned the steering wheel by the same amount 100 times, the car would turn a slightly different amount every time.

As humans we solve these problems in a variety of ways. Number 2 and 3 we solve by saying "ehh, I actually don't need to know exactly where I am or how fast I'm going, I just need to know those quantities with a high degree of certainty. Number 4 we solve by using our brain as a high performance adaptive controller. And number 1... who knows how we handle number 1...? (just kidding, you'll learn more about this in the machine learning course at the end of this curriculum).

## 3.3 Learning objectives explained

Learning objectives will be presented at the beginning of each lesson as a preview of what kind of questions the student should be able to answer the end of each said lesson.

## 3.4 Learning objectives: Probability

## 3.5 Probability

Probability and statistics are two sides of the same coin. In statistics, we are given data and try to determine the causes for that data. In probability, we are given the the causes and try to predict the future data.

In other words, probability gives us the language to describe the relationship between data and the underlying causes. Probability is a method of describing the anticipated outcome of a data stream.

## 3.6 Flipping coins

## 3.7 Fair coin

In a fair coin:

P(heads) = 0.5
P(tails) = 0.5

```python

def probability(side):
  return {
    'heads': 0.5,
    'tails': 0.5,
  }[side]
```

## 3.8 Loaded coin

```python

def probability(side):
  return {
    'heads': 1,
    'tails': 0,
  }[side]
```

```python

def probability(side):
  return {
    'heads': 0.75,
    'tails': 0.25,
  }[side]
```

## 3.9 Complementary outcomes

P(A) = 1 - P(~A)

```python
import random

prob_b = random.random()
prob_a = 1 - prob_b
```

## 3.10 Probabilistic events in robotics

Probability is the core of how a self driving car runs.

A coin flip is a perfect example of a probabilistic event: a set of outcomes to some experiment where each outcome has a probability.

With a coin, the outcomes are clear: heads or tails, and the probabilities are simple: 0.5 and 0.5.

A self-driving car makes hundreds of calculations about probabilistic events every second, but the events are not as clean as a coin flip. For example:

- What is the probability that this sensor measurement is accurate to within 5 centimeters? What about 1 centimeter?
- What is the probability that some other vehicle will turn left at this intersection? Go straight? Turn right? What if they just sit there forever?
- The radar and lidar measurements seem to disagree! What's the probability that the range finder somehow became detached from the roof?

These examples are all much more interesting than "heads or tails?" but they are also less straightforward, which makes it much harder to learn probability theory from them.

## 3.11 Two flips

P(heads, heads) = P(heads) * P(heads)
P(heads, heads) = 0.5 * 0.5
P(heads, heads) = 0.25

```python
from fractions import fraction

probability_heads = Fraction(1, 2)

probability_two_heads = probability_heads * probability_heads
# 1/4
```

With loaded coin P(heads) = 0.6

```python

probability_heads = Fraction(3, 5)
probability_tails = Fraction(2, 5)

probability_heads_tails = probability_heads * probability_tails
```

## 3.12 Two cars

Roboticists will often use the term state space to describe the set of all possible outcomes for a probabilistic event.

For a coin the state space for a "flip" event can be written mathematically as:

`{H,T}`

And for a car at an intersection the state space for a "turn" event can be written mathematically as:

`{L,S,R}`

Coins and cars may seem differently, but we can treat them in similar ways when we think in terms of events and state spaces.

In the last question you saw that calculating a truth table for 2 coin flips requires 4 calculations while calculating the truth table for 2 car turns at an intersection requires 9 calculations.

We can make these statements more broadly applicable:

1. When calculating the truth table for 2 events which each have a state space size of 2, we need to make 4 calculations.
2. When calculating the truth table for 2 events which each have a state space size of 3, we need to make 9 calculations.

And in fact, there's a mathematical pattern here that can be expressed algebraically:

When calculating the truth table for N events which each have a state space size of x, we need to make x^N calculations x^N gets very big very fast as x or N get bigger.

You will see later this Nanodegree how this exponential complexity growth can really slow down the performance of the code running inside of a self driving car.

```python
import itertools

possibilities = ['l', 's', 'r']
events = 2 # two events, i.e "l, l"

state_space = itertools.product(possibilities, repeat=events)
# [('l', 'l'), ('l', 's'), ('l', 'r'), ('s', 'l'), ('s', 's'), ('s', 'r'), ('r', 'l'), ('r', 's'), ('r', 'r')]

len(state_space) # 9
```
### Probabilities cheatsheet
product = independent events
permutations = dependent events, order matters
combinations = dependent events, order does not matter

multiply probabilities = and
add probabilities = or

## 3.13 One head

What is the probability of only one head in two coin flips?

```python
import itertools

state_space = [coin_flip for coin_flip in itertools.product(['h', 't'], repeat=2)] # [('h', 'h'), ('h', 't'), ('t', 'h'), ('t', 't')]

result = [r for r in filter(lambda coin_flip: coin_flip.count('h') == 1, state_space)] # [('h', 't'), ('t', 'h')]

probability = len(result) / len(state_space) # 0.5
```

## 3.14 One of three

What is the probability of only one head in three coin flips?

```python
import itertools

state_space = [coin_flip for coin_flip in itertools.product(['h', 't'], repeat=3)]
# [('h', 'h', 'h'), ('h', 'h', 't'), ('h', 't', 'h'), ('h', 't', 't'), ('t', 'h', 'h'), ('t', 'h','t'), ('t', 't', 'h'), ('t', 't', 't')]

result = [r for r in filter(lambda coin_flip: coin_flip.count('h') == 1, state_space)]
# [('h', 't', 't'), ('t', 'h', 't'), ('t', 't', 'h')]

probability = len(result) / len(state_space) # 0.375
```

With a loaded coin, the probabilities change. For example, P(head) = 0.6

```python
import functools

loaded_flips = [map(lambda el: 0.6 if el == 'h' else 0.4, flip) for flip in results]
flips_probabilities = [functools.reduce(lambda x, y: x * y, flip) for flip in loaded_flips]

final_probability = sum(flips_probabilities)
```

## 3.15 Even roll

P(ANY_NUMBER) = 1 / 6
P(EVEN_DIE) = 0.5

## 3.16 Doubles

What is the probability of a double with two dice?

```python
import itertools

state_space = [dice_throw for dice_throw in itertools.product(range(1, 7), repeat=2)]
doubles = [double for double in filter(lambda dice_throw: dice_throw[0] == dice_throw[1], state_space)]

probability = len(doubles) / len(state_space)
```

## 3.17 Summary

We learned about probability in this lesson. We learned that P(A) = 1 - P(B).
Coin flips and dice throws are examples of independent events.


# Lesson 4: Conditional probability
