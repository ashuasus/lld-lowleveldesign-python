from .plain_pizza import PlainPizza
from .farmhouse import Farmhouse
from .chicken_dominator import ChickenDominator
from .tandoori_paneer_delight import TandooriPaneerDelight
from .extra_cheese_topping import ExtraCheeseTopping
from .mushroom_topping import MushroomTopping
from .pepperoni_topping import PepperoniTopping
from .veggies_topping import VeggiesTopping


# Step 5: Client Demonstration
def main():
    print("======= Decorator Design Pattern ======")
    # Create a plain pizza
    pizza1 = PlainPizza()
    print("Order 1: " + pizza1.get_description() + " = Rs." + str(pizza1.get_cost()))

    # Add toppings to the PlainPizza - Extra Cheese Only
    pizza2 = ExtraCheeseTopping(PlainPizza())
    print("Order 2: " + pizza2.get_description() + " = Rs." + str(pizza2.get_cost()))

    # Add toppings to the PlainPizza - Extra Cheese and Veggies
    pizza3 = VeggiesTopping(ExtraCheeseTopping(PlainPizza()))
    print("Order 3: " + pizza3.get_description() + " = Rs." + str(pizza3.get_cost()))

    # Add toppings to the PlainPizza - Extra Cheese and Pepperoni
    pizza4 = PepperoniTopping(ExtraCheeseTopping(PlainPizza()))
    print("Order 4: " + pizza4.get_description() + " = Rs." + str(pizza4.get_cost()))

    # Add toppings to the PlainPizza - Extra Cheese, Mushroom and Pepperoni
    pizza5 = MushroomTopping(PepperoniTopping(ExtraCheeseTopping(PlainPizza())))
    print("Order 5: " + pizza5.get_description() + " = Rs." + str(pizza5.get_cost()))

    # Farmhouse Pizza
    pizza6 = Farmhouse()
    print("Order 6: " + pizza6.get_description() + " = Rs." + str(pizza6.get_cost()))

    # Farmhouse Pizza with Extra Cheese and Mushroom
    pizza7 = MushroomTopping(ExtraCheeseTopping(Farmhouse()))
    print("Order 7: " + pizza7.get_description() + " = Rs." + str(pizza7.get_cost()))

    # Tandoori Paneer Delight Pizza
    pizza8 = TandooriPaneerDelight()
    print("Order 8: " + pizza8.get_description() + " = Rs." + str(pizza8.get_cost()))

    # Chicken Dominator
    pizza9 = ChickenDominator()
    print("Order 9: " + pizza9.get_description() + " = Rs." + str(pizza9.get_cost()))

    # Chicken Dominator with Mushroom
    pizza10 = MushroomTopping(ChickenDominator())
    print("Order 10: " + pizza10.get_description() + " = Rs." + str(pizza10.get_cost()))


if __name__ == "__main__":
    main()
