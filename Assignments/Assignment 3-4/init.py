#this module exists so that the list can be globally used
import copy
global students
students=[{'P1':3,'P2':8,'P3':10},{'P1':10,'P2':10,'P3':9},{'P1':2,'P2':4,'P3':8},{'P1':3,'P2':2,'P3':5},{'P1':10,'P2':10,'P3':10},{'P1':6,'P2':7,'P3':8},{'P1':4,'P2':2,'P3':10},{'P1':5,'P2':2,'P3':1},{'P1':8,'P2':8,'P3':8},{'P1':6,'P2':7,'P3':10}] #predefined list
histudents1=copy.deepcopy(students)
global histudents
histudents=[]
histudents.append(histudents1.copy())

