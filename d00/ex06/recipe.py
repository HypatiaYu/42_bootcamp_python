{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Please select an option by typing the corresponding number:\n",
      "1: Add a recipe\n",
      "2: Delete a recipe\n",
      "3: Print a recipe\n",
      "4: Print the cookbook\n",
      "5: Quit 1\n"
     ]
    }
   ],
   "source": [
    "number = input(\"Please select an option by typing the corresponding number:\\n1: Add a recipe\\n2: Delete a recipe\\n3: Print a recipe\\n4: Print the cookbook\\n5: Quit\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "number = int(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "sandwich = {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'], 'meal' : 'lunch', 'prep_time' : 10}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "cake = {'ingredients' : ['flour', 'sugar', 'eggs'], 'meal' : 'dessert', 'prep_time' : 60}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "salad = {'ingredients' : ['avocado', 'arugula', 'tomato'], 'meal' : 'lunch', 'prep_time' : 15}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "cookbook = {'sandwich' : sandwich, 'cake' : cake, 'salad' : salad}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "#print ingredients \n",
    "\n",
    "def print_recipe(dish):\n",
    "    print(\"Recipe for \", dish, \":\")\n",
    "    print(\"Ingredients list: \", cookbook[dish]['ingredients'])\n",
    "    print(\"To be eaten for \", cookbook[dish]['meal'])\n",
    "    print(\"Takes \", cookbook[dish]['prep_time'], \" minutes of cooking.\")\n",
    "    print(\"\\n\")\n",
    "    return"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def delete_recipe(dish):\n",
    "    del cookbook[dish]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def print_cookbook():\n",
    "    for x in cookbook:\n",
    "        print_recipe(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_recipe(name, ingredients, meal_type, prep_time):\n",
    "    cookbook[name] = {'ingredients' : ingredients, 'meal' : meal_type, 'prep_time' : prep_time}\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "while (number != 5):\n",
    "    if number == 1:\n",
    "        recipe = input(\"Please enter the recipe's name to get its details\\n\")\n",
    "        name = input(\"Please enter the name\")\n",
    "        meal_type = input(\"Please enter the meal_type\")\n",
    "        ingredients = input(\"Please enter the ingredients separated by space\")\n",
    "        ingredients_list = ingredients.split()\n",
    "        prep_time = input(\"Please enter the prep_time\")\n",
    "        prep_time = int(prep_time)\n",
    "        add_recipe(name, ingredients_list, meal_type, prep_time)\n",
    "    elif number == 2:\n",
    "        recipe = input(\"Please enter the recipe's name to get its details\\n\")\n",
    "        delete_recipe(recipe)\n",
    "    elif number == 3:\n",
    "        recipe = input(\"Please enter the recipe's name to get its details\\n\")\n",
    "        print_recipe(recipe)\n",
    "    elif number == 4:\n",
    "        print_cookbook()\n",
    "    else:\n",
    "        print(\"This option does not exist, please type in the corresponding number\")\n",
    "    number = input(\"Please select an option by typing the corresponding number:\\n1: Add a recipe\\n2: Delete a recipe\\n3: Print a recipe\\n4: Print the cookbook\\n5: Quit\\n\")\n",
    "    number = int(number)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Recipe for  fudge :\n",
      "Ingredients list:  ['chocolate', 'bananas', 'sugars']\n",
      "To be eaten for  desert\n",
      "Takes  50  minutes of cooking.\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print_recipe('fudge')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
