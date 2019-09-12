"""Utiliy functions"""
import click


def prompt_float(label, unit, default=None):
    return click.prompt(
        "{} ({})".format(label, unit),
        type=float,
        default=default,
    )


def prompt_choice(label, choices):
    choices_type = type(choices[0])
    choices_str = [str(item) for item in choices]
    result = click.prompt(
        label,
        type=click.Choice(choices_str)
    )
    return choices_type(result)

