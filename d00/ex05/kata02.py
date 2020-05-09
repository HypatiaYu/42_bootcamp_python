{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "num = (3, 30, 2019, 9, 25)\n",
    "\n",
    "time = ('hour', 'minutes', 'year', 'month', 'day')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "#convert into string + add padding\n",
    "\n",
    "num2 = [str(x).zfill(2) for x in num]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "#convert into a dictionary \n",
    "result = {time[i] : num2[i] for i, _ in enumerate(time)}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "09 / 25 / 2019   03 : 30\n"
     ]
    }
   ],
   "source": [
    "print(result['month'], \"/\", result['day'], \"/\", result['year'], \" \", result['hour'], \":\", result['minutes'])"
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
