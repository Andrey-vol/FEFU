from otree.api import *
import random
import numpy as np
from flask import Flask, request, jsonify
doc = """
Slider example
"""


class Constants(BaseConstants):
    name_in_url = "slider"
    players_per_group = None
    num_rounds = 1
    endowment = 100


class Subsession(BaseSubsession):
    pass
def creating_session(subsession:Subsession):
    for player in subsession.get_players():
        #participant = player.participant
        player.treatments = random.choice([1, 0, 2])
        



class Group(BaseGroup):
    pass


class Player(BasePlayer):
    price = models.FloatField()
    cook_wallet = models.IntegerField()
    crisp_wallet = models.IntegerField()
    nrg_wallet = models.IntegerField()

    #number = models.IntegerField()
    cook_time = models.FloatField()
    crisp_time = models.FloatField()
    nrg_time = models.FloatField()
    
    sec_price = models.FloatField()
    fin_price = models.FloatField()
    choco_wallet = models.IntegerField()
    candy_wallet = models.IntegerField()
    drink_wallet = models.IntegerField()
    #number = models.IntegerField()
    candy_time = models.FloatField()
    choco_time = models.FloatField()
    drink_time = models.FloatField()
    todrink_time = models.FloatField()
    tocrisp_time = models.FloatField()
    zad_time = models.FloatField()
    next_time = models.FloatField()
    testy_time = models.FloatField()
    coke = models.IntegerField(label="   ")
    fanta = models.IntegerField(label="   ")
    sprite = models.IntegerField(label="   ")
    pepsi = models.IntegerField(label="   ")
    lemondr = models.IntegerField(label="   ")
    persik = models.IntegerField(label="   ")
    soju = models.IntegerField(label="   ")
    lich = models.IntegerField(label="   ")
    salt = models.IntegerField(label="   ")
    crab = models.IntegerField(label="   ")
    smet = models.IntegerField(label="   ")
    cheese = models.IntegerField(label="   ")
    ny = models.IntegerField(label="   ")
    lcrab = models.IntegerField(label="   ")
    kor = models.IntegerField(label="   ")
    mr = models.IntegerField(label="   ")
    treatments = models.IntegerField()
    surprise = models.StringField(label="Какая последняя покупка Вас приятно удивила? ")
    advice = models.StringField(label="Что бы Вы посоветовали человеку, сомневающемуся в выборе товара?", 
                                choices = ['Выбрать наиболее популярный', 'Посоветовать что-то новое', 'Посоветовать тот, который нравится лично Вам'])
    neww = models.StringField(label="Как часто Вы пробуете что-то новое (среди продуктов питания)?", 
                              widget=widgets.RadioSelect, 
                              choices=[1, 2, 3, 4, 5])
    cover = models.StringField(label="Часто при продаже товаров отдельное внимание уделяется их оформлению (упаковке, подаче и т.д.), чтобы создать целостный качественный облик товара, что может повышать его цену. Как Вы считаете, насколько такой подход оправдан?  ", 
                              widget=widgets.RadioSelect, 
                              choices=[1, 2, 3, 4, 5])
    hobby = models.StringField(label="Есть ли у Вас непопулярное хобби, которое Вы бы посоветовали попробовать каждому? (Если да, то какое?)")
    impress = models.StringField(label="Существует мнение, что самое ценное в покупках – впечатления, которые мы от них получаем, а не непосредственно товары. Насколько Вы согласны с этим утверждением? ", 
                              widget=widgets.RadioSelect, 
                              choices=[1, 2, 3, 4, 5])
    lemon = models.IntegerField()
    nelemon = models.IntegerField()
    milky = models.IntegerField()
    nemilky = models.IntegerField()
    shoko = models.IntegerField()
    neshoko = models.IntegerField()
    oreyro = models.IntegerField()
    neoreyro = models.IntegerField()
    belvi = models.IntegerField()
    nebelvi = models.IntegerField()
    vanila = models.IntegerField()
    nevanila = models.IntegerField()
    moloko = models.IntegerField()
    nemoloko = models.IntegerField()
    yubiley = models.IntegerField()
    neyubiley = models.IntegerField()
    red = models.IntegerField()
    nered = models.IntegerField()
    monstr = models.IntegerField()
    nemonstr = models.IntegerField()
    gns = models.IntegerField()
    negns = models.IntegerField()
    flas = models.IntegerField()
    neflas = models.IntegerField()
    pinkl = models.IntegerField()
    nepinkl = models.IntegerField()
    sky = models.IntegerField()
    nesky = models.IntegerField()
    adrnl = models.IntegerField()
    neadrnl = models.IntegerField()
    grpom = models.IntegerField()
    negrpom = models.IntegerField()
    smetana = models.IntegerField()
    nesmetana = models.IntegerField()
    karri = models.IntegerField()
    nekarri = models.IntegerField()
    newyork = models.IntegerField()
    nenewyork = models.IntegerField()
    syr = models.IntegerField()
    nesyr = models.IntegerField()
    lacrab = models.IntegerField()
    nelacrab = models.IntegerField()
    korean = models.IntegerField()
    nekorean = models.IntegerField()
    sol = models.IntegerField()
    nesol = models.IntegerField()
    lobik = models.IntegerField()
    nelobik = models.IntegerField()
    cocacola = models.IntegerField()
    necocacola = models.IntegerField()
    pepsicola = models.IntegerField()
    nepepsicola = models.IntegerField()
    sprinter = models.IntegerField()
    nesprinter = models.IntegerField()
    fantasia = models.IntegerField()
    nefantasia = models.IntegerField()
    tonik = models.IntegerField()
    netonik = models.IntegerField()
    persia = models.IntegerField()
    nepersia = models.IntegerField()
    yougurt = models.IntegerField()
    neyougurt = models.IntegerField()
    lychee = models.IntegerField()
    nelychee = models.IntegerField()
    front = models.IntegerField()
    nefront = models.IntegerField()
    frutti = models.IntegerField()
    nefrutti = models.IntegerField()
    belka = models.IntegerField()
    nebelka = models.IntegerField()
    ledenz = models.IntegerField()
    neledenz = models.IntegerField()
    mozgwhich = models.IntegerField()
    nemozgwhich = models.IntegerField()
    JL = models.IntegerField()
    neJL = models.IntegerField()
    zitrus = models.IntegerField()
    nezitrus = models.IntegerField()
    telenok = models.IntegerField()
    netelenok = models.IntegerField()
    russia = models.IntegerField()
    nerussia = models.IntegerField()
    arahis = models.IntegerField()
    nearahis = models.IntegerField()
    slivki = models.IntegerField()
    neslivki = models.IntegerField()
    klubnika = models.IntegerField()
    neklubnika = models.IntegerField()
    alena = models.IntegerField()
    nealena = models.IntegerField()
    mindal = models.IntegerField()
    nemindal = models.IntegerField()
    yagody = models.IntegerField()
    neyagody = models.IntegerField()
    orehi = models.IntegerField()
    neorehi = models.IntegerField()
    paycheck = models.FloatField()
    offpay = models.FloatField()
    compucter_1 = models.FloatField()
    compucter_2 = models.FloatField()
    compucter_3 = models.FloatField()
    coeff_1 = models.FloatField()
    coeff_2 = models.FloatField()
    coeff_3 = models.FloatField()
    summa = models.FloatField()
    bef_pref = models.FloatField()
    after_pref = models.FloatField()
    finpay = models.FloatField()
    gender = models.StringField( label="Укажите Ваш пол", 
        choices = ['мужской', 'женский']
    )
    age = models.IntegerField(label="Укажите Ваш возраст")
    receipt = models.IntegerField(label=" Сколько в среднем рублей в день Вы тратите на продукты питания?")
    wage = models.StringField(label="Какая из приведенных ниже оценок наиболее точно характеризует материальное положение? ", 
                              choices=['денег не хватает даже на приобретение продуктов питания  ', 
                                       ' денег хватает только на приобретение продуктов питания  ', 
                                       'денег достаточно для приобретения необходимых продуктов и одежды, но на более крупные покупки приходится откладывать  ',
                                       'покупка большинства товаров длительного пользования (холодильник, телевизор) не вызывает трудностей, однако купить квартиру, машину нет возможности  ', 
                                       'денег достаточно, чтобы ни в чем себе не отказывать  '])
    phone = models.StringField(label='Укажите номер телефона, по которому мы сможем перечислить Вам вознаграждение')
    satisf = models.StringField(label=" ", 
                              widget=widgets.RadioSelect, 
                              choices=[1, 2, 3, 4, 5])
    education = models.StringField(label='Укажите Ваш уровень образования', 
                                   choices = ['Основное общее', 'Среднее общее', 'Среднее профессиональное', 'Высшее', 'Высшее со степенью'])
    
    
    
    




# PAGES

class Surveyy(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'receipt', 'wage', 'phone', 'satisf', 'education']

class Intro(Page):
    pass
     

class Cookies(Page):
    form_model = "player"
    form_fields = ["cook_time", "cook_wallet", "lemon", "nelemon", "milky", "nemilky", "shoko", "neshoko", 
                   "oreyro", "neoreyro", "belvi", "nebelvi", "vanila", "nevanila", "moloko", "nemoloko", "yubiley", "neyubiley"]

    


class Crisps(Page):
    form_model = "player"
    form_fields = ["crisp_time", "crisp_wallet", "smetana", "nesmetana", "karri", "nekarri", "lobik", "nelobik", "syr", "nesyr", 
                   "newyork", "nenewyork", "lacrab", "nelacrab", "korean", "nekorean", "sol", "nesol"]
    
    
class Energy(Page):
    form_model = "player"
    form_fields = ["nrg_time", "nrg_wallet", "red", "nered", "monstr", "nemonstr", "gns", "negns", "flas", "neflas", "sky", "nesky", "adrnl", "neadrnl", 
                   "grpom", "negrpom", "pinkl", "nepinkl"]
    
class Candy(Page):
    form_model = "player"
    form_fields = ["candy_time", "candy_wallet", "front", "nefront", "frutti", "nefrutti", "belka", "nebelka", "ledenz", "neledenz", 
                   "mozgwhich", "nemozgwhich", "JL", "neJL", "zitrus", "nezitrus", "telenok", "netelenok"]

class Chocolate(Page):
    form_model = "player"
    form_fields = ["choco_time", "choco_wallet", "russia", "nerussia", "arahis", "nearahis", "slivki", "neslivki", "klubnika", "neklubnika", 
                   "alena", "nealena", "yagody", "neyagody", "orehi", "neorehi", "mindal", "nemindal"]
    

class Drinks(Page):
    form_model = "player"
    form_fields = ["drink_time", "drink_wallet", "cocacola", "necocacola", "pepsicola", "nepepsicola", "sprinter", "nesprinter", 
                   "fantasia", "nefantasia", "persia", "nepersia", "yougurt", "neyougurt", "lychee", "nelychee", "tonik", "netonik"]




class SliderPage(Page):
    form_model = "player"
    form_fields = ["price"]



#compucter = random.uniform(0.0, 5.0)

#def set_payoffs(group):
    #p1 = group.get_player_by_id(1)
    #p2 = group.get_player_by_id(2)
    #p3 = group.get_player_by_id(3)
    #p1.payoff = group.price*5
    #p2.payoff = group.price*5
    #p3.payoff = group.price*5


class Results(Page):
    pass

    @staticmethod
    def vars_for_template(player):
        compucter = random.uniform(0.0, 0.5)
        coeff = random.uniform(-min(player.price/100, compucter), max(player.price/100, compucter))
        paycheck = round(Constants.endowment*(1+coeff))
        player.compucter_1 = round(compucter*100)
        player.coeff_1 = round(coeff*100)
        player.paycheck = paycheck
        #payoff = player.price 
        #return dict(
        #    payoff = payoff,
        #)
        
class SecondSlide(Page):
    form_model = 'player'
    form_fields = ['sec_price']

    

        
class ResultTwo(Page):
    pass

    @staticmethod
    def vars_for_template(player):
        compucter = random.uniform(0.0, 0.5)
        coeff = random.uniform(-min(player.sec_price/100, compucter), max(player.sec_price/100, compucter))
        offpay = round(Constants.endowment*(1+coeff))
        player.offpay = offpay
        player.compucter_2 = round(compucter*100)
        player.coeff_2 = round(coeff*100)
        #return player.offpay
        #payoff = player.price 
        #return dict(
        #    offpay = offpay,
        #)
        
class TwoDrink(Page):
    form_model = "player"
    form_fields = ['coke', 'lemondr', 'persik', 'fanta', 'pepsi', 'soju', 'lich', 'sprite', 'todrink_time']
    
    
class TwoCrisp(Page):
    form_model = 'player'
    form_fields = ['tocrisp_time', 'smet', 'crab', 'kor', 'salt', 'lcrab', 'ny', 'mr', 'cheese']
    
class Trial(Page):
    @staticmethod
    def is_displayed(player):
        return player.treatments == 1
    form_model = "player"
    form_fields=['surprise', 'advice', 'neww', 'cover', 'hobby', 'impress']
    
class Zadachka(Page):
    @staticmethod
    def is_displayed(player):
        return player.treatments == 2
    form_model = "player"
    form_fields=['zad_time']

class NextPage(Page):
    @staticmethod
    def is_displayed(player):
        return player.treatments == 2
    form_model = "player"
    form_fields=['next_time']
    
class Testy(Page):
    @staticmethod
    def is_displayed(player):
        return player.treatments == 1
    form_model = "player"
    form_fields=['testy_time']

class FinalSlide(Page):
    form_model = 'player'
    form_fields = ['fin_price']
    @staticmethod
    def vars_for_template(player):
        paycheck = player.paycheck
        offpay = player.offpay
        summa = paycheck + offpay
        player.summa = summa
        
    
class FinResult(Page):
    pass
    @staticmethod
    def vars_for_template(player):
        compucter = random.uniform(0.0, 0.5)
        coeff = random.uniform(-min(player.fin_price/100, compucter), max(player.fin_price/100, compucter))
        paycheck = player.paycheck
        offpay = player.offpay
        summa = paycheck + offpay
        finpay = round(summa*(1+coeff))
        player.compucter_3 = round(compucter*100)
        player.coeff_3 = round(coeff*100)
        #payoff = player.price 
        player.finpay = finpay

class BefPref(Page):
    form_model = 'player'
    form_fields = ['bef_pref'] 
    
class AfterPref(Page):
    form_model = 'player'
    form_fields = ['after_pref']

########## 


page_sequence = [ Intro, Chocolate, Energy, Crisps, BefPref, SliderPage,  Results, Trial, Zadachka, NextPage, Testy, Drinks, Candy,  Cookies, AfterPref, SecondSlide, ResultTwo, TwoDrink, TwoCrisp, FinalSlide, FinResult, Surveyy]