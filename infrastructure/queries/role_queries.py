class RoleQueries:

    INSERT = """INSERT INTO role (name, level) VALUES (%(name)s, %(level)s) RETURNING id, name, level;"""

    SELECT_BY_ID = """SELECT id, name, level FROM role WHERE id = %(id)s;"""

    SELECT_ALL = """SELECT id, name, level FROM role;"""

    DELETE = """DELETE FROM role WHERE id = %(id)s;"""
