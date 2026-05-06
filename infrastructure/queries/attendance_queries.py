class AttendanceQueries:

    INSERT_CHECK_IN = """
    INSERT INTO attendance (employee_id, check_in, work_date)
    VALUES (%(employee_id)s, %(check_in)s, %(work_date)s)
    RETURNING id, employee_id, check_in, check_out, work_date;
    """

    UPDATE_CHECK_OUT = """
    UPDATE attendance
    SET check_out = %(check_out)s
    WHERE employee_id = %(employee_id)s AND check_out IS NULL
    RETURNING id, employee_id, check_in, check_out, work_date;
    """

    SELECT_OPEN_ATTENDANCE = """
    SELECT id, employee_id, check_in, check_out, work_date FROM attendance
    WHERE employee_id = %(employee_id)s AND check_out IS NULL;
    """

    SELECT_BY_EMPLOYEE = """
    SELECT id, employee_id, check_in, check_out, work_date FROM attendance
    WHERE employee_id = %(employee_id)s
    ORDER BY check_in DESC;
    """
