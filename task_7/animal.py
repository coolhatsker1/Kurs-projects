#!/usr/bin/env python3

class Animal:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

class Pet(Animal):
    def describe(self):
        descr = f'Pet name: {self.name}\n'f'Pet age: {self.age}\n'f'Pet weight: {self.weight}\n'
        print(descr)

class Cat(Pet):
    def __init__(self, name, age, weight, kind='Cat'):
        super().__init__(name, age, weight)
        self.kind = kind

class Dog(Pet):
    def __init__(self, name, age, weight, kind='Dog'):
        super().__init__(name, age, weight)
        self.kind = kind

class Fish(Pet):
    def __init__(self, name, age, weight, kind='Fish'):
        super().__init__(name, age, weight)
        self.kind = kind

class Person:
    def __init__(self, full_name, age, sex):
        self.full_name = full_name
        self.age = age
        self.sex = sex

class Owner(Person):
    def __init__(self, full_name, age, sex, pets_arr=None):
        super().__init__(full_name, age, sex)
        if pets_arr is None:
            pets_arr = []
        self.pets_arr = pets_arr
    
    def add_pet(self, pet):
        self.pets_arr.append(pet)

    def remove_pet(self, pet):
        if pet in self.pets_arr:
            self.pets_arr.remove(pet)
            
    def describe_by_kind(self, kind):
        print('\nOwner:', self.full_name)
        print('Pets:')
        for pet in self.pets_arr:
            if(pet.kind == kind):
                print(f'- {pet.name}')
        
    def describe(self):
        print('\nOwner:', self.full_name)
        print('Pets:')
        for pet in self.pets_arr:
            print(f'- {pet.name}')
            
    def transfer_pet(self, *pets, target_owner):
        for pet in pets:
            if pet in self.pets_arr:
                self.pets_arr.remove(pet)
                target_owner.add_pet(pet)
                
    def __contains__(self, pet):
        print(f'\n{self.full_name} has {len(self.pets_arr)} pet(s).')        
        if pet in self.pets_arr:
            print(f'{self.full_name} has {pet.name}')
        else:
            print(f'{self.full_name} doesn`t have {pet.name}')

if __name__ == '__main__':
    
    kristie = Cat('Kristie', 3, 3)
    zhorik = Cat('Zhorik', 5, 4)
    charlie = Dog('Charlie', 5, 8)
    brovko = Dog('Brovko', 12, 10)
    petro = Fish('Petro', 1, 0.1)
    
    Sviatoslav = Owner('Sviatoslav', 18, 'M', [kristie, charlie, zhorik])
    Olena = Owner('Olena', 22, 'F', [brovko])
    
    print('\nOriginal pets of an owner')
    Sviatoslav.describe()
    
    print('\nAdded Petro the fish')
    Sviatoslav.add_pet(petro)
    Sviatoslav.describe()
    
    print('\nDeleted the fish :(')
    Sviatoslav.remove_pet(petro)  
    Sviatoslav.describe()
    
    print('\nPrints elements with similar kind argument: ')
    Sviatoslav.describe_by_kind('Cat')
    
    print('\nTransfering pets to other owner: ')
    Sviatoslav.transfer_pet(kristie, brovko, charlie, target_owner=Olena)
    Olena.describe()
    Sviatoslav.describe()

    print('\nPrints quantity of pets and checks if there are specified pet')
    Olena.__contains__(zhorik)
