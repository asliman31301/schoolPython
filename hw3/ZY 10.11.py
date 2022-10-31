#Ahmad SLiman 1898612

class FoodItem:
    def __init__(self, name = 'None' , fat = 0, carbs = 0, protein= 0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
        self.num_servings = 1



    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self, num_servings):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        print(f'Number of calories for {num_servings:.2f} serving(s): {self.get_calories(num_servings):.2f}')









def main():
    f = FoodItem()

    name = str(input())
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    num_serving = float(input())

    f.print_info(num_serving)
    print("")

    f.name = name
    f.fat = fat
    f.carbs = carbs
    f.protein = protein

    f.print_info(num_serving)



if __name__ == '__main__':
    main()