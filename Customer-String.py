def format_string(s, operations):
    def _uppercase(s):
        return s.upper()

    def _reverse(s):
        return s[::-1]

    def _capitalize(s):
        return s.capitalize()

    if "uppercase" in operations:
        s = _uppercase(s)
    if "reverse" in operations:
        s = _reverse(s)
    if "capitalize" in operations:
        s = _capitalize(s)

    print(s)

s = "nada henedy"
operations = ["uppercase", "reverse"]
format_string(s, operations)
