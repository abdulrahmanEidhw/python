{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def conform(fav):\n",
    "    fav= 42\n",
    "    return fav \n",
    "\n",
    "if __name__== \"__main__\":\n",
    "    print ('Welcome')\n",
    "    fav =7\n",
    "    conform(fav)\n",
    "    #fav = conform(fav)\n",
    "    print(\"my favorite # is \", fav )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1.2"
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
      "Inside the function {'A': 28, 'B': 25, 'C': 32, 'D': 25, 'E': 30, 'F': 28}\n",
      "outside the function: {'A': 28, 'B': 25, 'C': 32, 'D': 25, 'E': 30, 'F': 28}\n"
     ]
    }
   ],
   "source": [
    "student={'A':28, 'B':25, 'C':32, 'D':25}\n",
    "def test(student):\n",
    "    new={'E':30, 'F':28}\n",
    "    student.update(new)\n",
    "    print(\"Inside the function\", student )\n",
    "    return \n",
    "test(student)\n",
    "print(\"outside the function:\", student)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. python classes"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "##  exercise 2.1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Student:\n",
    "    \n",
    "    def __init__(self, name):\n",
    "        self.name=name \n",
    "        self.course_list= []\n",
    "std=Student(\"Set_here_your_name\")\n",
    "print(std.name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# the class is public and all variable is public\n",
    "\n",
    "#if you want to make it private  you should put __\n",
    "\n",
    "# if you want to make it protected you put _ \n",
    "#(no accec only by inhertence(extend in java)) in python\n",
    "#you put the father class in bracket()\n",
    "\n",
    "#constructor give default or initlize value =>\n",
    "#def __init__(self=this in java,here u intlize value u want)\n",
    "\n",
    "#creating obj from student callss example:-\n",
    "#std= student(\"abdualrahman\")\n",
    "#print(std.name)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## methods 2.1 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['Python']\n"
     ]
    }
   ],
   "source": [
    "class Student:\n",
    "    def __init__(self, name):\n",
    "        self.name=name\n",
    "        self.course_list=[]\n",
    "    def add(self, new_course):\n",
    "            self.course_list.append(new_course)\n",
    "    def greeting( name)\n",
    "        pass\n",
    "            \n",
    "std=Student(\"abdulrahman\")\n",
    "std.add(\"Python\")\n",
    "\n",
    "print(std.course_list)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "## homeWork \n",
    "##add multiple values in the list *for loop *"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "# save as  => filename.py\n",
    "# save it in same dir then we can call the function \n",
    "#from another project by import filename from python version\n",
    "#"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2.3 LOOP \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Student:\n",
    "    \n",
    "    def __init__(self, name):\n",
    "        self.name=name\n",
    "        self.course_list= []\n",
    "    def add(self, new_course):\n",
    "        \n",
    "        self.course_list.append(new_course)\n",
    "        \n",
    "std=Student(\"Set_here_your_name\")\n",
    "\n",
    "for i in range(2):\n",
    "    txt = input(\"Type something to test this out: \")\n",
    "    std.add(txt)\n",
    "    \n",
    "print(std.course_list)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 2.2 ingeritance"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "class Person:\n",
    "    def __init__(self,fname, lname):\n",
    "        self.firstname = fname \n",
    "        self.lastname = lname \n",
    "        \n",
    "    def printname(self):\n",
    "        print(self.firstname, self.lastname)\n",
    "\n",
    "# this is the father class (inhertence)\n",
    "class Professor(Person):\n",
    "    pass\n",
    "mhd = Professor(\"Mohammed\",\"AlSarem\")\n",
    "mhd.printname()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mohammed AlSarem\n"
     ]
    }
   ],
   "source": [
    "class Person:\n",
    "    def __init__(self,fname, lname):\n",
    "        self.firstname = fname \n",
    "        self.lastname = lname \n",
    "        \n",
    "    def printname(self):\n",
    "        print(self.firstname, self.lastname)\n",
    "\n",
    "# this is the child class (inhertence)\n",
    "class Professor(Person):\n",
    "    def __init__(self,fname, lname):\n",
    "        self.firstname = fname \n",
    "        self.lastname = lname \n",
    "mhd = Professor(\"Mohammed\",\"AlSarem\")\n",
    "mhd.printname()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2.3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mohammed AlSarem 5\n"
     ]
    }
   ],
   "source": [
    "class Person:\n",
    "    def __init__(self,fname, lname):\n",
    "        self.firstname = fname \n",
    "        self.lastname = lname \n",
    "        \n",
    "    def printname(self):\n",
    "        print(self.firstname, self.lastname,self.number)\n",
    "\n",
    "# this is the child class (inhertence)\n",
    "class Professor(Person):\n",
    "    def __init__(self,fname, lname, num):\n",
    "        \n",
    "        self.firstname = fname \n",
    "        self.lastname = lname \n",
    "        self.number = num\n",
    "mhd = Professor(\"Mohammed\",\"AlSarem\", 5)\n",
    "mhd.printname()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import lab_3"
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
