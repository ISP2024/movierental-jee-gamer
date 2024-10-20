## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

2.1 Middle Man <br>
2.2 Single Responsibility Principle suggest this refactoring because movie is doing too much. It should only know about the movie but it also know about the rental price and points.

5.2 I have tried putting it in the movie because maybe the movie should know it's own price code so
I that I can just call the method by the movie itself without having to use paramter
but I'd have to import the price again and that would be hard to change so it's not a good idea.
<br>
High cohesion: Instead I choose a class that is already closely related with the price strategy which is rental. I put the method as the class method without having to modify anything.
<br>
Single Responsibility Principle: Since rental class has the priceStrategy and is already managing the price for movie, deciding price for a movie should fit right in for its responsibility.
<br>
Since the strategy can be decided in rental class without having to be assigned beforehand, just remove the strategy from the input and let the rental class decide for itself.

