{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\Hypatia\\\\git\\\\bootcamp\\\\data\\\\bacterial_growth'"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "#get list of arguments\n",
    "arg_list = sys.argv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['C:\\\\Users\\\\Hypatia\\\\Anaconda3\\\\lib\\\\site-packages\\\\ipykernel_launcher.py', '-f', 'C:\\\\Users\\\\Hypatia\\\\AppData\\\\Roaming\\\\jupyter\\\\runtime\\\\kernel-f9f654cb-0cd4-4d3f-83e0-ae5f2c54288e.json']\n"
     ]
    }
   ],
   "source": [
    "print(arg_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#concatenate into one string\n",
    "string = ''.join(arg_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "string = string.swapcase()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Function that reverses the string\n",
    "def reverse(s):\n",
    "    if len(s) == 0:\n",
    "        return s\n",
    "    else:\n",
    "        return reverse(s[1:]) + s[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "#reverse the input string\n",
    "string = reverse(string)"
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
      "NOSJ.E88245C2F5EA-0E38-F3D4-4DC0-BC456F9F-LENREK\\EMITNUR\\RETYPUJ\\GNIMAOr\\ATAdPPa\\AITAPYh\\SRESu\\:cF-YP.REHCNUAL_LENREKYPI\\SEGAKCAP-ETIS\\BIL\\3ADNOCANa\\AITAPYh\\SRESu\\:c\n"
     ]
    }
   ],
   "source": [
    "print(string)"
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
