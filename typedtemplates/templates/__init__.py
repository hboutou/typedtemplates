from collections.abc import Iterable
from importlib import resources


def get_items(*, ids: Iterable[int], names: Iterable[str], schema: str = 'public'):
    tmpl = resources.files(__package__).joinpath('get_items.sql').read_text()
    sql = tmpl.format(
        schema=schema,
        ids=','.join([str(x) for x in ids]),
        names=','.join([f"'{x}'" for x in names]),
    )
    return sql

