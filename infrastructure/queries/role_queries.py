class RoleQueries:

    INSERT = """
    INSERT INTO role (name, level)
    VALUES (%(name)s, %(level)s)
    RETURNING *;
    """

    SELECT_BY_ID = """
    SELECT * FROM role WHERE id = %(id)s;
    """

    SELECT_ALL = """
    SELECT * FROM role;
    """

    DELETE = """
    DELETE FROM role WHERE id = %(id)s;
    """
