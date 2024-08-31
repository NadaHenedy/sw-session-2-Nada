class Robot:
  def __init__(self,name):
    self.name = name
    self.battery_level = 100

  def status(self):
        print(f"Robot name: {self.name}")
        print(f"Battery level: {self.get_battery_level()}")  

  def move(self):
    self.battery_level -= 10

  def get_name(self):
    return self.name

  def get_battery_level(self):
    return self.battery_level

  def set_name(self,name):
    self.name = name

  def set_battery_level(self,battery_level):
    self.battery_level = battery_level

class GroudRobot(Robot):
  def __init__(self,name,wheels):
    super().__init__(name)
    self.wheels = wheels

  def move(self):
    super().move()
    self.wheels -= 1

  def get_wheels(self):
    return self.wheels

  def set_wheels(self,wheels):
    self.wheels = wheels

class AerialRobot(Robot):
  def __init__(self,name,rotors):
    super().__init__(name)
    self.rotors = rotors

  def move(self):
    super().move()
    self.rotors -= 1

  def get_rotors(self):
    return self.rotors

  def set_rotors(self,rotors):
    self.rotors = rotors

class FleetManagement:
  def __init__(self):
    self.robots = []
    
  def add_robot(self,robot):
    self.robots.append(robot)

  def remove_robot(self,robot):
    self.robots.remove(robot)

  def get_robots(self):
    return self.robots

  def control_robots(self):
    for robot in self.robots:
        robot.move()
        robot.status()
        
  def display_robots(self):
    for robot in self.robots:
        print(f"Robot name: {robot.get_name()}")
        print(f"Battery level: {robot.get_battery_level()}")


def main():
  ground_robot = GroudRobot("ground robot", 4)  # Updated to match the provided output
  aerial_robot = AerialRobot("aerial robot", 6)  # Updated to match the provided output

  fleet_management = FleetManagement()
  fleet_management.add_robot(ground_robot)
  fleet_management.add_robot(aerial_robot)

  fleet_management.control_robots()
  fleet_management.display_robots()

  ground_robot.status()
  aerial_robot.status()

if __name__ == "__main__":
  main()
