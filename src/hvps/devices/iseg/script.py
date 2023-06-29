import re

input_file = "module.py"
output_file = "output.py"

pattern1 = r"-> ([^:]*):"
pattern2 = r"_write_command\(self._serial, command"
group1 = ""

with open(input_file, "r") as input_f, open(output_file, "w") as output_f:
    for line in input_f:
        match = re.search(pattern1, line)
        if match:
            group1 = match.group(1)  # Extract the wildcard value

        modified_line = re.sub(
            pattern2, f"_write_command(self._serial, command, {group1}", line
        )
        output_f.write(modified_line)
