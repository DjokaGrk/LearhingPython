import turtle
import pandas as pd
import random

class CapitalCitiesGame:
    def __init__(self, data_file, image_file):
        self.screen = turtle.Screen()
        self.screen.title("Capital Cities Game")
        self.screen.setup(width=740, height=1024)
        self.screen.addshape(image_file)
        turtle.shape(image_file)

        self.pd_data = pd.read_csv(data_file)
        self.all_states = self.pd_data["state"].to_list()
        self.all_cities = self.pd_data["city"].to_list()
        self.answered_cities = []
        self.asked_states = set()
        self.writer = turtle.Turtle()
        self.writer.hideturtle()
        self.writer.penup()

    def get_random_state(self):
        remaining_states = [state for state in self.all_states if state not in self.asked_states]
        if not remaining_states:
            return None
        random_state = random.choice(remaining_states)
        self.asked_states.add(random_state)
        return random_state

    def get_city_of_state(self, state):
        state_data = self.pd_data[self.pd_data.state.str.lower() == state.lower()]
        if state_data.empty:
            return None
        return state_data.city.values[0]

    def write_city_on_map(self, city):
        city_data = self.pd_data[self.pd_data.city.str.lower() == city.lower()]
        if not city_data.empty:
            self.writer.goto(int(city_data.x.values[0]), int(city_data.y.values[0]))
            self.writer.write(city, align="center", font=("Arial", 12, "bold"))
        else:
            print(f"Coordinates for {city} not found.")

    def play(self):
        while len(self.answered_cities) < len(self.all_cities):
            random_state = self.get_random_state()
            if not random_state:
                break
            city_of_state = self.get_city_of_state(random_state)
            if not city_of_state:
                print(f"State '{random_state}' not found in data. Skipping.")
                continue

            answer_city = self.screen.textinput(
                title=f"Pogodi Glavni grad. {len(self.answered_cities)}/{len(self.all_cities)} Correct",
                prompt=f"{random_state}: Koji je Glavni Grad? (Type 'Exit' to quit)",
            )
            if not answer_city:
                continue

            answer_city = answer_city.strip().title()

            if answer_city == "Exit":
                break
            if answer_city == city_of_state and answer_city not in self.answered_cities:
                self.answered_cities.append(answer_city)
                self.write_city_on_map(answer_city)
            elif answer_city in self.answered_cities:
                print("You have already guessed that city.")
            else:
                print("That is not the correct capital city.")

        if len(self.answered_cities) == len(self.all_cities):
            self.screen.textinput(title="Bravo!", prompt="Pogodio si sve glavne gradove! Pritisni Enter za izlaz.")
        self.screen.bye()

if __name__ == "__main__":
    game = CapitalCitiesGame("europe_states.csv", "EuropePrintNoText-740x1024.gif")
    game.play()
