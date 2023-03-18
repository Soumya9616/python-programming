#17.03.2023
#1:
'''class primium:
    def __init__(self,v_id,v_type,cost,primium_amount):
        self.__v_id=v_id
        self.__v_type=v_type
        self.__cost=cost
        self.__primium_amount=primium_amount
    def get_v_id(self):
        return self.__v_id
    def get_v_type(self):
        return self.__v_type
    def get_cost(self):
        return self.__cost
    def set_primium_amount(self):
        if(self.__v_type=="two wheeler"):
            self.__primium_amount=self.__cost*0.02
        elif(self.__v_type=="four wheeler"):
            self.__primium_amount=self.__cost*0.06
        else:
            self.__primium_amount="Invalid type"
    def get_primium_amount(self):
        return self.__primium_amount
v1=primium(201,"two wheeler",40000,0)
v1.set_primium_amount()
print(v1.get_primium_amount(),v1.get_v_id(),v1.get_v_type(),v1.get_cost(),end=" ")
print()
v2=primium(204,"four wheeler",500000,0)
v2.set_primium_amount()
print(v2.get_primium_amount(),v2.get_v_id(),v2.get_v_type(),v2.get_cost(),end=" ")'''

#2:
'''class student:
    def __init__(self,s_id,age,mark):
        self.__s_id=s_id
        self.__age=age
        self.__mark=mark
    def get_s_id(self):
        return self.__s_id
    def get_age(self):
        return self.__age
    def get_mark(self):
        return self.__mark
    def validate_mark(self):
        if(100>=self.__mark>=0):
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>=20:
            return True
        else:
            return False
    def check_qualification(self):
        if 100>=self.__mark>=65 and self.__age>=20:
            return 'qualified'
        else:
            return 'disqualified'
    def amount(self,c_id,c_amount):
        if 100>=self.__mark>=85:
                c_amount-=c_amount*0.25
                return c_amount
s1=student(100,21,90)
s2=student(101,21,101)
s3=student(102,19,75)
s4=student(103,22,50)
s1.validate_mark()
s2.validate_mark()
s3.validate_mark()
s4.validate_mark()
s1.validate_age()
s2.validate_age()
s3.validate_age()
s4.validate_age()
print(s1.check_qualification())
print(s2.check_qualification())
print(s3.check_qualification())
print(s4.check_qualification())
print(s1.amount(1001,25575.0))
print(s1.amount(1002,15500.0))'''


#3:
class Customer:
    def __init__(self,customer_name,quantity):
        self.__customer_name=customer_name
        self.__quantity=quantity
        
    def get_customer_name(self):
        return self.__customer_name
        
    def get_quantity(self):
        return self.__quantity
        
    def validate_quantity(self):
        if self.__quantity>=1 and self.__quantity<=5:
            return True
        else:
            return False


class Pizzaservice:
    counter=100
    def __init__(self,customer,pizza_type,additional_topping):
        self.__service_id=None
        self.__customer=customer
        self.__pizza_type=pizza_type
        self.__additional_topping=additional_topping
        self.pizza_cost=None
        
    def validate_pizza_type(self):
        if self.__pizza_type.lower() in ["small","medium"]:
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_pizza_type()==True and self.__customer.validate_quantity()==True:
            Pizzaservice.counter+=1
            if self.__pizza_type.lower()=="small":
                self.pizza_cost=150*self.__customer.get_quantity()
                if self.__additional_topping==True:
                    self.pizza_cost+=35*self.__customer.get_quantity()
                self.__service_id="S"+str(Pizzaservice.counter)
            if self.__pizza_type.lower()=="medium":
                self.pizza_cost=200*self.__customer.get_quantity()
                if self.__additional_topping==True:
                    self.pizza_cost+=50*self.__customer.get_quantity() 
                self.__service_id="M"+str(Pizzaservice.counter)
        else:
            self.pizza_cost=-1 
            
    def get_service_id(self):
        return self.__service_id
        
    def get_customer(self):
        return self.__customer
        
    def get_pizza_type(self):
        return self.__pizza_type
        
    def get_additional_topping(self):
        return self.__additional_topping
    
class Doordelivery(Pizzaservice):
    def __init__(self,customer,pizza_type,additional_topping,distance_in_kms):
        super().__init__(customer,pizza_type,additional_topping)
        self.__delivery_charge=0
        self.__distance_in_kms=distance_in_kms

    def get_delivery_charge(self):
        return self.__delivery_charge
        
    def get_distance_in_kms(self):
        return self.__distance_in_kms
        
    def validate_distance_in_kms(self):
        if self.__distance_in_kms>=1 and self.__distance_in_kms<=10:
            return True
        else:
            return False
    
    def calculate_pizza_cost(self):
        if self.validate_distance_in_kms():
            Pizzaservice.calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.__distance_in_kms<=5:
                    self.__delivery_charge=self.__distance_in_kms*5 
                else:
                    self.__delivery_charge=25+(self.__distance_in_kms-5)*7 
                self.pizza_cost+=self.__delivery_charge
        else:
            self.pizza_cost=-1
c1=Customer("soumya",6)
p1=Pizzaservice("soumya","small",True)
d1=Doordelivery("soumya","small",True,9)
c1.validate_quantity()
p1.validate_pizza_type()
p1.calculate_pizza_cost()
d1.validate_distance_in_kms()
print(d1.calculate_pizza_cost())
