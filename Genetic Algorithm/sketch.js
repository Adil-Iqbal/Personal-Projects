// "The Evolution of Code" by Adil Iqbal.

/* This is an attempt at the implementation of evolutionary principles described in Chapter 9 of the
"The Nature of Code" by Daniel Shiffman. You can find his book at "natureofcode.com".

This code also relies on two libraries that can be found here:
p5.js "https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.5.6/p5.js"
p5.dom.js "https://cdnjs.cloudflare.com/ajax/libs/p5.js/0.5.6/addons/p5.dom.js" */

var target = "To be or not be"; // The target statement to which all specimens are compared.
var popSize; // The raw number of specimens in the species.
var mpSize; // The percentage of specimens that get to breed.
var mutationRate; // The rate of mutation of any given DNA sequence.
var predationRate; // The propensity of the fittest specimens to dominate the mating pool.

var generation = 0; // Tracks the number of generations that have elapsed.
var population = []; // An array to contain all specimens in the species.
var matingPool = []; // An array to contain those specimens who can potentially procreate.
var parents = []; // The two parents chosen to procreate.

// Interface variables...
var popSizeSlider, mpSizeSlider, mutationRateSlider, predationRateSlider, nextGenButton, completionButton, cancelButton;
var doEvolution = false;
var cancelled = false;
var popSample = [];
var theFittest = {
    dna: "",
    matched: 0,
    fitness: 0
};


function setup() {
    createCanvas(660, 320);
    setupObjects();
    for (var i = 0; i < 15; i++) {
        popSample[i] = "";
    }
}

function draw() {
    background(255);
    showText();
    updateText();
}

function setupObjects() {
    popSizeSlider = createSlider(100, 2000, 300, 20);
    popSizeSlider.position(290, 142);
    popSizeSlider.style("width", "150px");

    mpSizeSlider = createSlider(0, 1, 1, 0.01);
    mpSizeSlider.position(290, 179);
    mpSizeSlider.style("width", "150px");

    mutationRateSlider = createSlider(0, 1, 0.02, 0.01);
    mutationRateSlider.position(290, 214);
    mutationRateSlider.style("width", "150px");

    predationRateSlider = createSlider(0, 1, 0.4, 0.01);
    predationRateSlider.position(290, 250);
    predationRateSlider.style("width", "150px");

    nextGenButton = createButton("Breed Next Generation");
    nextGenButton.position(40, 290);
    nextGenButton.mousePressed(createPopulation);

    completionButton = createButton("Breed to Completion");
    completionButton.position(200, 290);
    completionButton.mousePressed(completionBehavior);

    cancelButton = createButton("Cancel");
    cancelButton.position(345, 290);
    cancelButton.mousePressed(cancelBehavior);
    cancelButton.hide();
}

function showText() {
    textSize(28);
    textFont("Courier New");
    textStyle(BOLD);
    text(target, 30, 48);
    text(theFittest.dna, 30, 85);

    textSize(18);
    textFont("Verdana");
    textStyle(NORMAL);
    text("Generation: " + generation, 30, 120);
    text("Population Size: " + popSize, 30, 155);
    text("Mating Pool Ratio: " + (mpSize * 100) + "%", 30, 190);
    text("Mutation Rate: " + (mutationRate * 100) + "%", 30, 225)
    text("Predation Rate: " + (predationRate * 100) + "%", 30, 260)

    textSize(14);
    textFont("Courier New");
    textStyle(NORMAL);
    for (var i = 0; i < popSample.length; i++) {
        text(popSample[i], 475, (25 + (i * 20)));
    }
}

function updateText() {
    popSize = popSizeSlider.value();
    mpSize = mpSizeSlider.value();
    mutationRate = mutationRateSlider.value();
    predationRate = predationRateSlider.value();

    var index = 0;
    var maxMatched = 0;
    if (population.length != 0) {
        if (doEvolution) {
            for (var i = 0; i < popSample.length; i++) {
                popSample[i] = population[round(random(0, population.length - 1))].dna;
            }
            for (var i = 0; i < population.length; i++) {
                if (population[i].matched > maxMatched) {
                    maxMatched = population[i].matched;
                    index = i;
                }
            }
            theFittest = population[index];
            doEvolution = false;
        }
    } else {
        theFittest = {
            dna: "",
            matched: 0,
            fitness: 0
        };
        for (var i = 0; i < popSample.length; i++) {
            popSample[i] = "";
        }
    }
}


function completionBehavior() {
    hardReset();
    nextGenButton.hide();
    completionButton.hide();
    cancelButton.show();

    var completion = 0;
    while (completion < 1 && cancelled == false && generation < 500) {
        createPopulation();
        updateText();
        completion = theFittest.matched / target.length;
    }

    nextGenButton.show();
    completionButton.show();
    cancelButton.hide();
}

function cancelBehavior() {
    nextGenButton.show();
    completionButton.show();
    cancelButton.hide();
    hardReset();
    cancelled = true;
}

function hardReset() {
    generation = 0;
    population = [];
    matingPool = [];
    parents = [];
    doEvolution = false;
    cancelled = false;
    theFittest = {
        dna: "",
        matched: 0,
        fitness: 0
    };
    for (var i = 0; i < popSample.length; i++) {
        popSample[i] = "";
    }
}

function createPopulation() {
    generation++;
    doEvolution = true;
    // INITIALIZE: If no species exists, then generate one randomly.
    if (population.length == 0) {
        for (var i = 0; i < popSize; i++) {
            population[i] = {
                dna: "",
                matched: 0,
                fitness: 0
            };
            // Creates a member of the population.
            for (var j = 0; j < target.length; j++) {
                var nextGene = char(round(random(32, 126)));
                population[i].dna += nextGene;
            }
            evalMatched(population[i]);
        }
    }
    // SELECTION: If a species exists, breed it's fittest members.
    else {
        // Populate mating pool.
        for (var i = 0; i < round(population.length * mpSize); i++) {
            var nextBreeder = findBreeder();
            matingPool[i] = population[nextBreeder];
            population.splice(nextBreeder, 1);
        }

        // Begin populating the next generation.
        population = [];
        for (var i = 0; i < popSize; i++) {
            population[i] = {
                dna: "",
                matched: 0,
                fitness: 0
            };
            // HEREDITY: Select two parents from the mating pool.
            parents[0] = matingPool[round(random(0, matingPool.length - 1))];
            parents[1] = matingPool[round(random(0, matingPool.length - 1))];
            // Incest protection.
            while (parents[0].dna == parents[1].dna) {
                parents[0] = matingPool[round(random(0, matingPool.length - 1))];
                parents[1] = matingPool[round(random(0, matingPool.length - 1))];
            }

            var midpoint = round(random(target.length));
            for (var j = 0; j < target.length; j++) {
                var nextGene = "";
                // Crossover.
                if (j <= midpoint) {
                    nextGene = parents[0].dna.charAt(j);
                } else {
                    nextGene = parents[1].dna.charAt(j);
                }
                // MUTATION: Mutate single gene based on mutation rate.
                if (random(1) < mutationRate) {
                    nextGene = char(round(random(32, 126)));
                }
                population[i].dna += nextGene;
            }
            evalMatched(population[i]);
        }
    }
    // Evaluate and assign fitness to all specimens.
    for (var i = 0; i < population.length; i++) {
        population[i].fitness = population[i].matched / target.length;
    }
    // Reorders population array such that the fittest specimens get priority access to the mating pool.
    if (predationRate > random(1)) {
        population.sort(function(a, b) {
            return a.fitness - b.fitness;
        })
    } else {
        population = shuffle(population);
    }
}

// Matches the specimen against the target statement.
function evalMatched(specimen) {
    for (var j = 0; j < target.length; j++) {
        if (specimen.dna.charAt(j) == target.charAt(j)) {
            specimen.matched++;
        }
    }
}

/* Cycles through all specimens in the population and tests their fitness. Returns the array position of first specimen
to pass the test. If all specimens fail, returns position of specimen at random (regardless of fitness). */
function findBreeder() {
    var found = false;
    var index = null;
    for (var i = population.length - 1; i >= 0; i--) {
        if (found == false && population[i].fitness > random(1)) {
            index = i;
            found = true;
        };
    }
    if (index == null) {
        index = round(random(population.length - 1));
    }
    return index;
}
