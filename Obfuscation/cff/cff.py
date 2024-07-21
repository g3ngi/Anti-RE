# ================ Simple CFF ================ 

def switch_flatten(basic_blocks):
    block_mapping = {name: code for name, code in basic_blocks}
    flattened_code = []
    dispatcher_code = []
    table = []

    for i, (name, code) in enumerate(basic_blocks):
        table.append(f"case {i}: {code}; next = {i+1}; break;")

    flattened_code.append("int next = 0;")
    flattened_code.append("while (next >= 0) {")
    flattened_code.append("  switch (next) {")
    flattened_code.extend(f"    {entry}" for entry in table) # add dispatcher
    flattened_code.append("  }")
    flattened_code.append("}")

    return '\n'.join(flattened_code)


def call_flatten(basic_blocks):
    functions = []
    function_definitions = []
    dispatch_table = []

    for i, (name, code) in enumerate(basic_blocks):
        func_name = f"func_{i}"
        function_definitions.append(f"void {func_name}() {{ {code} }};")
        dispatch_table.append(f"    {func_name},")

    flattened_code = []
    flattened_code.extend(function_definitions)
    flattened_code.append("")
    flattened_code.append("void call_dispatch_flatten() {")
    flattened_code.append("    void (*dispatch_table[])() = {")
    flattened_code.extend(dispatch_table)
    flattened_code.append("    };")
    flattened_code.append("")
    flattened_code.append("    int next = 0;")
    flattened_code.append("    while (next >= 0) {")
    flattened_code.append("        if (next < sizeof(dispatch_table) / sizeof(dispatch_table[0])) {")
    flattened_code.append("            dispatch_table[next]();")
    flattened_code.append("        }")
    flattened_code.append("        next++;")
    flattened_code.append("    }")
    flattened_code.append("}")

    return '\n'.join(flattened_code)

# ================ Advance CFF ================ 


def goto_switch_flatten(basic_blocks):
    block_mapping = {name: code for name, code in basic_blocks}
    flattened_code = []
    dispatcher_code = []
    table = []

    # Create table and dispatcher
    for i, (name, code) in enumerate(basic_blocks):
        table.append(f"case {i}: goto {name};")
        dispatcher_code.append(f"{name}: {code}; next = {i + 1}; break;")

    # Assemble the flattened control flow
    flattened_code.append("int next = 0;")
    flattened_code.append("while (next >= 0) {")
    flattened_code.append("  switch (next) {")
    flattened_code.extend(f"    {entry}" for entry in table)
    flattened_code.extend(f"    {i}" for i in dispatcher_code) # add dispatcher
    flattened_code.append("  }")
    flattened_code.append("}")

    return "\n".join(flattened_code)

basic_blocks = [
    ("A", "puts('Block A');"),
    ("B", "puts('Block B');"),
    ("C", "puts('Block C');"),
]

print(call_flatten(basic_blocks))