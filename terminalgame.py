#inserted modules here
import random

#The Eu class represeting all EU country objects
class Eu_country:
    continent = "Europe"
    options_pop = []
    options_main = []
    options_mainpop = []
    options_index = []
    
    def __init__(self, name, population, main_city, mc_population, happiness_index = 0):
        self.name = name
        self.population = population
        self.main_city = main_city
        self.mc_population = mc_population
        self.happiness = happiness_index
        Eu_country.country_count += 1
        self.id = Eu_country.country_count

    def __repr__(self):
        message = "The {country} has population of {population} people. The main city is {city} and has population of {mc_pop} people.".format(country = self.name, population = self.population, city = self.main_city, mc_pop = self.mc_population, index = self.happiness)
        if self.happiness > 0:
            message += " The latest index of happiness for {country} is {index}.".format(country = self.name, index = self.happiness)
        else:
            message += " The happiness index of {country} is not currently known.".format(country = self.name)
        return message
    
    def options(self, country):
        option1 = 
    


#The countries from EU with their respective variables
albania = Eu_country("Albania", "2 791 765", "Tirana", "418 495", 5.304)
andorra = Eu_country("Andorra", "81 938", "Andorra la Vella", "24 042")
austria = Eu_country("Austria", "9 120 813", "Vienna", "2 014 614", 6.905)
belarus = Eu_country("Belarus", "9 056 696", "Minsk", "1 992 862", 5.82)
belgium = Eu_country("Belgium", "11 738 763", "Brussels", "1 249 597", 6.894)
bosnia_and_herzegovina = Eu_country("Bosnia and Herzegovina", "3 164 253", "Sarajevo", "275524", 5.877)
bulgaria = Eu_country("Bulgaria", "6 757 689", "Sofia", "1 236 000", 5.463)
croatia = Eu_country("Croatia", "3 875 325", "Zagreb", "806 341", 5.882)
czech_republic = Eu_country("Czech Republic", "10 735 859", "Prague", "1 309 000", 6.822)
denmark = Eu_country("Denmark", "5 977 412", "Copenhagen", "602 481", 7.583)
estonia = Eu_country("Estonia", "1 360 546", "Tallinn", "394 024", 6.448)
finland = Eu_country("Finland", "5 617 310", "Helsinky", "658 864", 7.741)
france = Eu_country("France", "66 548 530", "Paris", "2 138 551", 6.610)
germany = Eu_country("Germany", "84 552 242", "Berlin", "3 426 354", 6.720)
greece = Eu_country("Greece", "10 047 817", "Athens", "664 046", 5.934)
holy_see = Eu_country("Holy See", "764", "Vatican", "764")
hungary = Eu_country("Hungary", "9 676 135", "Budapest", "1 741 041", 6.017)
iceland = Eu_country("Iceland", "5 255 017", "Rejkjavik", "118 918", 7.525)
ireland = Eu_country("Ireland", "5 255 017", "Dublin", "1 024 027", 6.838)
italy = Eu_country("Italy", "59 342 867", "Rome", "2 318 895", 6.324)
latvia = Eu_country("Latvia", "1 871 871", "Riga", "742 572", 6.235)
liechtenstein = Eu_country("Liechtenstein", "39 870", "Vaduz", "5 450")
lithuania = Eu_country("Lithuania", "2 859 110", "Vilnius", "542 366", 6.818)
luxembourg = Eu_country("Luxembourg", "673 036", "Luxembourg", "76 684", 7.122)
malta = Eu_country("Malta", "539 607", "San Pawl il-Bahar", "32 042", 6.346)
moldova = Eu_country("Moldova", "3 034 961", "Chisinau", "635 994", 5.816)
monaco = Eu_country("Monaco", "38 631", "Monaco-Ville", "975")
montenegro = Eu_country("Montenegro", "638 479", "Podgorica", "236 852", 5.707)
netherlands = Eu_country("Netherlands", "18 228 742", "Amsterdam", "741 636", 7.319)
north_macedonia = Eu_country("North Macedonia", "1 823 009", "Skopje", "474 889", 5.369)
norway = Eu_country("Norway", "5 576 660", "Oslo", "580 000", 7.302)
poland = Eu_country("Poland", "38 539 201", "Warsaw", "1 702 139", 6.442)
portugal = Eu_country("Portugal", "10 425 292", "Lisbon", "517 802", 6.030)
romania = Eu_country("Romania", "19 015 088", "Bucharest", "1 877 155", 6.491)
russia = Eu_country("Russia", "144 820 423", "Moscow", "10 381 222", 5.785)
san_marino = Eu_country("San Marino", "33 581", "San Marino", 4040)
serbia = Eu_country("Serbia", "6 736 216", "Belgrade", "1 273 651", 6.411)
slovakia = Eu_country("Slovakia", "5 506 760", "Bratislava", "423 737", 6.257)
slovenia = Eu_country("Slovenia", "2 118 697", "Ljubljana", "272 220", 6.743)
spain = Eu_country("Spain", "47 910 526", "Madrid", "3 255 944", 6.421)
sweden = Eu_country("Sweden", "10 606 999", "Stockholm", "1 515 017", 7.344)
switzerland = Eu_country("Switzerland", "8 921 981", "Zurich", "341 730", 7.060)
ukraine = Eu_country("Ukraine", "37 860 221", "Kyiv", "2 797 553", 4.873)
united_kingdom = Eu_country("United Kingdom", "69 138 192", "London", "8 961 989", 6.749)

correct_answers = 0
wrong_answers = 0

def questions(country):
    global correct_answers
    global wrong_answers
    answer1 = input("What is +- 20% the population of {country}? Guess the number and press enter.\n".format(country = country.name))
    if int(answer1) > (country.population * 0.90) and int(answer1) < (country.population * 1.1):
        correct_answers += 1
        print("Yes that is pretty accurate, the population of {country} is {population} and you guessed {guess}".format(country = country.name, population = country.population, guess = str(answer1)))
    elif int(answer1) > (country.population * 0.8) and int(answer1) < (country.population * 1.2):        
        print("Yes, close enough! The population of {country} is {population} and you guessed {guess}".format(country = country.name, population = country.population, guess = str(answer1)))
        correct_answers += 1
    else:
        print("That is a worng answer, the population of {country} is {population} and you guessed {guess}".format(country = country.name, population = country.population, guess = str(answer1)))
        wrong_answers += 1
    answer2 = input("What is the main city of {country}? Guess the name and press enter.\n".format(country = country.name))
    if answer2 == country.main_city:
        correct_answers += 1
        print("Yes that is correct! The main city of {country} is {city}!".format(country = country.name, city = country.main_city))
    else:
        wrong_answers += 1
        print("That is not right, the main city of {country} is {city}.".format(country = country.name, city = country.main_city))
    answer3 = input("What is +- 40% the population of {city} the main city of {country}?. Guess the number and press enter.\n".format(city = country.main_city, country = country.name))
    if int(answer3) > (country.mc_population * 0.80) and int(answer3) < (country.mc_population * 1.2):
        correct_answers += 1
        print("Yes that is pretty accurate, the population of {city} the main city of {country} is {mcpop} and you guessed {guess}.".format(city = country.main_city, country = country.name, mcpop = country.mc_population, guess = str(answer3)))
    elif int(answer3) > (country.mc_population * 0.60) and int(answer3) < (country.mc_population * 1.4):
        correct_answers += 1
        print("Yes close enough, the population of {city} the main city of {country} is {mcpop} and you guessed {guess}.".format(city = country.main_city, country = country.name, mcpop = country.mc_population, guess = str(answer3)))
    else:
        wrong_answers += 1
        print("No that is a wrong answer, the population of {city} the main city of {country} is {mcpop} and you guessed {guess}.".format(city = country.main_city, country = country.name, mcpop = country.mc_population, guess = str(answer3)))
    if country.happiness > 0:
        answer4 = input("Now tell me, what is the latest known happiness index for {country} from 0-10. Guess the number and press enter.\n".format(country = country.name))
        if float(answer4) > (country.happiness - 0.5) and float(answer4) < (country.happiness + 0.5):
            correct_answers += 1
            print("That is close enough, the latest known happiness index for {country} is {index} and you guessed {guess}.".format(country = country.name, index = country.happiness, guess = str(answer4)))
        else:
            wrong_answers += 1
            print("That is wrong, the latest known happiness index for {country} is {index} and you guessed {guess}.".format(country = country.name, index = country.happiness, guess = str(answer4)))
    total_answers = correct_answers + wrong_answers
    correct_percentage = correct_answers / (total_answers * 0.01)
    print("You have answered {number} questions with a {percent}% of correct answers until now, keep it up!".format(number = str(total_answers), percent = str(correct_percentage)))       



list_of_countries = [albania, andorra, austria, belarus, belgium, bosnia_and_herzegovina, bulgaria, croatia, czech_republic, denmark, \
                    estonia, finland, france, germany, greece, holy_see, hungary, iceland, ireland, italy, latvia, liechtenstein, \
                    lithuania, luxembourg, malta, moldova, monaco, montenegro, netherlands, north_macedonia, norway, poland, portugal, \
                    romania, russia, san_marino, serbia, slovakia, slovenia, spain, sweden, switzerland, ukraine, united_kingdom]
def quiz():
    global correct_answers
    global wrong_answers
    while len(list_of_countries) > 24:
        random_country = random.choice(list_of_countries)
        list_of_countries.remove(random_country)
        questions(random_country)
    total_answers = correct_answers + wrong_answers
    correct_percentage = correct_answers / (total_answers * 0.01)
    message = "And that is it for the quiz!"
    if correct_percentage > 90:
        message += " SUCH A BRANIAC! Congratulations, you have succesfully filled your head with useless information, hope you are proud of yourself."
    elif correct_percentage > 75:
        message += " You did pretty well! Consider redoing the quiz couple more times for better results. Keep up the good work."
    elif correct_percentage > 50:
        message += " Not bad, but not good either, practice buddy."
    else:
        message += " Well, you better be good at something else with this kind of \"knowledge\"."
    print(message)
    
print("Welcome! its time for a QUIZ!")
quiz()