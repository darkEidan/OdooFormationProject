def create_role_cli(service):
    name = input("Role name: ")
    level = input("Level: ")
    role = service.create(name, level)
    print("✅ Created:", role)


def list_roles_cli(service):
    for r in service.list():
        print(r)