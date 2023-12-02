#!/usr/bin/env nix-shell
#! nix-shell -i python3 -p python3Packages.requests -p python3Packages.typer -p python3Packages.rich

from contextlib import contextmanager
import pathlib
import requests
import typer
app = typer.Typer()

THIS_DIR = (pathlib.Path(__file__).parents[0])
DEFAULT_COOKIE_PATH = (THIS_DIR / ".." / "cookie")
DEFAULT_INPUTS_PATH = (THIS_DIR / ".." / "inputs")
DEFAULT_CODE_PATH = (THIS_DIR / ".." / "code")

@contextmanager
def get_session(cookie_path: pathlib.Path):
    try:
        s = requests.session()
        cookies = requests.utils.cookiejar_from_dict({"session": "".join(x.strip() for x in cookie_path.open('r').readlines())})
        s.cookies.update(cookies)
        yield s
    finally:
        s.close()

@app.command()
def check_cookie(cookie_path: pathlib.Path = DEFAULT_COOKIE_PATH):
    with get_session(cookie_path) as session:
        response = session.get("https://adventofcode.com/2023/day/1/input")
        if len([x.strip() for x in response.text.split("\n")]) > 10:
            typer.echo("Cookie Loaded successfully! Good luck! :)")
        else:
            typer.echo("Cookie did not work. Out of date or wrong to begin with.")
            typer.echo("To get your cookie:")
            typer.echo("\t 1. Login with browser.")
            typer.echo("\t 2. Go to dev tools, look for session=<string>")
            typer.echo(f"\t 3. Save <string> to {cookie_path} with no suffix or prefix")

@app.command()
def grab_input(day: int, cookie_path: pathlib.Path = DEFAULT_COOKIE_PATH, output_root: pathlib.Path = DEFAULT_INPUTS_PATH):
    output_file_path = (output_root / f"day{day}.txt")
    with output_file_path.open("w") as f:
        with get_session(cookie_path) as session:
            response = session.get(f"https://adventofcode.com/2023/day/{day}/input")
            f.write(response.text)
            typer.echo(f"Successfully wrote {output_file_path}, good luck!")

if __name__ == '__main__':
    app()
