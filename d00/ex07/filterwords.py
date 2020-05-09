{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "#check the number of arguments\n",
    "if (len(sys.argv) != 3):\n",
    "    print(\"ERROR\")\n",
    "    sys.exit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ERROR\n"
     ]
    }
   ],
   "source": [
    "#Check if arguments have the correct datatype\n",
    "if (isinstance(sys.argv[1], str) == False):\n",
    "    print(\"ERROR\")\n",
    "    sys.exit\n",
    "elif (isinstance(sys.argv[2], int) == False):\n",
    "    print(\"ERROR\")\n",
    "    sys.exit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "#split input into a list\n",
    "sentence = \"this is a sentence\"\n",
    "# = (sys.argv[1]).split(' ')\n",
    "word_list = (sentence).split(' ')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "upper_bound = sys.argv[2]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "upper_bound = 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [],
   "source": [
    "#remove components that are below the threshold\n",
    "for i in range(0, len(word_list) -1):\n",
    "    if (len(word_list[i]) < 0):\n",
    "        word_list[i].pop        "
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
