#!/usr/bin/python

import click

from calculators import get_calculator

@click.command()
@click.argument('calculator')
def main(calculator):
    calc = get_calculator(calculator)

    if calc is None:
        click.echo("Calculator `{}' not found.".format)
        return

    calc.start()
        


if __name__ == '__main__':
    main()
