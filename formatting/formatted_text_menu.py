MENU_LEN = 63


class FormattedTextMenu:
    @staticmethod
    def main_title(title):
        outer_line = "|" + "*" * (MENU_LEN - 2) + "|"
        middle_line = "|" + \
            ("{:^" + str(MENU_LEN - 2) + "}").format(title) + "|"
        return outer_line + "\n" + middle_line + "\n" + outer_line

    @staticmethod
    def sub_title(title):
        outer_line = "|" + "=" * (MENU_LEN - 2) + "|"
        middle_line = "|" + \
            ("{:^" + str(MENU_LEN - 2) + "}").format(title) + "|"
        return outer_line + "\n" + middle_line + "\n" + outer_line

    @staticmethod
    def options_menu(options):
        outer_line = "|" + "-" * (MENU_LEN - 2) + "|"
        options_text = "|" + \
            ("{:<" + str(MENU_LEN - 2) + "}").format(" Options:") + "|\n"

        for option in options:
            options_text += "|" + ("{:<" + str(MENU_LEN - 2) + "}").format((" " * 6)
                                                                           + str(options.index(option) + 1) + ". " + option) + "|\n"
        return options_text + outer_line

    @staticmethod
    def body_content(content):
        pass

    @staticmethod
    def error_title(title):
        outer_line = "|" + "#" * (MENU_LEN - 2) + "|"
        middle_line = "|" + \
            ("{:^" + str(MENU_LEN - 2) + "}").format(title) + "|"
        return outer_line + "\n" + middle_line + "\n" + outer_line
