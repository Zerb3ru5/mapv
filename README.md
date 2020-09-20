# The mapv physics simulation engine

Mapv is a cli based physics simulation engine with a graphical visualization tool for it's output.

## Overall structure

## Commands

The mapv cli can be divided into different categories, the ones that are globally available to manage overall functionality and the ones that can only be used in specific shell environments. 

The globally available ones can be adressed from the commandline with the keyword `mapv` and are:
- `sim` : open the simulator shell environment and run the simulation 
- `config` : according to the type of the argument, open a shell environment to modify a simulation or model with a visual representation of more complicated structures and connections
- `create` : opens the creator environment, designed to optimise the creation of simulations and models; it is a modified version of the config environment
- `delete` : to delete a simulations
