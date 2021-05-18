# there is no block scope
# game_level= 3
# enemies = ["Skeleton","Zombie", "Alien"]

enemies = 1


def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function : {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


# Global constants
PI = 3.14159

# Naming convention use UPPERCASE:
