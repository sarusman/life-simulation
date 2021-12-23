# Conway's Game of Life

The game of the life in Python.

The game of life is a cellular automaton whose rules were defined by J. Conway in 1970. The state of the automaton at stage n is only a function of its state at stage n - 1. The evolution of the state of a cell depends on the state of its 8 closest neighbors.
In the Conway automaton, the rules are as follows:
* An empty cell in step n - 1 and having exactly 3 neighbors will be occupied in the next step. (birth linked to an optimal environment)
* A cell occupied in step n - 1 and having 2 or 3 neighbors will be maintained in step n otherwise it is emptied. (destruction by desertification or overpopulation)
It is the analogy between these rules and certain criteria for the evolution of populations of bacteria that has led to this automaton being given the name of life.


![Capture d’écran 2021-12-12 à 00 46 17](https://user-images.githubusercontent.com/60844500/145695176-448a665b-7228-4dbc-aae7-c9babc7db9f7.png)

![Capture d’écran 2021-12-12 à 00 46 39](https://user-images.githubusercontent.com/60844500/145695177-26294d33-002d-41ff-9022-b76c560afc47.png)
