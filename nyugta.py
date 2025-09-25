def main():
    star = "******************************"
    eq = "=============================="

    nyugta = (
        f"{star}\n"
        f"*{'NYUGTA':^28}*\n"
        f"{star}\n"
        "{:<10}{:>17} Ft\n".format("tétel1", "1234.20") +
        "{:<10}{:>17} Ft\n".format("tétel2", "45.12") +
        "{:<10}{:>17} Ft\n".format("tétel3", "232.35") +
        f"{eq}\n"
        "{:<10}{:>17} Ft\n".format("Összesen:", "1511.67") +
        "{:<10}{:>16} Ft\n".format("Szervízdíj:", "151.17") +
        f"{eq}\n"
        "{:<10}{:>17} Ft\n".format("Fizetendő:", "1662.84") +
        "\n"
        "---------           ----------\n"
        "  Dátum                 Név\n"
        f"{star}\n"
        "*{:^28}*\n".format("CÉG") +
        f"{star}"
    )

    print(nyugta)