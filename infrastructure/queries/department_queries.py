class DepartmentQueries:

    INSERT = """
    INSERT INTO department (name)
    VALUES (%(name)s)
    RETURNING *;
    """

    SELECT_BY_ID = """
    SELECT * FROM department WHERE id = %(id)s;
    """

    SELECT_ALL = """
    SELECT * FROM department;
    """

    DELETE = """
    DELETE FROM department WHERE id = %(id)s;
    """
