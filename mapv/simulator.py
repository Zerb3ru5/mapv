from click_shell import shell


# @click.group()  # no longer
@shell(prompt='my-app > ', intro='Starting my app...')
def my_app():
    pass

@my_app.command()
def testcommand():
    print('testcommand is running')

if __name__=="__main__":
    my_app()
