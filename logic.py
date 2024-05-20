from datetime import timedelta, datetime, tzinfo, timezone
from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        self.last_feed_time = datetime.now()

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.ability = self.get_ability()
        self.hp = randint(1,50)
        self.power = randint(1,50)


        Pokemon.pokemons[pokemon_trainer] = self




    # Метод для получения картинки покемона через API
    
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['official-artwork']['front_default'])
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"
        
    def get_ability(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data["abilities"][0]["ability"]["name"])

    def attack(self, enemy):
        enemy.hp -= self.power
        if enemy.hp <= 0:
            return "ты победил"
        else:
            return f"здоровье врага {enemy.hp}"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name} hp: {self.hp} power: {self.power}"
        

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img


    def ability_1(self):
        return self.ability
    
    def feed(self, feed_interval = 10, hp_increase = 10 ):
        current_time = datetime.now()  
        delta_time = timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {current_time+delta_time}"  
