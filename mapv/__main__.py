import click
import os

@click.group()
def main():
    pass


# run a simulation 
@main.command()
@click.argument('name')
def sim(name):
    print('hello, ', name)
    os.system(f'python C:/Users/Nutzer/Desktop/Private/Programming/Projects/mapv/mapv/simulator.py {name}')


if __name__=="__main__":
    main()