class EmployeeQueries:

    INSERT = f"""
    INSERT INTO employee (name, email, hire_date, status, department_id, role_id)
    VALUES (%(name)s, %(email)s, %(hire_date)s, %(status)s, %(department_id)s, %(role_id)s)
    RETURNING id, name, email, hire_date, status, department_id, role_id;
    """

    SELECT_BY_ID = f"""
    SELECT id, name, email, hire_date, status, department_id, role_id
    FROM employee
    WHERE id = %(id)s;
    """

    SELECT_BY_EMAIL = f"""
    SELECT id, name, email, hire_date, status, department_id, role_id
    FROM employee
    WHERE email = %(email)s;
    """

    SELECT_ALL = f"""
    SELECT id, name, email, hire_date, status, department_id, role_id
    FROM employee;
    """
