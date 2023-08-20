from functools import lru_cache
from typing import List

from redis_om.connections import get_redis_connection


@lru_cache(maxsize=None)
def check_for_command(conn, cmd):
    cmd_info = conn.execute_command("command", "info", cmd)
    return None not in cmd_info


@lru_cache(maxsize=None)
def has_redis_json(conn=None):
    if conn is None:
        conn = get_redis_connection()
    command_exists = check_for_command(conn, "json.set")
    return command_exists


@lru_cache(maxsize=None)
def has_redisearch(conn=None):
    if conn is None:
        conn = get_redis_connection()
    if has_redis_json(conn):
        return True
    command_exists = check_for_command(conn, "ft.search")
    return command_exists
