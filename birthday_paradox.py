import app_functions
import constants


def main() -> None:
    app_functions.show_message(constants.GREET_MESSAGE)

    amount_of_birthdays = app_functions.get_amount_of_birthdays()
    app_functions.show_message()

    birthdays = app_functions.get_birthdays(amount_of_birthdays)
    app_functions.show_message(f'Oto {amount_of_birthdays} dni urodzin:')
    app_functions.show_generate_birthdays(birthdays)
    app_functions.show_message()

    match = app_functions.get_match(birthdays)
    app_functions.show_message(app_functions.get_match_message(match))

    app_functions.show_message(f'Generowanie, {amount_of_birthdays} losowych dni urodzin '
                               f'{constants.NUMBER_OF_SIMULATION} razy...')
    input(constants.INPUT_SIMULATION_PROMPT)
    simulation_match = app_functions.get_simulation_match(amount_of_birthdays)


if __name__ == '__main__':
    main()
