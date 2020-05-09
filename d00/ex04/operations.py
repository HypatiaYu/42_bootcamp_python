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
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "InputError: too many arguments\n"
     ]
    }
   ],
   "source": [
    "#check the number of arguments\n",
    "\n",
    "i = len(sys.argv)\n",
    "if (i > 2):\n",
    "    print(\"InputError: too many arguments\")\n",
    "    sys.exit\n",
    "elif (i == 1):\n",
    "    print(\"Usage: python operations.py <number1><number2>\\n\")\n",
    "    print(\"Example:\\n\")\n",
    "    print(\"python oprations.py 10 3\")\n",
    "    sys.exit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "number1 = sys.argv[1]\n",
    "number2 = sys.argv[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Usage: python operations.py <number1><number2>\n",
      "\n",
      "Example:\n",
      "\n",
      "python oprations.py 10 3\n"
     ]
    }
   ],
   "source": [
    "#check if the inputs are numeric\n",
    "\n",
    "if number1.isnumeric() == False or number1.isnumeric():\n",
    "    print(\"Usage: python operations.py <number1><number2>\\n\")\n",
    "    print(\"Example:\\n\")\n",
    "    print(\"python oprations.py 10 3\")\n",
    "    sys.exit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "#recast as integers\n",
    "number1 = \"1\"\n",
    "number2 = \"2\"\n",
    "number1 = int(number1)\n",
    "number2 = int(number2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "#perform operations\n",
    "num_sum = number1 + number2\n",
    "num_diff = number1 - number2\n",
    "num_prod = number1 * number2\n",
    "num_quotient = number1 / float(number2)\n",
    "num_remainder = number1 % number2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sum:\t\t 3\n",
      "Difference:\t -1\n",
      "Product:\t 2\n",
      "Quotient:\t 0.5\n",
      "Remainder:\t 1\n"
     ]
    }
   ],
   "source": [
    "#print numbers\n",
    "\n",
    "print(\"Sum:\\t\\t\", num_sum)\n",
    "print(\"Difference:\\t\", num_diff)\n",
    "print(\"Product:\\t\", num_prod)\n",
    "print(\"Quotient:\\t\", num_quotient)\n",
    "print(\"Remainder:\\t\", num_remainder)"
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
