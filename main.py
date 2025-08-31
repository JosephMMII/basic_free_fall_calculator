import functions as f

### This is a simple calculator to find height, time, and velocity of an object
### falling parallel to the ground with no angular momentum or wind resistance.

g = 9.81 # Meters per second squared
    
def main():
    while True:
        select_calc = input("SYSTEM: What answer do you need? (Enter a number or exit to close program):\n"
                            "         1: Time until object touched the ground\n"
                            "         2: Initial height of object given time\n"
                            "         3: Find final velocity at impact\n"
                            "USER: ")
        
        if select_calc.lower() == "exit":
            f.sys.exit()

        if select_calc not in {"1", "2", "3"}:
            print("SYSTEM: Please enter a number that's available")
            continue

        num = int(select_calc)

        if num == 1:
            height = f.get_float_input("SYSTEM: Enter initial height in meters\nUSER: ")
            time = f.math.sqrt((2 * height) / g)
            print(f'SYSTEM: Time to impact =  {time:.2f}s')

        elif num == 2:
            time = f.get_float_input("SYSTEM: Enter time to impact (s)\nUSER:")
            height = f.find_initial_height(time)
            print(f"SYSTEM: Initial height = {height:.2f} m")

        elif num == 3:
            while True:
                choice = input("SYSTEM: Find velocity using height or time?\n"
                            "          1: Height\n"
                            "          2: Time\n"
                            "USER: ")
                if choice.lower() == "exit":
                    f.sys.exit()
                try:
                    choice = int(choice)
                    if choice > 0 and choice < 3:
                        break
                    else:
                        print("Invalid input")
                        pass
                except ValueError:
                    print("Invalid input")
                    pass

            if choice == 1:
                height = f.get_float_input("SYSTEM: Enter height (m)\nUSER: ")
                velocity = f.final_velocity_with_height(height)
                print(f"SYSTEM: The final velocity is {velocity:.2f} (m/s)")
            elif choice == 2:
                time = f.get_float_input("SYSTEM: Enter time (s)\nUSER: ")
                velocity = f.final_velocity_with_time(time)
                print(f"SYSTEM: The final velocity is {velocity:.2f} (m/s)")
            else:
                print("SYSTEM: Invalid input")
                continue

        stop_prgm = input("SYSTEM: Want to calculate something else? (Y/N)\nUSER: ").lower()
        if stop_prgm != "y":
            f.sys.exit()

if __name__ == "__main__":
    main()