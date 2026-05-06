class DepartmentQueries:

    INSERT = f"""INSERT INTO department (name) VALUES (%(name)s) RETURNING id, name;"""

    SELECT_BY_ID = f"""SELECT id, name FROM department WHERE id = %(id)s;"""

    SELECT_ALL = f"""SELECT id, name FROM department;"""

    DELETE = """DELETE FROM department WHERE id = %(id)s; """

