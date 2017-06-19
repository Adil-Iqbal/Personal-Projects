# Evolution of Code

**Summary:** This program uses a genetic algorithm which attempts to reproduce a target phrase starting from a population of strings that have a random series characters.

**Acknowledgement** - This is an attempt at the implementation of evolutionary principles described in Chapter 9 of the "The Nature of Code" by Daniel Shiffman. You can find his book at [*natureofcode.com*](http://natureofcode.com/).

### To see the program, [**right-click here and open a new tab.**](https://jsfiddle.net/qrx5kno1/)

**Instructions:**
* You can click the "Breed Next Generation" button to proceed one generation at a time (Recommended).
* You can also click the "Breed to Completion" button to breed on a loop until either the target phrase is reproduced or a maximum generation limit is reached.
* Feel free to play around with the sliders to see how it affects the evolutionary process.
* You can also hit the "Run" button in the top-left corner of the screen to reload the program.  

**Evolutionary Features (found in sketch.js):**
* **Starts Randomly** - When generating the members of the first population, all characters are chosen randomly (line 193)
* **Fitness Score** - The fitness score is determined by counting the number of characters in the member that match the corresponding characters in the target phrase (line 264). We than divide the number of matched characters by the total number of characters in the phrase (line 248).
* **Natural Selection** - Members who breed are chosen by the 'findBreeder' function (line 205). The 'findBreeder' function tests the fitness of each member and the first member to pass is chosen to breed (line 276). Members with a higher fitness score are more likely to pass. The breeders are all added to the mating pool for later use (line 206 & 207).
* **Heredity and Crossover** - Two breeders are chosen at random from the mating pool (lines 220 & 221). Their genes (or characters) are than spliced together at a randomly chosen midpoint (lines 228 to 236).
* **Mutation** - Before the offspring is added to the next generation (line 241), each of its genes (or characters) has a chance to mutate based on the mutation rate (lines 238 & 234).
* **Predation** - Predation is simulated by sorting the population array based on fitness (lines 253 & 254).

### Copyright 2017 by **Adil Iqbal**. All rights reserved.
