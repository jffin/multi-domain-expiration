#!/usr/bin/env python
import argparse
import logging
import pathlib
from time import time
from typing import NamedTuple

from utils.file_module import FileModule
from utils.whois_wrapper import WhoisWrapper


class RunConfig(NamedTuple):
    """
    Run config to define arguments to.
    """
    input: str = 'input.txt'
    output: str = 'results.json'


def define_config_from_cmd(parsed_args: 'argparse.Namespace') -> RunConfig:
    """
    Parsing config from args
    :param parsed_args: argparse.Namespace
    :return: RunConfig
    """
    return RunConfig(
        input=parsed_args.input,
        output=parsed_args.output,
    )


def cli() -> argparse.Namespace:
    """
    here we define args to run the script with
    :return: argparse.Namespace
    """
    parser = argparse.ArgumentParser(description='Domains Expiration')

    # Add the arguments to the parser
    parser.add_argument(
        '-i', '--input', required=True, help='File to read targets from', default='input.txt', type=pathlib.Path)
    parser.add_argument(
        '-o', '--output', required=True, help='File to save result in', default='result.json', type=pathlib.Path)

    return parser.parse_args()


def main() -> None:
    """
    Entrypoint into the application.
    :return: None
    """
    parsed_args: argparse.Namespace = cli()
    run_config: RunConfig = define_config_from_cmd(parsed_args=parsed_args)

    file_module: FileModule = FileModule(input_file_name=run_config.input, result_file_name=run_config.output)
    results: list[dict[str, str]] = WhoisWrapper.get_results(targets=file_module.read_input_file())

    file_module.write_result_file(results=results)


if __name__ == '__main__':
    try:
        start_time = time()
        main()
        logging.log(logging.DEBUG, f'Time consumption: {time() - start_time: 0.3f}s')
    except Exception as error:
        logging.exception(f'Failed with: {error}')
