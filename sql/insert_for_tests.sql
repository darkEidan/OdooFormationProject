```sql id="l4x8nm"
-- ======================
-- DEPARTMENTS
-- ======================

INSERT INTO department (name) VALUES
('IT'),
('HR'),
('Finance');

-- ======================
-- ROLES
-- ======================

INSERT INTO role (name, level) VALUES
('Developer', 'junior'),
('Developer', 'senior'),
('HR Manager', 'senior'),
('Accountant', 'mid');

-- ======================
-- EMPLOYEES
-- ======================

INSERT INTO employee (name, email, hire_date, status, department_id, role_id) VALUES
('John Doe', 'john.doe@example.com', '2022-03-01', 'active', 1, 2),
('Jane Smith', 'jane.smith@example.com', '2023-06-15', 'active', 2, 3),
('Alice Brown', 'alice.brown@example.com', '2021-11-20', 'suspended', 3, 4);

-- ======================
-- LEAVE REQUESTS
-- ======================

INSERT INTO leave_request (employee_id, type, start_date, end_date, status) VALUES
(1, 'vacation', '2026-06-01', '2026-06-05', 'pending'),
(2, 'sick', '2026-05-10', '2026-05-12', 'approved'),
(1, 'vacation', '2026-07-15', '2026-07-20', 'rejected');

-- ======================
-- ATTENDANCE
-- ======================

INSERT INTO attendance (employee_id, work_date, check_in, check_out) VALUES
(1, '2026-05-01', '2026-05-01 09:00:00', '2026-05-01 17:30:00'),
(1, '2026-05-02', '2026-05-02 09:15:00', '2026-05-02 18:00:00'),
(2, '2026-05-01', '2026-05-01 08:45:00', '2026-05-01 17:00:00');

-- ======================
-- DOCUMENTS (FOLDER)
-- ======================

INSERT INTO employee_document (employee_id, name, type, file_path, status) VALUES
(1, 'Employment Contract', 'contract', '/docs/john_contract.pdf', 'active'),
(1, 'Performance Review 2025', 'performance', '/docs/john_review_2025.pdf', 'active'),
(2, 'HR Policy Agreement', 'administrative', '/docs/jane_policy.pdf', 'active'),
(3, 'Warning Letter', 'administrative', '/docs/alice_warning.pdf', 'archived');

-- ======================
-- PAYROLL RECORDS (SIMPLIFIED)
-- ======================

INSERT INTO payroll_record (
    employee_id,
    period_start,
    period_end,
    base_salary,
    worked_hours,
    overtime_pay,
    bonus,
    deductions,
    final_salary
) VALUES
(1, '2026-04-01', '2026-04-30', 3000.00, 172.00, 240.00, 300.00, 100.00, 3440.00),
(2, '2026-04-01', '2026-04-30', 3500.00, 160.00, 0.00, 200.00, 0.00, 3700.00),
(3, '2026-04-01', '2026-04-30', 2800.00, 150.00, 0.00, 0.00, 150.00, 2650.00);
```
