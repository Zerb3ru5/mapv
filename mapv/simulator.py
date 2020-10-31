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
    ctx.obj = Simulation('Karen')


@simulator.command()
@click.pass_obj
def start(simulation):
    '''
    This command starts a simulation with the parameters defined in the simulations settings.
    '''
    simulation.simulate()
    click.echo('simulation started')


if __name__ == '__main__':
    simulator()