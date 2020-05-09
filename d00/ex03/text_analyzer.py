{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [],
   "source": [
    "def text_analyzer(string):\n",
    "    spaces = sum(c.isspace() for c in string)\n",
    "    numbers = sum(c.isdigit() for c in string)\n",
    "    lc_letters = sum(c.isalpha() & c.islower() for c in string)\n",
    "    uc_letters = sum(c.isalpha() & c.isupper() for c in string)\n",
    "    return spaces, numbers, lc_letters, uc_letters"
   ]
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
