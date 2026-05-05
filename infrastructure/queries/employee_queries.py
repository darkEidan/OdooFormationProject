class EmployeeQueries:

    INSERT = """
    INSERT INTO employee (name, email, hire_date, status, department_id, role_id)
    VALUES (%(name)s, %(email)s, %(hire_date)s, %(status)s, %(department_id)s, %(role_id)s)
    RETURNING *;
    """

    SELECT_BY_ID = """
    SELECT * FROM employee WHERE id = %(id)s;
    """

    SELECT_BY_EMAIL = """
    SELECT * FROM employee WHERE email = %(email)s;
    """

    SELECT_ALL = """
    SELECT * FROM employee;
    """
