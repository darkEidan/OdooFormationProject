def create_department_cli(service):
    name = input("Department name: ")
    dept = service.create(name)
    print("✅ Created:", dept)


def list_departments_cli(service):
    for d in service.list():
        print(d)