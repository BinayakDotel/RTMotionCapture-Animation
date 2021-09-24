import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

class FirebaseAccess:
    def __init__(self):
        self.cred = credentials.Certificate("Resources/Key.json")
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://word-search-aed56-default-rtdb.europe-west1.firebasedatabase.app/'
        })
        self.reference = db.reference('GameData')

    def SendCategory(self):
        print("send")
        self.reference.child('Categories').set({
            '0': {
                'isVisible': True,
                'name': "Animals"
            },
            '1': {
                'isVisible': True,
                'name': "Clothes"
            },
            '2': {
                'isVisible': True,
                'name': "Colours"
            },
            '3': {
                'isVisible': True,
                'name': "Fruits"
            },
            '4': {
                'isVisible': True,
                'name': "Foods"
            },
            '5': {
                'isVisible': True,
                'name': "Brands"
            },
            '6': {
                'isVisible': True,
                'name': "Sports"
            },
            '7': {
                'isVisible': True,
                'name': "Trees"
            },
            '8': {
                'isVisible': True,
                'name': "Plants"
            },
            '9': {
                'isVisible': True,
                'name': "Flowers"
            },
            '10': {
                'isVisible': True,
                'name': "Aquatic"
            },
            '11': {
                'isVisible': True,
                'name': "Mountains"
            },
            '12': {
                'isVisible': True,
                'name': "Rivers"
            },
            '13': {
                'isVisible': True,
                'name': "Birds"
            },
            '14': {
                'isVisible': True,
                'name': "Computers"
            },
            '15': {
                'isVisible': True,
                'name': "Movies"
            },
            '16': {
                'isVisible': True,
                'name': "Names"
            },
            '17': {
                'isVisible': True,
                'name': "Mathematics"
            },
            '18': {
                'isVisible': True,
                'name': "Languages"
            },
            '19': {
                'isVisible': False,
                'name': "celebrities"
            },
        })
        print("success")
    '''def SendData(self, joints, x, y, z):
        branch = self.reference.child(joints)
        branch.update({
                'x': x,
                'y': y,
                'z': z
        })
        self.reference.set({
            "LEFT_HIP":{
                "x": 0.2,
                "y": 0.2,
                "z": 0.3
            },
            "RIGHT_HIP":{
                "x": 0.2,
                "y": 0.2,
                "z": 0.3
            },
            "LEFT_KNEE":{
                "x": 0.2,
                "y": 0.2,
                "z": 0.3
            },
            "RIGHT_KNEE":{
                "x": 0.2,
                "y": 0.2,
                "z": 0.3
            },
            "LEFT_ANKLE":{
                "x": 0.2,
                "y": 0.2,
                "z": 0.3
            },
            "RIGHT_ANKLE":{
                "x": 0.2,
                "y": 0.2,
                "z": 0.3
            }
        })'''
    def SendWords(self):
        self.reference.child("words/Categories").set({
            "Animals": {
                '0': {
                    'difficulty': "easy",
                    'name': "lion"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "cow"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "dog"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "cat"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "rat"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "hare"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "deer"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "mule"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "bear"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "wolf"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "fox"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "bat"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "pig"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "goat"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "puma"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "seal"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "yak"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "mole"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "elk"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "bull"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "carp"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "dodo"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "frog"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "toad"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "kudu"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "lynx"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "mink"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "olm"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "pika"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "pug"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "hawk"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "cub"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "calf"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "colt"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "mare"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "foal"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "buck"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "ewe"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "ainu"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "zebu"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "bobcat"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "baboon"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "camel"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "koala"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "ferret"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "panda"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "rhino"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "hyena"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "skunk"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "zebra"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "tiger"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "jackal"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "mouse"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "moose"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "rabbit"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "buffalo"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "civet"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "akita"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "camel"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "badger"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "beago"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "beagle"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "beaski"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "boggle"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "borkie"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "caiman"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "corkie"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "coyote"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "dunker"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "donkey"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "monkey"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "jaguar"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "hamster"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "snake"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "lizard"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "anteater"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "aurochs"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "dolphin"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "gorilla"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "alligator"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "caracal"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "cavador"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "capybara"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "cavapoo"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "cheagle"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "cheetah"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "crocodile"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "elephant"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "eskipoo"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "frengle"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "gharial"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "giraffe"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "gorilla"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "rhinoceros"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "kangaroo"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "keeshond"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "pyrador"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "raccoon"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "quokka"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "reindeer"
                }
            },
            "Colours": {
                '0': {
                    'difficulty': "easy",
                    'name': "areo"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "blue"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "red"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "pink"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "ruby"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "ao"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "aqua"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "lime"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "gray"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "bole"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "bone"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "rose"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "buff"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "corn"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "cyan"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "dark"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "lava"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "sky"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "ecru"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "erin"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "fawn"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "flax"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "tan"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "navy"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "gold"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "teal"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "dim"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "snow"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "lace"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "sand"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "oat"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "itte"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "fire"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "corn"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "rust"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "clay"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "yam"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "wine"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "plum"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "iris"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "green"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "violet"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "orange"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "almond"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "purple"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "amazon"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "amber"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "brass"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "bronze"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "brown"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "white"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "yellow"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "azure"
                },
                '53': {
                    'difficulty': "medium",
                    'name': "powder"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "mania"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "beaver"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "beige"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "lemon"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "coffee"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "olive"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "blond"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "blood"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "bluish"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "yonder"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "crimson"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "maroon"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "camel"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "chrome"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "citron"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "copper"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "indigo"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "brandy"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "flame"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "light"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "wooden"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "fulvous"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "fuchsia"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "frostbite"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "raspberry"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "firebrick"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "reddish"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "ferngreen"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "etonblue"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "lavender"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "eminence"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "emerald"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "eggplant"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "dukeblue"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "cyclemen"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "cinnabar"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "cinereous"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "chocolate"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "chestnut"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "champagne"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "catawba"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "byzantine"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "magenta"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "byzantium"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "eggshell"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "eigengrau"
                }
            },
            "Fruits": {
                    '0': {
                        'difficulty': "easy",
                        'name': "fig"
                    },
                    '1': {
                        'difficulty': "easy",
                        'name': "plum"
                    },
                    '2': {
                        'difficulty': "easy",
                        'name': "kiwi"
                    },
                    '3': {
                        'difficulty': "easy",
                        'name': "lime"
                    },
                    '4': {
                        'difficulty': "easy",
                        'name': "pear"
                    },
                    '5': {
                        'difficulty': "easy",
                        'name': "yuzu"
                    },
                    '6': {
                        'difficulty': "easy",
                        'name': "pine"
                    },
                    '7': {
                        'difficulty': "easy",
                        'name': "nut"
                    },
                    '8': {
                        'difficulty': "easy",
                        'name': "palm"
                    },
                    '9': {
                        'difficulty': "easy",
                        'name': "monk"
                    },
                    '10': {
                        'difficulty': "easy",
                        'name': "cran"
                    },
                    '11': {
                        'difficulty': "easy",
                        'name': "ugli"
                    },
                    '12': {
                        'difficulty': "easy",
                        'name': "imbe"
                    },
                    '13': {
                        'difficulty': "easy",
                        'name': "ugni"
                    },
                    '14': {
                        'difficulty': "easy",
                        'name': "bean"
                    },
                    '15': {
                        'difficulty': "easy",
                        'name': "bay"
                    },
                    '16': {
                        'difficulty': "easy",
                        'name': "mio"
                    },
                    '17': {
                        'difficulty': "easy",
                        'name': "peri"
                    },
                    '18': {
                        'difficulty': "easy",
                        'name': "mora"
                    },
                    '19': {
                        'difficulty': "easy",
                        'name': "pom"
                    },
                    '20': {
                        'difficulty': "easy",
                        'name': "idra"
                    },
                    '21': {
                        'difficulty': "easy",
                        'name': "anzu"
                    },
                    '22': {
                        'difficulty': "easy",
                        'name': "date"
                    },
                    '23': {
                        'difficulty': "easy",
                        'name': "emu"
                    },
                    '24': {
                        'difficulty': "easy",
                        'name': "abiu"
                    },
                    '25': {
                        'difficulty': "easy",
                        'name': "acai"
                    },
                    '26': {
                        'difficulty': "easy",
                        'name': "bael"
                    },
                    '27': {
                        'difficulty': "easy",
                        'name': "duku"
                    },
                    '28': {
                        'difficulty': "easy",
                        'name': "coco"
                    },
                    '29': {
                        'difficulty': "easy",
                        'name': "neem"
                    },
                    '30': {
                        'difficulty': "easy",
                        'name': "nere"
                    },
                    '31': {
                        'difficulty': "easy",
                        'name': "dote"
                    },
                    '32': {
                        'difficulty': "easy",
                        'name': "bing"
                    },
                    '33': {
                        'difficulty': "easy",
                        'name': "fugi"
                    },
                    '34': {
                        'difficulty': "easy",
                        'name': "pea"
                    },
                    '35': {
                        'difficulty': "easy",
                        'name': "clay"
                    },
                    '36': {
                        'difficulty': "easy",
                        'name': "yam"
                    },
                    '37': {
                        'difficulty': "easy",
                        'name': "wine"
                    },
                    '38': {
                        'difficulty': "easy",
                        'name': "plum"
                    },
                    '39': {
                        'difficulty': "easy",
                        'name': "leek"
                    },
                    '40': {
                        'difficulty': "medium",
                        'name': "apple"
                    },
                    '41': {
                        'difficulty': "medium",
                        'name': "orange"
                    },
                    '42': {
                        'difficulty': "medium",
                        'name': "grapes"
                    },
                    '43': {
                        'difficulty': "medium",
                        'name': "mango"
                    },
                    '44': {
                        'difficulty': "medium",
                        'name': "ackee"
                    },
                    '45': {
                        'difficulty': "medium",
                        'name': "arhat"
                    },
                    '46': {
                        'difficulty': "medium",
                        'name': "cherry"
                    },
                    '47': {
                        'difficulty': "medium",
                        'name': "araza"
                    },
                    '48': {
                        'difficulty': "medium",
                        'name': "aprium"
                    },
                    '49': {
                        'difficulty': "medium",
                        'name': "banana"
                    },
                    '50': {
                        'difficulty': "medium",
                        'name': "cherry"
                    },
                    '51': {
                        'difficulty': "medium",
                        'name': "babaco"
                    },
                    '52': {
                        'difficulty': "medium",
                        'name': "berry"
                    },

                    '53': {
                        'difficulty': "medium",
                        'name': "damson"
                    },
                    '54': {
                        'difficulty': "medium",
                        'name': "feijoa"
                    },
                    '55': {
                        'difficulty': "medium",
                        'name': "almond"
                    },
                    '56': {
                        'difficulty': "medium",
                        'name': "genip"
                    },
                    '57': {
                        'difficulty': "medium",
                        'name': "jelly"
                    },
                    '58': {
                        'difficulty': "medium",
                        'name': "kapok"
                    },

                    '59': {
                        'difficulty': "medium",
                        'name': "huito"
                    },
                    '60': {
                        'difficulty': "medium",
                        'name': "jujube"
                    },
                    '61': {
                        'difficulty': "medium",
                        'name': "jocote"
                    },
                    '62': {
                        'difficulty': "medium",
                        'name': "kabosu"
                    },
                    '63': {
                        'difficulty': "medium",
                        'name': "korian"
                    },
                    '64': {
                        'difficulty': "medium",
                        'name': "kepel"
                    },

                    '65': {
                        'difficulty': "medium",
                        'name': "keule"
                    },
                    '66': {
                        'difficulty': "medium",
                        'name': "kutjera"
                    },
                    '67': {
                        'difficulty': "medium",
                        'name': "lablab"
                    },
                    '68': {
                        'difficulty': "medium",
                        'name': "lapsi"
                    },
                    '69': {
                        'difficulty': "medium",
                        'name': "lemato"
                    },
                    '70': {
                        'difficulty': "medium",
                        'name': "lemon"
                    },
                    '71': {
                        'difficulty': "medium",
                        'name': "marula"
                    },
                    '72': {
                        'difficulty': "medium",
                        'name': "olive"
                    },
                    '73': {
                        'difficulty': "medium",
                        'name': "papaya"
                    },
                    '74': {
                        'difficulty': "medium",
                        'name': "peach"
                    },
                    '75': {
                        'difficulty': "hard",
                        'name': "pears"
                    },
                    '76': {
                        'difficulty': "hard",
                        'name': "pluot"
                    },
                    '77': {
                        'difficulty': "hard",
                        'name': "safou"
                    },
                    '78': {
                        'difficulty': "hard",
                        'name': "santol"
                    },
                    '79': {
                        'difficulty': "hard",
                        'name': "tangor"
                    },
                    '80': {
                        'difficulty': "hard",
                        'name': "tomato"
                    },
                    '81': {
                        'difficulty': "hard",
                        'name': "vanilla"
                    },
                    '82': {
                        'difficulty': "hard",
                        'name': "walnut"
                    },
                    '83': {
                        'difficulty': "hard",
                        'name': "apricot"
                    },
                    '84': {
                        'difficulty': "hard",
                        'name': "avocado"
                    },
                    '85': {
                        'difficulty': "hard",
                        'name': "aceroia"
                    },
                    '86': {
                        'difficulty': "hard",
                        'name': "cucumber"
                    },
                    '87': {
                        'difficulty': "hard",
                        'name': "raspberry"
                    },
                    '88': {
                        'difficulty': "hard",
                        'name': "atemoya"
                    },
                    '89': {
                        'difficulty': "hard",
                        'name': "bayberry"
                    },
                    '90': {
                        'difficulty': "hard",
                        'name': "blueberry"
                    },
                    '91': {
                        'difficulty': "hard",
                        'name': "blackberry"
                    },
                    '92': {
                        'difficulty': "hard",
                        'name': "bearberry"
                    },
                    '93': {
                        'difficulty': "hard",
                        'name': "bilberry"
                    },
                    '94': {
                        'difficulty': "hard",
                        'name': "bayberry"
                    },
                    '95': {
                        'difficulty': "hard",
                        'name': "bramble"
                    },
                    '96': {
                        'difficulty': "hard",
                        'name': "cranberry"
                    },
                    '97': {
                        'difficulty': "hard",
                        'name': "cocoplum"
                    },
                    '98': {
                        'difficulty': "hard",
                        'name': "coconut"
                    },
                    '99': {
                        'difficulty': "hard",
                        'name': "jackfruit"
                    }
                },
            "Clothes": {
                '0': {
                    'difficulty': "easy",
                    'name': "alb"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "aba"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "boa"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "box"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "cap"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "fez"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "fig"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "fur"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "hat"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "kit"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "lid"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "mac"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "mob"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "obi"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "tam"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "tee"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "tie"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "top"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "wig"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "agal"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "bags"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "baju"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "barb"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "belt"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "boot"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "busk"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "cack"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "cape"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "cest"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "clog"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "coat"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "cope"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "cowl"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "mask"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "hood"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "sari"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "shoe"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "suit"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "vest"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "tie"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "abnet"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "acton"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "aglet"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "amice"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "apron"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "armet"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "array"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "bands"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "blues"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "jeans"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "cardi"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "chaps"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "crown"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "dress"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "ducks"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "gloves"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "jupon"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "lammy"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "levis"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "lungi"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "nappy"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "pants"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "skirt"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "sagum"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "socks"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "finery"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "costume"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "anklet"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "arctic"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "barret"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "blazer"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "boater"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "jacket"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "jersey"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "jumper"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "apparel"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "baboosh"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "baggies"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "baldric"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "bandana"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "barbour"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "chiphat"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "coronet"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "garment"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "hairpin"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "pyjamas"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "shalwar"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "slippers"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "baldrick"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "basquine"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "bloomers"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "bootlace"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "breeches"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "burgonet"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "capalline"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "crinoline"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "fleshings"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "sleepsuit"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "trousers"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "miniskirt"
                }
            },
            "Foods": {
                '0': {
                    'difficulty': "easy",
                    'name': "egg"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "curd"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "ice"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "fish"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "meat"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "ham"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "soup"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "momo"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "rice"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "corn"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "parm"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "crab"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "beef"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "pork"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "nuts"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "seed"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "dips"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "pies"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "tots"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "bean"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "ribs"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "stew"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "roti"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "wine"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "beer"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "cake"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "bake"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "beet"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "bowl"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "bran"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "buns"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "chew"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "clam"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "diet"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "feed"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "fork"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "kiwi"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "lime"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "nut"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "milk"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "apple"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "bacon"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "berry"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "beans"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "bread"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "broil"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "candy"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "chili"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "cream"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "curry"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "dairy"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "dried"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "flour"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "grains"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "guava"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "lemon"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "pizza"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "salad"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "roast"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "toast"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "cheese"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "crunch"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "garlic"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "mutton"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "spices"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "hunger"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "walnut"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "yogurt"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "toffee"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "tomato"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "potato"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "cereal"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "butter"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "curry"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "muffin"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "biscuit"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "calorie"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "caramel"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "chicken"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "cupcake"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "dessert"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "custard"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "freezer"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "mustard"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "noodles"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "popcorn"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "vanilla"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "vitamin"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "cucumber"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "milkshake"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "hamburger"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "zucchini"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "turmeric"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "lollipop"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "macaroni"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "minerals"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "crackers"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "ketchup"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "nourish"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "utensils"
                }
            },
            "Brands": {
                '0': {
                    'difficulty': "easy",
                    'name': "ikea"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "irke"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "nasa"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "oreo"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "dell"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "visa"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "nike"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "lego"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "fila"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "puma"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "juul"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "ebay"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "vans"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "basf"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "sony"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "vaio"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "avis"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "uber"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "lyft"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "ford"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "jeep"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "xbox"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "sega"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "asus"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "acer"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "oppo"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "nike"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "jio"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "ufc"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "dior"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "elle"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "lays"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "ritz"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "mars"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "line"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "mtv"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "bbc"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "milo"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "kfc"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "snap"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "honoly"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "gozzby"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "anetly"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "hamofy"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "biverty"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "facebook"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "adidas"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "apple"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "pepsi"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "rolex"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "bentley"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "cristal"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "lexus"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "lincoln"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "gucci"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "jaguar"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "honda"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "toyota"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "amazon"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "prime"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "google"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "titan"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "disney"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "tesla"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "cisco"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "pixar"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "disney"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "canon"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "loreal"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "nestle"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "adobe"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "huawei"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "xiaomi"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "realme"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "xerox"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "microsoft"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "samsung"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "mercedes"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "gillette"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "pampers"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "hyundai"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "philips"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "porsche"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "starbucks"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "panasonic"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "discovery"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "burberry"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "heineken"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "ferrari"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "linkedin"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "nintendo"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "hennessy"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "colgate"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "kelloggs"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "spotify"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "netflix"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "danone"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "youtube"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "alphabet"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "mitsubishi"
                }
            },
            "Sports": {
                '0': {
                    'difficulty': "easy",
                    'name': "ball"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "dibs"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "clob"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "faro"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "ispy"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "crib"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "dice"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "golf"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "grab"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "jass"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "judo"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "klob"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "ludo"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "mora"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "polo"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "pool"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "snap"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "sumo"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "vint"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "card"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "pit"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "rum"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "pan"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "tig"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "taw"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "tag"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "indy"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "ski"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "skat"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "race"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "goal"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "foul"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "dunk"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "sack"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "runs"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "bull"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "duck"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "putt"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "ruff"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "brag"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "chess"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "bingo"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "cinch"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "comet"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "halma"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "jacks"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "lotto"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "monte"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "rally"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "rodeo"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "rules"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "rummy"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "yukon"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "boxing"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "casino"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "caving"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "driving"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "racing"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "flying"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "hazard"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "hockey"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "karata"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "kungfu"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "pokino"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "riding"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "skiing"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "tennis"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "soccer"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "sevens"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "chemmy"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "squash"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "yablon"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "trumps"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "banker"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "aikido"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "archery"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "badminton"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "bowling"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "skydiving"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "cricket"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "cycling"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "solitaire"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "wrestling"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "karting"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "lottery"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "marbles"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "netball"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "football"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "swimming"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "pinball"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "rackets"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "skating"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "snooker"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "baseball"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "climbing"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "monopoly"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "handball"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "highjump"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "pingpong"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "shooting"
                }
            },
            "Trees": {
                '0': {
                    'difficulty': "easy",
                    'name': "acer"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "anil"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "coca"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "coco"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "crab"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "date"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "hule"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "ilex"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "kava"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "khat"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "kola"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "lime"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "ling"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "neem"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "nim"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "nipa"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "palm"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "pear"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "pine"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "plum"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "rimu"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "sorb"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "teak"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "upas"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "bay"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "ben"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "box"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "elm"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "kat"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "oak"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "sal"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "tea"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "yew"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "ivy"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "alba"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "whin"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "may"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "wych"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "fig"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "alba"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "apple"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "aspen"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "balsa"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "beech"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "birch"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "broom"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "cacao"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "cedar"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "elder"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "erica"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "fagus"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "gorse"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "guava"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "hazel"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "holly"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "kokum"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "larch"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "lemon"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "levis"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "lilac"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "mango"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "olive"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "peach"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "papaw"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "rowan"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "saman"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "sapan"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "thuya"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "yapon"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "zaman"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "almond"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "sallow"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "pawpaw"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "locust"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "laurel"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "apricot"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "amboyna"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "avocado"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "bigtree"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "bluegum"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "bramble"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "buckeye"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "dogwood"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "jasmine"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "redwood"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "barberry"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "basewood"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "hornbeam"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "ironwood"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "quandang"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "raintree"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "tamarisk"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "cherimoya"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "flametree"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "hackberry"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "kauripine"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "stonepine"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "sweetwood"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "whitebeam"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "sassafras"
                }
            },
            "Plants": {
                '0': {
                    'difficulty': "easy",
                    'name': "bay"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "box"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "cos"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "ers"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "hop"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "ivy"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "kat"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "nep"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "oat"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "pea"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "pia"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "poa"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "rue"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "rye"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "seg"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "tef"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "yam"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "zea"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "alfa"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "alga"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "aloe"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "anil"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "arum"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "bean"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "beet"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "bent"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "corn"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "dill"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "diss"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "fern"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "herb"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "neem"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "jute"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "leek"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "mint"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "oats"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "poke"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "leaf"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "root"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "reed"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "agave"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "ajuga"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "alang"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "alder"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "anise"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "avens"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "basil"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "blite"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "brake"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "broom"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "cacti"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "chara"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "clote"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "clove"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "couch"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "dicot"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "swale"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "grass"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "henna"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "maize"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "orris"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "paddy"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "rubus"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "solar"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "barley"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "wheat"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "short"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "wrack"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "yeast"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "bamboo"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "cactus"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "carrot"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "cotton"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "fungus"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "garlic"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "absinth"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "aconite"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "alecost"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "alkanet"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "amanite"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "bramble"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "bulbule"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "cabbage"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "creeper"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "cytisus"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "foxtail"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "mangold"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "mustard"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "pumpkin"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "saffron"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "seaweed"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "spinach"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "brooklime"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "butterbur"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "chinaroot"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "fenugreek"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "goldenrod"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "greenweed"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "groundnut"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "liverwort"
                }
            },
            "Flowers": {
                '0': {
                    'difficulty': "easy",
                    'name': "arum"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "dock"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "flag"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "geum"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "iris"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "ixia"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "lily"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "ling"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "ling"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "lote"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "musk"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "pink"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "rose"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "tare"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "aloe"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "date"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "root"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "pear"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "stem"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "leaf"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "fig"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "ivy"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "lent"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "reed"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "rue"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "sage"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "uva"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "uris"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "urn"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "ulex"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "woad"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "yew"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "yam"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "oat"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "pia"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "poa"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "rye"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "zea"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "hop"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "bay"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "aster"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "bloom"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "bugle"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "clary"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "erica"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "lilac"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "lotus"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "lupin"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "orpin"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "poppy"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "stock"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "tansy"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "tulip"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "vinca"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "viola"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "abelia"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "bellis"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "clover"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "cosmea"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "iberis"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "nuphar"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "orchid"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "orchis"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "salvia"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "squill"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "violet"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "yarrow"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "zinnia"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "thrift"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "paeony"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "paigle"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "scrilla"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "tutsan"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "sprrel"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "oxeye"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "aconite"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "alkaner"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "alussum"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "anchusa"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "bartsia"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "begonia"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "buckeye"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "blewart"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "bugloss"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "calluna"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "campion"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "cudweed"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "frogbit"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "fuchsia"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "heather"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "jasmine"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "jassamy"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "kingcup"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "lynchnis"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "melifoil"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "waterlily"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "rosebay"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "lavendar"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "marigold"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "sunflower"
                }
            },
            "Aquatic": {
                '0': {
                    'difficulty': "easy",
                    'name': "cod"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "dab"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "eel"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "gar"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "ged"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "bib"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "ide"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "par"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "ray"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "roe"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "sar"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "tai"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "fish"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "seal"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "opus"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "mink"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "gill"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "fins"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "barb"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "chub"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "clam"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "loch"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "moth"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "loaf"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "rush"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "reed"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "alga"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "acta"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "aqua"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "boat"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "ship"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "skis"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "sea"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "bugs"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "mary"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "hare"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "ater"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "worm"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "flea"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "sea"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "otter"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "steal"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "seals"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "shoal"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "coral"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "hippo"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "trout"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "prawn"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "manta"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "minke"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "water"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "sponge"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "lotus"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "elodea"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "algae"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "dolphin"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "whale"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "shark"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "umbra"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "fluke"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "grunt"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "perch"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "elver"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "tench"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "trawl"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "guppy"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "salmon"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "pisces"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "barbel"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "burbot"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "saurel"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "darter"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "fungus"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "ocean"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "water"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "acaleph"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "alewife"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "anchovy"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "batfish"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "bergylt"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "bluecap"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "capelin"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "catfish"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "cavalla"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "cavally"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "chimera"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "codfish"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "dogfish"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "hogfish"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "jewfish"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "keeling"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "kokanee"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "octupus"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "oarfish"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "osseter"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "pigfish"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "sawfish"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "seawolf"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "bluewhale"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "bulltrout"
                }
            },
            "Mountains": {
                '0': {
                    'difficulty': "easy",
                    'name': "api"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "imja"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "yala"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "peak"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "oro"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "alp"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "glob"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "ibex"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "crag"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "dome"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "azul"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "cook"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "dore"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "ebal"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "etna"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "fuji"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "jaya"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "joma"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "meru"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "ossa"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "rigi"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "roan"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "teak"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "rosa"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "viso"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "devi"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "deep"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "kea"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "kat"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "loa"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "peru"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "cho"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "sar"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "ata"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "rimo"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "snow"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "ice"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "you"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "ski"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "slip"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "adams"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "asahi"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "athos"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "baker"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "binga"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "blanc"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "cenis"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "cinto"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "corno"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "cowan"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "dendi"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "eiger"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "hayes"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "overo"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "sinai"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "ararat"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "bogong"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "carmel"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "hermon"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "elbert"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "elbrus"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "erebus"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "hotaka"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "lelija"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "makalu"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "musala"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "muztag"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "sangay"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "taftan"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "wilson"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "tolima"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "yeguas"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "zirkel"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "sajama"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "mount"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "bernina"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "bolivar"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "brocken"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "everest"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "ganesh"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "foraker"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "harvard"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "hoffman"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "illampu"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "olympus"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "sanford"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "whitney"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "columbia"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "cotopaxi"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "adamello"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "kailash"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "fujiyama"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "kinabalu"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "annapurna"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "mckinley"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "maladetta"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "parnassus"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "tocurpuri"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "tongariro"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "pietrosul"
                }
            },
            "Rivers": {
                '0': {
                    'difficulty': "easy",
                    'name': "ain"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "arc"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "don"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "ems"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "hay"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "hue"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "ili"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "inn"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "lek"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "lot"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "mur"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "oka"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "taz"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "ume"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "var"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "aare"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "adda"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "amur"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "arno"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "aube"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "aude"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "back"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "beas"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "cher"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "gota"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "nile"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "gila"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "juba"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "kama"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "kemi"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "lech"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "naab"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "yew"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "ohio"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "ravi"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "tana"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "tone"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "unac"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "waal"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "yalu"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "adigo"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "ardour"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "aisne"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "aldan"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "aller"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "amnok"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "benue"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "congo"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "desna"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "doubs"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "drava"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "drina"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "havel"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "indus"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "kabul"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "miami"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "dvina"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "niger"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "rhine"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "lilac"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "shari"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "tagus"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "peach"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "xiang"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "yukon"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "amazon"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "angara"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "canton"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "gambia"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "hudson"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "orange"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "ottawa"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "rajang"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "ganga"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "koshi"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "krishna"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "lachlan"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "madeira"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "maranon"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "selenga"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "trinity"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "bagmati"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "trishuli"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "zambesi"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "bluenile"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "brisbane"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "chindwin"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "colorado"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "columbia"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "delaware"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "godavari"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "guadiana"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "missouri"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "indigirka"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "tennessee"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "tocantins"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "whitenile"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "roosevelt"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "irrawaddy"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "macquarie"
                }
            },
            "Birds": {
                '0': {
                    'difficulty': "easy",
                    'name': "ani"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "auk"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "cob"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "daw"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "emu"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "jay"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "kea"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "mew"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "moa"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "owl"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "pen"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "pie"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "tit"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "tui"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "chat"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "duck"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "coly"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "coot"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "crow"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "hen"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "dodo"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "dove"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "erne"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "eyas"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "fowl"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "guan"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "gull"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "hawk"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "ibis"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "kagu"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "swan"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "teal"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "kiwi"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "wren"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "kite"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "loom"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "myna"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "wych"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "rail"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "weka"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "brant"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "crake"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "crane"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "driver"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "eagle"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "egret"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "finch"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "galah"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "goose"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "greba"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "heron"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "merle"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "miner"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "mynah"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "owlet"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "pewit"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "pipt"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "quail"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "raven"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "robin"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "serin"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "snipe"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "swift"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "twite"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "parrot"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "stilt"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "falcon"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "veery"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "vireo"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "barbet"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "bishop"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "bulbul"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "chukor"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "pigeon"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "eagle"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "antbird"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "babbler"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "barnowl"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "bittern"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "bunting"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "bulshit"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "bushtit"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "bustard"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "buzzard"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "cacique"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "catbird"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "harrier"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "kestrel"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "lumpkin"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "ostrich"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "peacock"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "penguin"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "sparrow"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "vulture"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "windfowl"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "crossbill"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "bluebird"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "kingbird"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "whipbird"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "woodcock"
                }
            },
            "Languages": {
                '0': {
                    'difficulty': "easy",
                    'name': "gur"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "ibo"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "ido"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "kru"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "kwa"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "lao"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "mama"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "min"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "mon"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "neo"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "san"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "tiv"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "twi"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "ute"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "ainu"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "akan"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "chad"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "cham"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "cree"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "crow"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "dard"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "erse"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "eyak"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "dyak"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "hopi"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "igbo"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "inca"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "kana"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "kroo"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "lapp"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "maya"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "more"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "motu"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "nupe"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "pali"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "sulu"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "thai"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "tupi"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "urdu"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "zuni"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "aleut"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "argot"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "attic"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "banta"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "creek"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "czech"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "dayak"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "fanti"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "greek"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "hindi"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "ionic"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "irish"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "nepali"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "afghan"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "altaic"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "apache"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "arabic"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "asante"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "bahasa"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "basque"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "bihari"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "newari"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "danish"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "french"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "korean"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "german"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "lydian"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "median"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "yapon"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "sindhi"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "syriac"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "telugu"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "turkic"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "uralic"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "gaelic"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "apricot"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "amharic"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "aramaic"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "mrikara"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "armoric"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "ashanti"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "asianic"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "bengali"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "bosotho"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "chinese"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "english"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "italian"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "lativian"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "marathi"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "morisco"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "russian"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "serbian"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "spanish"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "swedish"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "turkish"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "armenian"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "ukrainian"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "gurkhali"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "japanese"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "sumerian"
                }
            },
            "Computers": {
                '0': {
                    'difficulty': "easy",
                    'name': "ada"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "alt"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "aol"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "apl"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "bit"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "bot"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "bug"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "ai"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "bus"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "cpu"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "dos"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "ftp"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "pop"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "push"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "hex"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "gui"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "ibm"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "isp"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "job"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "mac"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "net"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "web"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "icon"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "beta"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "byte"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "boot"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "cell"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "chip"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "code"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "core"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "data"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "edit"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "file"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "font"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "form"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "html"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "link"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "logo"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "menu"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "node"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "basic"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "ascii"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "abort"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "algol"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "arial"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "block"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "cache"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "click"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "close"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "crash"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "email"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "erase"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "frame"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "image"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "video"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "logic"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "macro"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "modem"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "router"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "queue"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "stack"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "spool"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "virus"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "papaw"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "access"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "avatar"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "backup"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "bitmap"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "client"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "google"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "memory"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "online"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "record"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "mouse"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "board"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "adaptor"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "animation"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "address"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "archive"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "arpanet"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "internet"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "browser"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "channel"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "chipset"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "circuit"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "display"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "firefox"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "hashing"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "imaging"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "monitor"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "mailbox"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "network"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "process"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "storage"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "bookmark"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "compiler"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "software"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "algorithm"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "bandwidth"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "backspace"
                }
            },
            "Movies": {
                '0': {
                    'difficulty': "easy",
                    'name': "ted"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "saw"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "red"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "spy"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "rio"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "big"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "abby"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "adam"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "argo"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "babe"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "baby"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "coma"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "fool"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "duel"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "dune"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "fame"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "fury"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "hook"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "mask"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "tron"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "tess"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "cujo"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "help"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "hugo"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "jude"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "nuts"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "iron"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "rope"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "star"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "taps"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "wilt"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "run"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "go"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "dark"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "hero"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "don"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "cops"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "save"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "hunt"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "ok"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "abyss"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "alfie"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "alien"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "alive"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "alone"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "angel"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "annie"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "ariel"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "babel"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "bambi"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "cobra"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "doubt"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "earth"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "ghost"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "giant"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "greed"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "gypsy"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "hotel"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "julia"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "kitty"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "mammy"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "wings"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "yanks"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "arthur"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "avalon"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "avatar"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "buster"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "cocoon"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "island"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "sahara"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "psycho"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "black"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "venom"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "harvey"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "hostel"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "aladdin"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "titanic"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "dracula"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "gravity"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "lincoln"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "chicago"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "everest"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "tangled"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "tootsie"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "platoon"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "witness"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "airport"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "superman"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "ironman"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "spiderman"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "airforce"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "tamarisk"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "airlift"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "airplane"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "airport"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "fighter"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "betrayal"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "godzilla"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "nightmare"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "gladiator"
                }
            },
            "Names": {
                '0': {
                    'difficulty': "easy",
                    'name': "ben"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "tom"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "tim"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "amy"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "army"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "bob"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "eva"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "jim"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "dan"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "ted"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "ron"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "lou"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "sam"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "jon"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "mia"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "riya"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "ray"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "ken"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "meg"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "joe"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "gil"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "gary"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "cory"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "cody"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "coby"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "kia"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "mony"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "tony"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "nia"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "elsa"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "elon"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "bill"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "jeff"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "mark"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "jack"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "dora"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "dani"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "adam"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "ajay"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "arno"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "aaden"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "aanya"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "aarav"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "aaron"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "abram"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "aisha"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "alina"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "aisha"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "alexa"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "alisa"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "angel"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "allen"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "biden"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "trump"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "caron"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "brown"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "bryon"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "cesar"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "daisy"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "james"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "kevin"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "aarush"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "aditya"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "gerald"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "andrew"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "alexis"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "adelia"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "alanna"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "apollo"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "harris"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "jimmy"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "robert"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "malaki"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "martin"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "marcos"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "abraham"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "addison"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "adelina"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "bartley"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "bellamy"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "benicio"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "annabel"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "angella"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "angella"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "anthony"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "charley"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "brynlee"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "clement"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "camisha"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "charlee"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "raintree"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "florida"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "hillary"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "kendrick"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "georgine"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "roosevelt"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "valentine"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "jacquelin"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "christian"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "alexandro"
                }
            },
            "Mathematics": {
                '0': {
                    'difficulty': "easy",
                    'name': "arc"
                },
                '1': {
                    'difficulty': "easy",
                    'name': "cos"
                },
                '2': {
                    'difficulty': "easy",
                    'name': "cot"
                },
                '3': {
                    'difficulty': "easy",
                    'name': "hcf"
                },
                '4': {
                    'difficulty': "easy",
                    'name': "lcm"
                },
                '5': {
                    'difficulty': "easy",
                    'name': "log"
                },
                '6': {
                    'difficulty': "easy",
                    'name': "odd"
                },
                '7': {
                    'difficulty': "easy",
                    'name': "ray"
                },
                '8': {
                    'difficulty': "easy",
                    'name': "sec"
                },
                '9': {
                    'difficulty': "easy",
                    'name': "set"
                },
                '10': {
                    'difficulty': "easy",
                    'name': "sin"
                },
                '11': {
                    'difficulty': "easy",
                    'name': "sum"
                },
                '12': {
                    'difficulty': "easy",
                    'name': "tan"
                },
                '13': {
                    'difficulty': "easy",
                    'name': "apex"
                },
                '14': {
                    'difficulty': "easy",
                    'name': "area"
                },
                '15': {
                    'difficulty': "easy",
                    'name': "axis"
                },
                '16': {
                    'difficulty': "easy",
                    'name': "base"
                },
                '17': {
                    'difficulty': "easy",
                    'name': "cosh"
                },
                '18': {
                    'difficulty': "easy",
                    'name': "coth"
                },
                '19': {
                    'difficulty': "easy",
                    'name': "even"
                },
                '20': {
                    'difficulty': "easy",
                    'name': "sinh"
                },
                '21': {
                    'difficulty': "easy",
                    'name': "join"
                },
                '22': {
                    'difficulty': "easy",
                    'name': "line"
                },
                '23': {
                    'difficulty': "easy",
                    'name': "mean"
                },
                '24': {
                    'difficulty': "easy",
                    'name': "node"
                },
                '25': {
                    'difficulty': "easy",
                    'name': "null"
                },
                '26': {
                    'difficulty': "easy",
                    'name': "path"
                },
                '27': {
                    'difficulty': "easy",
                    'name': "real"
                },
                '28': {
                    'difficulty': "easy",
                    'name': "root"
                },
                '29': {
                    'difficulty': "easy",
                    'name': "one"
                },
                '30': {
                    'difficulty': "easy",
                    'name': "sech"
                },
                '31': {
                    'difficulty': "easy",
                    'name': "two"
                },
                '32': {
                    'difficulty': "easy",
                    'name': "skew"
                },
                '33': {
                    'difficulty': "easy",
                    'name': "four"
                },
                '34': {
                    'difficulty': "easy",
                    'name': "five"
                },
                '35': {
                    'difficulty': "easy",
                    'name': "six"
                },
                '36': {
                    'difficulty': "easy",
                    'name': "nine"
                },
                '37': {
                    'difficulty': "easy",
                    'name': "ten"
                },
                '38': {
                    'difficulty': "easy",
                    'name': "unit"
                },
                '39': {
                    'difficulty': "easy",
                    'name': "zero"
                },
                '40': {
                    'difficulty': "medium",
                    'name': "three"
                },
                '41': {
                    'difficulty': "medium",
                    'name': "seven"
                },
                '42': {
                    'difficulty': "medium",
                    'name': "eight"
                },
                '43': {
                    'difficulty': "medium",
                    'name': "symbol"
                },
                '44': {
                    'difficulty': "medium",
                    'name': "table"
                },
                '45': {
                    'difficulty': "medium",
                    'name': "letter"
                },
                '46': {
                    'difficulty': "medium",
                    'name': "number"
                },
                '47': {
                    'difficulty': "medium",
                    'name': "double"
                },
                '48': {
                    'difficulty': "medium",
                    'name': "float"
                },
                '49': {
                    'difficulty': "medium",
                    'name': "binary"
                },
                '50': {
                    'difficulty': "medium",
                    'name': "center"
                },
                '51': {
                    'difficulty': "medium",
                    'name': "circle"
                },
                '52': {
                    'difficulty': "medium",
                    'name': "convex"
                },

                '53': {
                    'difficulty': "medium",
                    'name': "cosine"
                },
                '54': {
                    'difficulty': "medium",
                    'name': "cuboid"
                },
                '55': {
                    'difficulty': "medium",
                    'name': "radian"
                },
                '56': {
                    'difficulty': "medium",
                    'name': "degree"
                },
                '57': {
                    'difficulty': "medium",
                    'name': "factor"
                },
                '58': {
                    'difficulty': "medium",
                    'name': "linear"
                },

                '59': {
                    'difficulty': "medium",
                    'name': "matrix"
                },
                '60': {
                    'difficulty': "medium",
                    'name': "origin"
                },
                '61': {
                    'difficulty': "medium",
                    'name': "radius"
                },
                '62': {
                    'difficulty': "medium",
                    'name': "scalar"
                },
                '63': {
                    'difficulty': "medium",
                    'name': "vector"
                },
                '64': {
                    'difficulty': "medium",
                    'name': "sphere"
                },

                '65': {
                    'difficulty': "medium",
                    'name': "volume"
                },
                '66': {
                    'difficulty': "medium",
                    'name': "divide"
                },
                '67': {
                    'difficulty': "medium",
                    'name': "domain"
                },
                '68': {
                    'difficulty': "medium",
                    'name': "euler"
                },
                '69': {
                    'difficulty': "medium",
                    'name': "member"
                },
                '70': {
                    'difficulty': "medium",
                    'name': "finite"
                },
                '71': {
                    'difficulty': "medium",
                    'name': "round"
                },
                '72': {
                    'difficulty': "medium",
                    'name': "graph"
                },
                '73': {
                    'difficulty': "medium",
                    'name': "normal"
                },
                '74': {
                    'difficulty': "medium",
                    'name': "angle"
                },
                '75': {
                    'difficulty': "hard",
                    'name': "adjoint"
                },
                '76': {
                    'difficulty': "hard",
                    'name': "algebra"
                },
                '77': {
                    'difficulty': "hard",
                    'name': "average"
                },
                '78': {
                    'difficulty': "hard",
                    'name': "bounded"
                },
                '79': {
                    'difficulty': "hard",
                    'name': "complex"
                },
                '80': {
                    'difficulty': "hard",
                    'name': "concave"
                },
                '81': {
                    'difficulty': "hard",
                    'name': "decimal"
                },
                '82': {
                    'difficulty': "hard",
                    'name': "ellipse"
                },
                '83': {
                    'difficulty': "hard",
                    'name': "epsilon"
                },
                '84': {
                    'difficulty': "hard",
                    'name': "formula"
                },
                '85': {
                    'difficulty': "hard",
                    'name': "hexagon"
                },
                '86': {
                    'difficulty': "hard",
                    'name': "octagon"
                },
                '87': {
                    'difficulty': "hard",
                    'name': "pentagon"
                },
                '88': {
                    'difficulty': "hard",
                    'name': "integer"
                },
                '89': {
                    'difficulty': "hard",
                    'name': "inverse"
                },
                '90': {
                    'difficulty': "hard",
                    'name': "mapping"
                },
                '91': {
                    'difficulty': "hard",
                    'name': "maximum"
                },
                '92': {
                    'difficulty': "hard",
                    'name': "minimum"
                },
                '93': {
                    'difficulty': "hard",
                    'name': "modulus"
                },
                '94': {
                    'difficulty': "hard",
                    'name': "polygon"
                },
                '95': {
                    'difficulty': "hard",
                    'name': "segment"
                },
                '96': {
                    'difficulty': "hard",
                    'name': "surface"
                },
                '97': {
                    'difficulty': "hard",
                    'name': "algorithm"
                },
                '98': {
                    'difficulty': "hard",
                    'name': "conjugate"
                },
                '99': {
                    'difficulty': "hard",
                    'name': "decrement"
                }
            },
        })


