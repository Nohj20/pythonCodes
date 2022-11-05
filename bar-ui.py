from tkinter import Grid
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import random as rn


class MainGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MainGrid, self).__init__(**kwargs)
        self.cols = 2

        self.drinks = [
            ['Dry Martini Cocktail', 'Gibson', 'Manhattan', 'Cosmopolitan'],
            ['Brandy Alexander', 'Grasshopper', 'White Russian', 'Golden Cadillac'],
            ['Chi Chi', 'Frozen Mango Daiquire', 'Pina Colada', 'Frozen Daiquire'],
            ['Margarita', 'Whiskey Sour', 'Pink Lady', 'Kamikaze'],
            ['Virgin Mary', 'Virgin Colada', 'Shirley Temple', '4 Seasons'],
            ['Harvey Wallbanger', 'Tequila Sunrise', 'Mojito', 'Caipirinha'],
            ['Bloody Mary', 'Tom Collins', 'Cuba Libre', 'Negroni'],
            ['Vodka Martini', 'Gimlet Straight Up', 'Rob Roy', 'Perfect Manhattan']
        ]

        self.recipes = {
            self.drinks[0][0]:'60ml Gin, 15ml Dry Vermouth, Martini Glass, Olives or Lemon Twist',
            self.drinks[0][1]:'60ml Gin, 15ml Dry Vermouth, Martini Glass, Onion White Skin',
            self.drinks[0][2]:'60ml Whiskey, 15ml Sweet Vermouth, Dash Angustura Bitter, Martini Glass, Cherry',
            self.drinks[0][3]:'1jigger Vodka, 15ml Cointreau, 30ml Cranberry Juice, 15ml Lime Juice, Martini Glass, Lemon Slice',
            self.drinks[1][0]:'30ml Brandy, 30ml Cream/Evap, 30ml Crem de Cacao Brown, Cocktail Glass, Nutmeg',
            self.drinks[1][1]:'30ml Crem de Menthe Green, 30ml Cream/Evap, 30ml Crem de Cacao White, Cocktail Glass, Cherry',
            self.drinks[1][2]:'50ml Vodka, 30ml Cream/Evap, 20ml Coffee Liqueur, Old Fashioned Glass, Nutmeg',
            self.drinks[1][3]:'15ml Galliano, 15ml Cream/Evap, 30ml Crem de Cacao White, Cocktail Glass, Cherry',
            self.drinks[2][0]:'45ml Vodka, 90ml Pineapple Juice, 30ml Coconut Cream, Red Wine Glass, Pineapple Slice and Cherry',
            self.drinks[2][1]:'45ml White Rum, 15ml Sugar Syrup, 20ml Lime Juice, 6 Slices Mango, Cocktail Glass, Lime Slice',
            self.drinks[2][2]:'30ml White Rum, 30ml Coconut Milk, 90ml Pineapple Juice, Poco Grande Glass, Pineapple Slice',
            self.drinks[2][3]:'45ml White Rum, 15ml Sugar Syrup, 20ml Lime Juice, Cocktail Glass, Lime Slice',
            self.drinks[3][0]:'45ml Tequila, 20ml Triple Sec, 15ml Lime Juice, Margarita Glass Salt on Rim, Lime Slice',
            self.drinks[3][1]:'45ml Whiskey, 20ml Lemon Juice, 15ml Sugar Syrup, Dash Egg White, Old Fashioned Glass, Cherry',
            self.drinks[3][2]:'45ml Gin, 1 Egg White, 4dash Grenadine, Cocktail Glass, Cherry',
            self.drinks[3][3]:'30ml Triple Sec, 30ml Vodka, 30ml Lime Juice, Cocktail Glass, Lime Slice',
            self.drinks[4][0]:'90ml Tomato Juice, 15ml Lemon Juice, Dash Worcestershire Sauce, Salt, Pepper, Hot Sauce, Highball Glass, Celery Stalk',
            self.drinks[4][1]:'90ml Pineapple Juice, 60ml Coconut Cream, 10ml Whipped Cream, 25ml Lime Juice, Poco Grande Glass, Pineapple Slice',
            self.drinks[4][2]:'.25oz Grenadine, 7up, Highball Glass, Cherry',
            self.drinks[4][3]:'90ml Juices - Orange, Mango, Pineapple, Guava, Highball Glass, Orange Slice',
            self.drinks[5][0]:'45ml Vodka, 90ml Orange Juice, 15ml Galliano, Highball Glass, Orange Slice',
            self.drinks[5][1]:'45ml Tequila, 90ml Orange Juice, 15ml Grenadine, Highball Glass, Cherry',
            self.drinks[5][2]:'40ml White Rum, 30ml Lime Juice, 6 Mint Leaves, 10ml Sugar Syrup, Soda Water, Collins Glass, Mint and Straw',
            self.drinks[5][3]:'50ml Cachaca/Rum, 10ml Sugar Syrup, 4 Wedges Lime, Old Fashioned Glass, Lime Slice',
            self.drinks[6][0]:'30ml Vodka, 60ml Tomato Juice, 15ml Lemon Juice, Dash Worcestershire Sauce, Salt, Pepper, Hot Sauce, Highball Glass, Orange Slice',
            self.drinks[6][1]:'30ml Gin, 30ml Lemon Juice, 5ml Sugar Syrup, Soda Water, Highball Glass, Cherry',
            self.drinks[6][2]:'45ml White Rum, 180ml Cola, 10ml Lime Juice, Highball Glass, Lime Wedge',
            self.drinks[6][3]:'30ml Gin, 30ml Campari, 30ml Sweet Red Vermouth, Old Fashioned Glass, Orange Peel',
            self.drinks[7][0]:'60ml Vodka, 15ml Dry Vermouth, Martini Glass, Olive or Lemon Twist',
            self.drinks[7][1]:'45ml Gin, 15ml Lemon Juice, Soda Water, Cocktail Glass, LimeSlice',
            self.drinks[7][2]:'45ml Whiskey, 15ml Sweet Vermouth, Dash Angustura Bitter, Cocktail Glass, Lemon Twist',
            self.drinks[7][3]:'60ml Whiskey, 15ml Sweet Vermouth, 15ml Dry Vermouth, 2dash Angustura Bitter, Cocktail Glass, Lemon Slice'
        }

        self.check = ''
        self.done = []
        self.counter = 0
        self.score = 0

        self.inputs = []
        self.answers = []
        self.correctIng = ''

        self.scored = False

        #Label or Question
        self.add_widget(Label(text='Drink: ', font_size=30))
        self.drink = Label(text='', font_size=30)
        self.add_widget(self.drink)

        #Input Section        
        self.add_widget(Label(text='Enter Ingredients: ', font_size=30))
        self.ingredients = TextInput(multiline=True, font_size=30)
        self.add_widget(self.ingredients)

        #Buttons
        self.randomize = Button(text='Randomize', font_size=40)
        self.randomize.bind(on_press=self.randomizeDrink)
        self.add_widget(self.randomize)

        self.submitBtn = Button(text='Submit', font_size=40)
        self.submitBtn.bind(on_press=self.submit)
        self.add_widget(self.submitBtn)

        #Score and Counter
        self.add_widget(Label(text='Score:', font_size=40))
        self.scoreLabel = Label(text='0', font_size=40)
        self.add_widget(self.scoreLabel)

        self.add_widget(Label(text='Count:', font_size=40))
        self.counterLabel = Label(text='0', font_size=40)
        self.add_widget(self.counterLabel)

    def clearInputs(self):
        self.ingredients.text = ''

    def randomizeIndex(self):
        r1 = rn.randint(0, len(self.drinks)-1)
        r2 = rn.randint(0, len(self.drinks[r1])-1)
        self.check = self.drinks[r1][r2]

    def randomizeDrink(self, instance):
        self.clearInputs()
        self.randomizeIndex()
        self.scored = False

        self.counter += 1

        if self.counter > 32:

            layout = GridLayout(cols=1, padding=10)
            alertLabel = Label(text=f'You got {self.score} out of 32!')
            closeBtn = Button(text='Close Me!')

            layout.add_widget(alertLabel)
            layout.add_widget(closeBtn)

            popup = Popup(title='My popup', content=layout)
            popup.open()

            closeBtn.bind(on_press=popup.dismiss)

            self.counter = 1
            self.score = 0
            self.scoreLabel.text = str(self.score)
            self.done.clear()
            self.randomizeIndex()

        while self.check in self.done:
            self.randomizeIndex()

        out = self.recipes.get(self.check)
        self.answers = out.split(', ')

        self.done.append(self.check)

        self.drink.text = self.check
        self.counterLabel.text = str(self.counter)

    """def submit(self, instance):
        self.inputs = self.ingredients.text.split('\n')
        print(self.ingredients.text)
        print(self.inputs)

        if self.inputs == self.answers:
            self.score += 1

        for i in self.answers:
            self.correctIng += f'{i}\n'

        self.correctIngredients.text = self.correctIng
        self.scoreLabel.text = str(self.score)

        self.clearInputs()
        self.randomizeDrink(instance)"""

    def submit(self, instance):
        self.correctIng = ''
        self.inputs = self.ingredients.text.split('\n')

        if self.inputs == self.answers:
            if self.scored == False:
                self.score += 1
                self.scored = True
            result = 'You were Correct!'
        else:
            result = 'You were Incorrect!'
        
        for i in self.answers:
            self.correctIng += f'{i}\n'

        self.scoreLabel.text = str(self.score)

        layout = GridLayout(cols=1, padding=10)

        alertLabel = Label(text=result)
        popupLabel = Label(text=self.correctIng)
        closeBtn = Button(text='Close Me!')

        layout.add_widget(alertLabel)
        layout.add_widget(popupLabel)
        layout.add_widget(closeBtn)

        popup = Popup(title='My popup', content=layout, size=(400,400))
        popup.open()
        closeBtn.bind(on_press=popup.dismiss)


class Main(App):
    def build(self):
        return MainGrid()


if __name__ == '__main__':
    Main().run()
