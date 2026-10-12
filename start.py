"""
start.py (PROVIDED: do not modify)
Runs your game. Run it with: python3 start.py
"""
from rps import rps
 "Runs the whole program"
 print_initial_header()

p1_name = get_name(Player_1)
p2_name = get_name(Player_2)

choice = get_menu_choice()

 
def main():
    rps()
 
 
if __name__ == "__main__":
    main()
 
