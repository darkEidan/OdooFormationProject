class LeaveQueries:

    INSERT = """
    INSERT INTO leave_request (employee_id, leave_type, start_date, end_date, status)
    VALUES (%(employee_id)s, %(leave_type)s, %(start_date)s, %(end_date)s, %(status)s)
    RETURNING id, employee_id, leave_type, start_date, end_date, status, created_at;
    """

    SELECT_BY_ID = """
    SELECT id, employee_id, leave_type, start_date, end_date, status, created_at
    FROM leave_request
    WHERE id = %(id)s;
    """

    SELECT_BY_EMPLOYEE = """
    SELECT id, employee_id, leave_type, start_date, end_date, status, created_at
    FROM leave_request
    WHERE employee_id = %(employee_id)s
    ORDER BY start_date DESC;
    """

    UPDATE = """
    UPDATE leave_request
    SET 
        employee_id = %(employee_id)s,
        leave_type = %(leave_type)s,
        start_date = %(start_date)s,
        end_date = %(end_date)s,
        status = %(status)s
    WHERE id = %(id)s
    RETURNING id, employee_id, leave_type, start_date, end_date, status, created_at;
    """

    DELETE = """
    DELETE FROM leave_request
    WHERE id = %(id)s;
    """

    SELECT_OVERLAPPING = """
    SELECT id, employee_id, leave_type, start_date, end_date, status, created_at
    FROM leave_request
    WHERE employee_id = %(employee_id)s
      AND NOT (end_date < %(start_date)s  OR  start_date > %(end_date)s);
    """
