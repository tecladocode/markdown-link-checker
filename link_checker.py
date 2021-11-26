import sys
from pathlib import Path
import markdown
from bs4 import BeautifulSoup
import requests
from rich.console import Console
from rich.table import Table
import click
from concurrent.futures import ThreadPoolExecutor

try:
    file = Path(sys.argv[1])
except IndexError:
    file = Path("./MARKDOWN_TEST.md")

console = Console()


@click.command()
@click.argument("input", type=click.File("r"))
def check_file_links(input: file):
    html = markdown.markdown(input.read())
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a")
    hrefs = [link.attrs["href"] for link in links]
    valid = []
    invalid = []
    with ThreadPoolExecutor() as executor:
        for link, result in zip(links, executor.map(handle_link, hrefs)):
            if result[0]:
                valid.append(link)
            else:
                invalid.append((link, result[1]))

    valid_links, invalid_links = construct_link_tables(valid, invalid)
    console.print(invalid_links)
    console.print(valid_links)


def handle_link(href):
    try:
        resp = requests.get(href)
        if str(resp.status_code).startswith("2") or str(resp.status_code).startswith(
            "3"
        ):
            return True, "Valid link"
        return False, "Invalid link for unknown reason"
    except Exception as e:
        return False, str(e.args[0])


def construct_link_tables(valid, invalid):
    invalid_table = Table(
        "link", "reason", title="Invalid links in document", show_lines=True
    )
    for link, reason in invalid:
        invalid_table.add_row(link.attrs["href"], reason)

    valid_table = Table("text", "link", title="Valid links in document")
    for link in valid:
        valid_table.add_row(link.text, link.attrs["href"])

    return valid_table, invalid_table


if __name__ == "__main__":
    check_file_links()
