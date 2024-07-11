




def generate_gpio_init(port, pin, direction):
    """ Generate init function for GPIO on AVR microcontroller """
    if direction == 'output':
        init_code = f"""
void init_gpio() {{
    // Initialize pin {pin} of port {port} as OUTPUT
    DDR{port} |= (1 << {pin});
}}
"""
    elif direction == 'input':
        init_code = f"""
void init_gpio() {{
    // Initialize pin {pin} of port {port} as INPUT
    DDR{port} &= ~(1 << {pin});
}}
"""
    else:
        raise ValueError("Direction must be 'input' or 'output'.")

    return init_code

# Example usage:

port_name = input("Enter the port_name A,B,C,D : ")  # Example port B
pin_number = int (input("Enter the pin number :- "))  # Example pin 3
pin_direction = input("Enter the direction input or output :- ")  # 'output' or 'input'

init_function_code = generate_gpio_init(port_name, pin_number, pin_direction)
print(init_function_code)
