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
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "#check number of arguments\n",
    "\n",
    "i = len(sys.argv)\n",
    "if i != 2:\n",
    "    print(\"ERROR\")\n",
    "    sys.exit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "first_argument = sys.argv[1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#check if everything is a number\n",
    "\n",
    "if (str.isdecimal(first_argument) == False):\n",
    "    print(\"ERROR\")\n",
    "    sys.exit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "#recast as an integer\n",
    "\n",
    "first_argument_int = int(first_argument)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I'm Even.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "if first_argument_int == 0:\n",
    "    print(\"I'm Zero.\\n\")\n",
    "elif (first_argument_int % 2 == 1):\n",
    "    print(\"I'm Odd.\\n\")\n",
    "else:\n",
    "    print(\"I'm Even.\\n\")"
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
