import click


@click.group()
def main():
    print('main')

@main.command()
def hello():
    print('hello')

if __name__=="__main__":
    main()