from application.services.main_service import MainService
from api.menu.main_menu import MainMenu


def main():

    main_service = MainService()

    main_menu = MainMenu(main_service)

    main_menu.run()


if __name__ == "__main__":
    main()
