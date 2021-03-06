import hashlib
import math
import random
import sys
# Do NOT alter the import list!!!!
# import numpy as np
# import gmpy2

class Project3:

    def __init__(self):
        pass

    # TODO: OPTIONAL - Add helper methods below
    # BEGIN HELPER METHODS
    def isqrt(self, n: int) -> int:
        # Newtorn method square root https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (x + n // x) // 2
        return x

    def icbrt(self, n):
        # r, fo = gmpy2.iroot(n , 3)
        # j = n - pow(r, 3)
        # # print(f"the diff is {j}, root founf {fo}")
        # return r
        # a = np.array([n], dtype=np.int)
        # return np.cbrt(a)
        x = n
        y = (x + 1) // 2
        while y < x:
            x = y
            y = (2*x + n // pow(x, 2)) // 3
        
        return x
        

    def egcd(self, a: int, b: int) -> int:
        if a % b == 0:
            return 0, 1
        else:
            q = a // b
            x, y = self.egcd(b, a % b)
            return y, x - y * q
        

    def product(self, a, b):
        return a*b

    def chineese_reminder(self, n_items, c_items):
        N = n_items[0] * n_items[1]
        a, b = self.egcd(n_items[0], n_items[1])
        p1 = b * n_items[1] % N
        q1 = a * n_items[0] % N
        c_p = (c_items[0] * p1 + c_items[1] * q1) % N

        a, b = self.egcd(N, n_items[2])
        n_p = N
        N *= n_items[2]
        p1 = b * n_items[2] % N
        q1 = a * n_p % N
        c = (c_p * p1 +  c_items[2]  * q1) % N
        r = self.icbrt(c)
        return r

    # END HELPER METHODS

    def get_factors(self, n: int):
        # Fermat factorization method https://en.wikipedia.org/wiki/Fermat%27s_factorization_method
        p = 0
        q = 0
        # brute force --- doesn't work
        # for i in range (2, n - 1):
        #     if n % i == 0:
        #         p = i
        #         q = n / i
        #         break
        a = self.isqrt(n) + 1
        b2 = pow(a, 2) - n
        b = self.isqrt(b2)
        
        while pow(b, 2) != b2:
            a += 1
            b2 = pow(a, 2) - n
            b = self.isqrt(b2)
        
        return a + b, a - b
        # return p, q

    def get_private_key_from_p_q_e(self, p: int, q: int, e: int):
        # TODO: Implement this method for Task 5, Step 2
        # https://mathworld.wolfram.com/ModularInverse.html
        # https://www.dcode.fr/extended-gcd
        phi  = (p-1) * (q-1)
        u1, u2, r1,  v1, v2, r2 = 1, 0, e, 0, 1, phi
        while r2 != 0:
            q = r1 // r2
            v1, v2, r2, u1, u2, r1 = (u1 - q * v1), (u2 - q * v2), (r1 - q * r2), v1, v2, r2
        # _, u1, _ = self.egcd(phi, e)
        return u1 % phi
        

    def task_1(self, n_str: str, d_str: str, c_str: str) -> str:
        # TODO: Implement this method for Task 1
        n = int(n_str, 16)
        d = int(d_str, 16)
        c = int(c_str, 16)
        m = pow(c, d, n)

        return hex(m).rstrip('L')

    def task_2(self, password_hash: str) -> str:
        # The password list is prepopulated for your convenience
        common_password_list = ['123456', '12345', '123456789', 'password', 'iloveyou', 'princess', '1234567', 'rockyou', '12345678',
                                'abc123', 'nicole', 'daniel', 'babygirl', 'monkey', 'lovely', 'jessica', '654321', 'michael', 'ashley',
                                'qwerty', '111111', 'iloveu', '0', 'michelle', 'tigger', 'sunshine', 'chocolate', 'password1', 'soccer',
                                'anthony', 'friends', 'butterfly', 'purple', 'angel', 'jordan', 'liverpool', 'justin', 'loveme', '123123',
                                'football', 'secret', 'andrea', 'carlos', 'jennifer', 'joshua', 'bubbles', '1234567890', 'superman',
                                'hannah', 'amanda', 'loveyou', 'pretty', 'basketball', 'andrew', 'angels', 'tweety', 'flower', 'hello',
                                'elizabeth', 'hottie', 'tinkerbell', 'charlie', 'samantha', 'barbie', 'chelsea', 'lovers', 'teamo',
                                'jasmine', 'brandon', '666666', 'shadow', 'melissa', 'eminem', 'matthew', 'robert', 'danielle', 'forever',
                                'family', 'jonathan', '987654321', 'computer', 'whatever', 'dragon', 'vanessa', 'cookie', 'naruto',
                                'summer', 'sweety', 'spongebob', 'joseph', 'junior', 'softball', 'taylor', 'yellow', 'daniela', 'lauren',
                                'mickey', 'princesa', 'alexandra', 'alexis', 'jesus', 'estrella', 'miguel', 'william', 'thomas',
                                'beautiful', 'mylove', 'angela', 'poohbear', 'patrick', 'iloveme', 'sakura', 'adrian', 'alexander',
                                'destiny', 'christian', '121212', 'sayang', 'america', 'dancer', 'monica', 'richard', '112233', 'princess1',
                                '555555', 'diamond', 'carolina', 'steven', 'rangers', 'louise', 'orange', '789456', '999999', 'shorty',
                                '11111', 'nathan', 'snoopy', 'gabriel', 'hunter', 'cherry', 'killer', 'sandra', 'alejandro', 'buster',
                                'george', 'brittany', 'alejandra', 'patricia', 'rachel', 'tequiero', '7777777', 'cheese', '159753',
                                'arsenal', 'dolphin', 'antonio', 'heather', 'david', 'ginger', 'stephanie', 'peanut', 'blink182', 'sweetie',
                                '222222', 'beauty', '987654', 'victoria', 'honey', '0', 'fernando', 'pokemon', 'maggie', 'corazon',
                                'chicken', 'pepper', 'cristina', 'rainbow', 'kisses', 'manuel', 'myspace', 'rebelde', 'angel1', 'ricardo',
                                'babygurl', 'heaven', '55555', 'baseball', 'martin', 'greenday', 'november', 'alyssa', 'madison', 'mother',
                                '123321', '123abc', 'mahalkita', 'batman', 'september', 'december', 'morgan', 'mariposa', 'maria',
                                'gabriela', 'iloveyou2', 'bailey', 'jeremy', 'pamela', 'kimberly', 'gemini', 'shannon', 'pictures',
                                'sophie', 'jessie', 'hellokitty', 'claudia', 'babygirl1', 'angelica', 'austin', 'mahalko', 'victor',
                                'horses', 'tiffany', 'mariana', 'eduardo', 'andres', 'courtney', 'booboo', 'kissme', 'harley', 'ronaldo',
                                'iloveyou1', 'precious', 'october', 'inuyasha', 'peaches', 'veronica', 'chris', '888888', 'adriana',
                                'cutie', 'james', 'banana', 'prince', 'friend', 'jesus1', 'crystal', 'celtic', 'zxcvbnm', 'edward',
                                'oliver', 'diana', 'samsung', 'freedom', 'angelo', 'kenneth', 'master', 'scooby', 'carmen', '456789',
                                'sebastian', 'rebecca', 'jackie', 'spiderman', 'christopher', 'karina', 'johnny', 'hotmail', '123456789',
                                'school', 'barcelona', 'august', 'orlando', 'samuel', 'cameron', 'slipknot', 'cutiepie', 'monkey1',
                                '50cent', 'bonita', 'kevin', 'maganda', 'babyboy', 'casper', 'brenda', 'adidas', 'kitten', 'karen',
                                'mustang', 'isabel', 'natalie', 'cuteako', 'javier', '789456123', '123654', 'sarah', 'bowwow', 'portugal',
                                'laura', '777777', 'marvin', 'denise', 'tigers', 'volleyball', 'jasper', 'rockstar', 'january', 'alicia',
                                'nicholas', 'flowers', 'cristian', 'tintin', 'bianca', 'chrisbrown', 'chester', '101010', 'smokey',
                                'silver', 'internet', 'sweet', 'strawberry', 'garfield', 'dennis', 'panget', 'francis', 'cassie', 'benfica',
                                'love123', 'asdfgh', 'lollipop', 'olivia', 'cancer', 'camila', 'qwertyuiop', 'superstar', 'harrypotter',
                                'charles', 'monique', 'midnight', 'vincent', 'christine', 'apples', 'scorpio', 'jordan23', 'lorena',
                                'andreea', 'mercedes', 'katherine', 'charmed', 'abigail', 'rafael', 'icecream', 'mexico', 'brianna',
                                'nirvana', 'aaliyah', 'pookie', 'johncena', 'lovelove', 'abcdef', 'benjamin', '131313', 'gangsta', 'brooke',
                                '333333', 'hiphop', 'aaaaaa', 'mybaby', 'sergio', 'welcome', 'metallica', 'julian', 'travis', 'myspace1',
                                'babyblue', 'sabrina', 'michael1', 'jeffrey', 'stephen', 'love', 'dakota', 'catherine', 'badboy',
                                'fernanda', 'westlife', 'blondie', 'sasuke', 'smiley', 'jackson', 'simple', 'melanie', 'steaua', 'dolphins',
                                'roberto', 'fluffy', 'teresa', 'piglet', 'ronald', 'slideshow', 'asdfghjkl', 'minnie', 'newyork', 'jason',
                                'raymond', 'santiago', 'jayson', '88888888', '5201314', 'jerome', 'gandako', 'muffin', 'gatita', 'babyko',
                                '246810', 'sweetheart', 'chivas', 'ladybug', 'kitty', 'popcorn', 'alberto', 'valeria', 'cookies', 'leslie',
                                'jenny', 'nicole1', '12345678910', 'leonardo', 'jayjay', 'liliana', 'dexter', '232323', 'amores', 'rockon',
                                'christ', 'babydoll', 'anthony1', 'marcus', 'fatima', 'miamor', 'lover', 'chris1', 'single', 'eeyore',
                                'lalala', '252525', 'scooter', 'natasha', 'skittles', 'brooklyn', 'colombia', '159357', 'teddybear',
                                'winnie', 'happy', 'manutd', '123456a', 'britney', 'katrina', 'christina', 'pasaway', 'cocacola', 'mahal',
                                'grace', 'linda', 'albert', 'tatiana', 'london', 'cantik', '123456', 'lakers', 'marie', 'teiubesc',
                                '147258369', 'charlotte', 'natalia', 'francisco', 'amorcito', 'smile', 'paola', 'angelito', 'manchester',
                                'hahaha', 'elephant', 'mommy1', 'shelby', '147258', 'kelsey', 'genesis', 'amigos', 'snickers', 'xavier',
                                'turtle', 'marlon', 'linkinpark', 'claire', 'stupid', '147852', 'marina', 'garcia', 'diego', 'brandy',
                                'letmein', 'hockey', '444444', 'sharon', 'bonnie', 'spider', 'iverson', 'andrei', 'justine', 'frankie',
                                'pimpin', 'disney', 'rabbit', '54321', 'fashion', 'soccer1', 'red123', 'bestfriend', 'england', 'hermosa',
                                '456123', 'qazwsx', 'bandit', 'danny', 'allison', 'emily', '102030', 'lucky1', 'sporting', 'miranda',
                                'dallas', 'hearts', 'camille', 'wilson', 'potter', 'pumpkin', 'iloveu2', 'number1', 'katie', 'guitar',
                                '212121', 'truelove', 'jayden', 'savannah', 'hottie1', 'phoenix', 'monster', 'player', 'ganda', 'people',
                                'scotland', 'nelson', 'jasmin', 'timothy', 'onelove', 'ilovehim', 'shakira', 'estrellita', 'bubble',
                                'smiles', 'brandon1', 'sparky', 'barney', 'sweets', 'parola', 'evelyn', 'familia', 'love12', 'nikki',
                                'motorola', 'florida', 'omarion', 'monkeys', 'loverboy', 'elijah', 'joanna', 'canada', 'ronnie', 'mamita',
                                'emmanuel', 'thunder', '999999999', 'broken', 'rodrigo', 'maryjane', 'westside', 'california', 'lucky',
                                'mauricio', 'yankees', 'jamaica', 'justin1', 'amigas', 'preciosa', 'shopping', 'flores', 'mariah', 'matrix',
                                'isabella', 'tennis', 'trinity', 'jorge', 'sunflower', 'kathleen', 'bradley', 'cupcake', 'hector',
                                'martinez', 'elaine', 'robbie', 'friendster', 'cheche', 'gracie', 'connor', 'hello1', 'valentina', 'melody',
                                'darling', 'sammy', 'jamie', 'santos', 'abcdefg', 'joanne', 'candy', 'loser', 'dominic', 'pebbles',
                                'sunshine1', 'swimming', 'millie', 'loving', 'gangster', 'blessed', 'compaq', 'taurus', 'gloria', 'tyler',
                                'aaron', 'darkangel', 'kitkat', 'megan', 'dreams', 'sweetpea', 'bettyboop', 'jessica1', 'cynthia',
                                'cheyenne', 'ferrari', 'dustin', 'iubire', 'a123456', 'snowball', 'purple1', 'violet', 'darren', 'starwars',
                                'bestfriends', 'inlove', 'kelly', 'batista', 'karla', 'sophia', 'chacha', 'marian', 'sydney', 'pogiako',
                                'gerald', 'jordan1', '10203', 'daddy1', 'zachary', 'daddysgirl', 'billabong', 'carebear', 'froggy', 'pinky',
                                'erika', 'oscar', 'skater', 'raiders', 'nenita', 'tigger1', 'ashley1', 'charlie1', 'gatito', 'lokita',
                                'maldita', 'buttercup', 'nichole', 'bambam', 'nothing', 'glitter', 'bella', 'amber', 'apple', '123789',
                                'sister', 'zacefron', 'tokiohotel', 'loveya', 'lindsey', 'money', 'lovebug', 'bubblegum', 'marissa',
                                'dreamer', 'darkness', 'cecilia', 'lollypop', 'nicolas', 'google', 'lindsay', 'cooper', 'passion',
                                'kristine', 'green', 'puppies', 'ariana', 'chubby', 'raquel', 'lonely', 'anderson', 'sammie', 'mario',
                                'butter', 'willow', 'roxana', 'mememe', 'caroline', 'susana', 'kristen', 'baller', 'hotstuff', 'carter',
                                'stacey', 'babylove', 'angelina', 'miller', 'scorpion', 'sierra', 'sweet16', '12345', 'rocker', 'bhebhe',
                                'gustavo', 'marcos', 'chance', '123qwe', 'kayla', 'james1', 'football1', 'eagles', 'loveme1', 'milagros',
                                'stella', 'lilmama', 'beyonce', 'lovely1', 'rocky', 'daddy', 'catdog', 'armando', 'margarita', '151515',
                                'loves', 'lolita', '202020', 'gerard', 'undertaker', 'amistad', 'williams', 'qwerty1', 'freddy',
                                'capricorn', 'caitlin', 'bryan', 'delfin', 'dance', 'cheerleader', 'password2', 'PASSWORD', 'martha',
                                'lizzie', 'georgia', 'matthew1', 'enrique', 'zxcvbn', 'badgirl', 'andrew1', '141414', '11111111', 'dancing',
                                'cuteme', 'booger', 'amelia', 'vampire', 'skyline', 'chiquita', 'angeles', 'scoobydoo', 'janine', 'tamara',
                                'carlitos', 'money1', 'sheila', 'justme', 'ireland', 'kittycat', 'hotdog', 'yamaha', 'tristan', 'harvey',
                                'israel', 'legolas', 'michelle1', 'maddie', 'angie', 'cinderella', 'lester', 'ashton', 'tazmania',
                                'remember', 'xxxxxx', 'tekiero', 'thebest', 'princesita', 'lucky7', 'peewee', 'paloma', 'buddy1', 'deedee',
                                'miriam', 'april', 'patches', 'regina', 'janice', 'cowboys', 'myself', 'lipgloss', 'jazmin', 'rosita',
                                'happy1', 'felipe', 'chichi', 'pangit', 'mierda', 'genius', '741852963', 'hernandez', 'awesome', 'walter',
                                'tinker', 'arturo', 'silvia', 'melvin', 'celeste', 'pussycat', 'gorgeous', 'david1', 'molly', 'honeyko',
                                'mylife', 'animal', 'penguin', 'babyboo', 'loveu', 'simpsons', 'lupita', 'boomer', 'panthers', 'hollywood',
                                'alfredo', 'musica', 'johnson', 'hawaii', 'sparkle', 'kristina', 'crazy', 'valerie', 'spencer', 'scarface',
                                'hardcore', '98765', '0', 'winter', 'hailey', 'trixie', 'hayden', 'micheal', 'wesley', '242424',
                                '987654321', 'marisol', 'nikita', 'daisy', 'jeremiah', 'pineapple', 'mhine', 'isaiah', 'christmas', 'cesar',
                                'lolipop', 'butterfly1', 'chloe', 'lawrence', 'xbox360', 'sheena', 'murphy', 'madalina', 'anamaria',
                                'gateway', 'debbie', 'blonde', 'jasmine1', 'please', 'bubbles1', 'jimmy', 'beatriz', 'diamonds', 'whitney',
                                'friendship', 'sweetness', 'pauline', 'desiree', 'trouble', '741852', 'united', 'marley', 'brian',
                                'barbara', 'hannah1', 'bananas', 'julius', 'leanne', 'sandy', 'marie1', 'anita', 'lover1', 'chicago',
                                'twinkle', 'pantera', 'february', 'birthday', 'shadow1', 'qwert', 'bebita', '87654321', 'twilight',
                                'imissyou', 'pollito', 'ashlee', 'tucker', 'cookie1', 'shelly', 'catalina', '147852369', 'beckham',
                                'simone', 'nursing', 'iloveyou!', 'eugene', 'torres', 'damian', '123123123', 'joshua1', 'bobby', 'babyface',
                                'andre', 'donald', 'daniel1', 'panther', 'dinamo', 'mommy', 'juliana', 'cassandra']

        # password = common_password_list[0]
        # This is how you get the SHA-256 hash:
        
        for p in common_password_list:
            hashed_password = hashlib.sha256(p.encode()).hexdigest()
            if hashed_password == password_hash:
                return p

        return ""

    def task_3(self, user_id_1: str, user_id_2: str, amount: int, prev_block_hash: str) -> int:
        nonce = 0
        transaction_string = f"{user_id_1}:{user_id_2}:{amount}{prev_block_hash}"
        while True:
            candidate = f"{nonce}{transaction_string}"
            block_hash = hashlib.sha256(candidate.encode())
            hex = block_hash.hexdigest()
            if hex.startswith('00'):
                return nonce
            nonce += 1
            # break

        return nonce

    def task_4(self, from_user_id: str, to_user_id: str, amount: int, d: int, e: int, n: int) -> int:
        # Build the transaction string
        trans = from_user_id + ':' + to_user_id + ':' + str(amount)
        # Hash the transaction string
        trans_hash = hashlib.sha256(trans.encode('utf-8'))
        # You may find this line helpful for getting the integer value of the transaction hash
        trans_hash_as_int = int.from_bytes(trans_hash.digest(), sys.byteorder)

        # Create the signature (the number 11 is simply a placeholder)
        signature = pow(trans_hash_as_int, d, n)

        return signature

    def task_5(self, n_str: str, e_str: str) -> str:
        n = int(n_str, 16)
        e = int(e_str, 16)

        # Step 1
        p, q = self.get_factors(n)
        if p * q == n:
            ssd = 'greta'
        # Step 2
        d = self.get_private_key_from_p_q_e(p, q, e)

        return hex(d).rstrip('L')

    def task_6(self, given_public_key_n: int, given_public_key_e: int, public_key_list: list) -> int:
        counter = 0
        d = 0
        for candidate_n in public_key_list:
            n_gcd = math.gcd(given_public_key_n, candidate_n)
            if n_gcd != 1:
                # found two keys with common factors
                #factorize using the acquired knowledge
                p = n_gcd
                q = given_public_key_n // p
                d = self.get_private_key_from_p_q_e(p, q, given_public_key_e)
                break
            counter += 1

        return d

    def task_7(self, n_1_str: str, c_1_str: str, n_2_str: str, c_2_str: str, n_3_str: str, c_3_str: str) -> str:
        # TODO: Implement this method for Task 7
        n_1 = int(n_1_str, 16)
        c_1 = int(c_1_str, 16)
        n_2 = int(n_2_str, 16)
        c_2 = int(c_2_str, 16)
        n_3 = int(n_3_str, 16)
        c_3 = int(c_3_str, 16)

        msg = ''
        m = 0

        #cubic root is overflowing
        # m = (c_1 * c_2 * c_3) ** 1./3
        # Hastad's attack https://1library.net/article/hastad-s-broadcast-attack-rsa-vulnerabilities.qol1r2jq
        m = self.chineese_reminder([n_1, n_2, n_3], [c_1, c_2, c_3])
        msg = bytes.fromhex(hex(m).rstrip('L')[2:]).decode('UTF-8')

        return msg