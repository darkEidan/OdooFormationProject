from application.services.container import Container
from api.menu.main_menu import MainMenu


def main():

    main_service = Container()

    main_menu = MainMenu(main_service)

    main_menu.run()


if __name__ == "__main__":
    main()
