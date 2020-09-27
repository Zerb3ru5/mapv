import click
from click_shell import make_click_shell
from click_shell import shell

# project specific imports
from mapv.computations.simulation import Simulation


# the function that return the correct prompt
def print_promt(ctx):
    return ctx.txt


# my startup function for a simulation
@shell(prompt=print_promt, intro='Starting...')
@click.argument('name')
@click.pass_context
def simulator(ctx, name):
    ctx.txt = name + ' > '

    # load the simulation data
    ctx.simulation = Simulation()


@simulator.command()
def start():
    '''
    This command starts a simulation with the parameters defined in the simulations settings.
    '''
    click.echo('simulation started')


if __name__ == '__main__':
    simulator()