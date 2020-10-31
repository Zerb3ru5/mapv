import click
import os
from mapv.computations.simulation import Simulation
import matplotlib.pyplot as plt

@click.group()
def main():
    pass

# run a simulation 
@main.command()
@click.argument('name')
def sim(name):
    print('hello, ', name)
    os.system(f'python C:/Users/Nutzer/Desktop/Private/Programming/Projects/mapv/mapv/simulator.py {name}')


@main.command()
def start():
    sim = Simulation('Karen')
    sim.simulate()


if __name__=="__main__":
    main()