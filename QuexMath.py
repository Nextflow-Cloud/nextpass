"""

/*----------------------------------------------------------------------------------------------*
*   Copyright (c) Queryzi Inc. All rights reserved.
*   You may not decompile this software (the QuexMath.pyd file) without permittance of Queryzi Inc.
/*----------------------------------------------------------------------------------------------*

This is a math class, that does not replace the already exisiting math class for python.
This provides a bit more features than the python math library as it has HEX - Decimal, and binary conversion. 
This class is similar to the python math library, but aims to add more features, and has a bit more features. 

This library is written by Queryzi.

"""
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # Quebec City
# Quartier petit champlain
# Fleur de lys centre commercial
# Citadelle
import sys
# try:
from tkinter import *
import math as ma
import math
import secrets
from functools import reduce
from tkinter.ttk import *
from tkinter.messagebox import *
from decimal import Decimal, getcontext
# except ImportError:
    # mods = [m.__name__ for m in sys.modules.values() if m]
    # message = 'You need the following modules to use this math class: '
    # for i in range(len(mods)):
    #     message += mods[i] + ', '
    
    # message = message.split(', ')
    # message.pop()

    # message = ", ".join(message)
    # message += '.'
    # raise ImportError(message)

class BaseMathConsoleError(Exception):
    def __init__(self, message):
        super.__init__(message)

class BaseMathGuiError():
    def __init__(self, message, consolas = False):
        root = Tk()

        root.withdraw()

        showerror('An error has occured', message)

        root.mainloop()


def getType(x):
    """This returns the type of x."""
    result = str(type(x)).replace('<class', '').replace('>', '', ).replace('\'', '').replace(' ', '')
    if result == 'int':
        return int
    elif result == 'str':
        return str
    elif result == 'dict':
        return dict
    elif result == 'object':
        return object
    elif result == 'float':
        return float
    else:
        return result

class MathError():
    def __init__(self, message, console = False):
        if (console):
            raise BaseMathConsoleError(message)
        elif ( not (console)):
            BaseMathGuiError(message)
        else:
            print(f"Console or not, need a boolean value not {(str(type(console))).replace('<', '').replace('type', '').replace('>', '')}.")
            newone = input('Proper value')
            super.__init__(message, bool(newone))

class Math():
    """This is a math library of basic math functions. This is a math class created by Queryzi."""
    def __init__(self, consolas = False):
        with open(f'QuexMath.pyi', 'w') as f:
            f.write('''"""

/*----------------------------------------------------------------------------------------------*
*   Copyright (c) Queryzi Inc. All rights reserved.
*   You may not decompile this software (the QuexMath.pyd file) without permittance of Queryzi Inc.
/*----------------------------------------------------------------------------------------------*

This is a math class, that does not replace the already exisiting math class for python.
This provides a bit more features than the python math library as it has HEX - Decimal, and binary conversion. 
This class is similar to the python math library, but aims to add more features, and has a bit more features. 

This library is written by Queryzi.

"""

from decimal import Decimal

class BaseMathConsoleError(Exception):
    """This is the basemath console error exception and it inherits Exception."""

    def __init__(self, message) -> None: ...

class BaseMathGuiError():
    """This is the basemath GUI error exception and it inherits Exception."""

    def __init__(self, message, consolas = False) -> None: ...

def getType(x): ...
    """This returns the type of x."""

class MathError():
    """This is the math error class, and it raises a error."""
    def __init__(self, message, console = False) -> None: ...

class Math():
    """This is a math library of basic math functions. This is a math class created by Queryzi."""

    def divide(self, x: float, y: float) -> float: ...
        """Divide two numbers by eachother, divide x by y."""

    def range(self, x: int) -> list: ...
        """Generate a range from 0 to x, where x is a integer."""

    def combination(self, n: int, r: int) -> float: ...
        """This calculates the amount of combinations for n of r."""

    def permutation(self, n: int, r: int, repeat=False) -> float: ...
        """This calculates the amount of permutations for n of r."""

    def factorial(self, x: int) -> int: ...
        """This calculates the factorial of x. Example is 9, 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1."""

    def multiply(self, x: float, y: float) -> float: ...
        """Multiply two numbers by eachother, multiply x by y."""

    def factors(self, n) -> list: ...
        """Gets the factors of n."""

    def pi(self, n: int) -> Decimal: ...
        """This will calculate pi up to n digits. This uses Decimal for better precision than float."""

    def piFloat(self, n: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def getArray(self, fr: float, ut: float, interval: float) -> list: ...
        """Returns a list starting from fr, and ends at ut, at an interval of interval."""

    def e(self, x: int) -> Decimal: ...
        """This will calculate e up to n digits. This uses Decimal for better precision than float."""

    def eFloat(self, x: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def sin(self, n: float, mode='rad') -> float: ...
        """This will calculate the sin of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cos(self, n: float, mode='rad') -> float: ...
        """This will calculate the cos of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def tan(self, n: float, mode='rad') -> float: ...
        """This will calculate the tan of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cot(self, n: float, mode='rad') -> float: ...
        """This will calculate the cot of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def log(self, x, b) -> float: ...
        """This will calculate the log of x of base b."""

    def ln(self, x) -> float: ...
        """This will calculate the log of e of x, or it calculate the natural log of x."""

    def radians(self, r: float) -> float: ...
        """This will convert degrees into radians mathematically."""

    def degrees(self, r: float) -> float: ...
        """This will convert radians into degrees mathematically."""

    def gcd(self, x, y) -> int: ...
        """This will calculate the greatest common denominator, or gcd for x and y."""

    def fraction(self, x: float) -> list: ...
        """This will return the fraction of a float."""

    @property
    def __version(self) -> tuple: ...
        """This will return the version of the math library in a tuple."""

class String():
    """This is a class for manipulating strings. This doesn't have much right now except for reverse a string."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, string: str) -> str: ...
        """Reverses a string efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Array():
    """This is a class for manipulating arrays. This doesn't have much right now except for reverse a array."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, array: list) -> list: ...
        """Reverses a array efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Binary(Math):
    """This is a class for binary conversions between decimal and text conversions."""
    
    def __init__(self, consolas = False) -> None: ...

    def texttoBinary(self, x: str) -> str: ...
        """This converts text to binary using the ord() function and converting to binary."""

    def Binarytotext(self, x: str) -> str: ...
        """Convert binary to text. This will convert it using chr and convert Binary to int and return the string."""

    def InttoBinary(self, x: int) -> int: ...
        """This will convert a integer to binary."""

    def toDecimal(self, x: int) -> int: ...
        """Convert binary to decimal (integer with base 10)."""

    @property
    def __version(self) -> tuple:
        """Returns the version of this class."""

class Hexadecimal:
    """A class for hexadecimal conversions with int to hexadecimal and hexadecimal to int, or base 16 to base 10, and base 10 to base 16."""

    def __init__(self, consolas = False) -> None: ...

    def InttoHexa(self, x: int) -> str: ...
        """Convert integer or decimal with base 10, and convert it to hexadecimal with base 16."""

    def HexatoInt(self, x: str) -> int: ...
        """Convert Hexa decimal to integer, or convert base 16 to base 10."""

    def texttoHexa(self, x: str) -> str: ...
        """Converts text to hexadecimal. This uses ASCII encoding."""

    def HexatoText(self, x: str) -> str: ...
        """This will convert hexadecimal string to a text string using ascii encoding."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""''')
            f.close()
        self.console = True
        if (consolas and not bool(consolas)):
            self.console = False

    def divide(self, x: float, y: float):
        """Divide two numbers by eachother, divide x by y."""
        leny = len(str(y))
        posy = str(y).index('.') + 1
        pow10y = 10 ** (leny - posy)
        ytmp = y * pow10y
        ytmpa = 1 / ytmp
        result = x * ytmpa
        return result * pow10y

    def range(self, x: int):
        """Generate a range from 0 to x, where x is a integer."""
        n = x
        numbs = []
        while n != 0:
            numbs.append(n)
            n = n - 1
        return numbs

    def combination(self, n: int, r: int):
        """This calculates the amount of combinations for n of r."""
        numerator = self.self.factorial(n)
        denominator = self.self.factorial(r) * self.self.factorial(n - r)
        return numerator / denominator

    def permutation(self, n: int, r: int, repeat=False):
        """This calculates the amount of permutations for n of r."""
        if (repeat == False):
            numerator = self.self.factorial(n)
            denominator = self.self.factorial(n - r)
            return numerator / denominator
        else:
            return n ** r

    def factorial(self, x: int):
        """This calculates the factorial of x. Example is 9, 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1."""
        result = 1
        for i in self.range(x):
            result = result * i
        return result

    def multiply(self, x: float, y: float):
        """Multiply two numbers by eachother, multiply x by y."""
        lenx = len(str(x))
        leny = len(str(y))
        posx = str(x).index('.') + 1
        posy = str(y).index('.') + 1
        pow10x = 10 ** (len(str(x)) - posx)
        pow10y = 10 ** (len(str(y)) - posy)
        ytmp = y * pow10y
        xtmp = x * pow10x
        multix = xtmp
        for i in range(int(round(ytmp)) - 1):
            multix = multix + xtmp
        
        tmppow = pow10x

        for i in range(pow10y - 1):
            tmppow += pow10x

        multix = multix / tmppow

        return multix
    def factors(self, n):
        """Gets the factors of n."""
        step = 2 if n%2 else 1
        return list(set(reduce(list.__add__,
                    ([i, n//i] for i in range(1, int(math.sqrt(n))+1, step) if n % i == 0))))

    def pi(self, n: int):
        """This will calculate pi up to n digits. This uses Decimal for better precision than float."""
        getcontext().prec=n
        t= Decimal(0)
        pi = Decimal(0)
        deno= Decimal(0)
        k = 0
        for k in range(n):
            t = ((-1)**k)*(self.factorial(6*k))*(13591409+545140134*k)
            deno = self.factorial(3*k)*(self.factorial(k)**3)*(640320**(3*k))
            pi += Decimal(t)/Decimal(deno)                                   
        pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
        pi = 1/pi
        return Decimal(pi)

    def piFloat(self, n: int):
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""
        getcontext().prec=n
        t= Decimal(0)
        pi = Decimal(0)
        deno= Decimal(0)
        k = 0
        for k in range(n):
            t = ((-1)**k)*(self.factorial(6*k))*(13591409+545140134*k)
            deno = self.factorial(3*k)*(self.factorial(k)**3)*(640320**(3*k))
            pi += Decimal(t)/Decimal(deno)                                   
        pi = pi * Decimal(12)/Decimal(640320**Decimal(1.5))
        pi = 1/pi
        return float(pi)

    def getArray(self, fr: float, ut: float, interval: float):
        """Returns a list starting from fr, and ends at ut, at an interval of interval."""
        y = []
        st = fr
        while st < ut:
            getamo = str(interval)
            lena = len(getamo)
            pos = getamo.index('.')
            getamo = lena - pos - 1
            getamo1 = str(fr)
            lena1 = len(getamo1)
            pos1 = getamo1.index('.')
            getamo1 = lena1 - pos1 - 1
            if getamo > getamo1:
                y.append(round(st, getamo))
            elif getamo <= getamo1:
                y.append(round(st, getamo1))
            st = st + interval
        return y

    def e(self, x: int):
        """This will calculate e up to n digits. This uses Decimal for better precision than float."""
        getcontext().prec = x
        e = Decimal(0)
        f = Decimal(1)
        n = Decimal(1)
        while True:
            olde = e
            e += Decimal(1) / f
            if e == olde:
                break
            f *= n
            n += Decimal(1)
        return Decimal(e)

    def eFloat(self, x: int):
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""
        getcontext().prec = x
        e = Decimal(0)
        f = Decimal(1)
        n = Decimal(1)
        while True:
            olde = e
            e += Decimal(1) / f
            if e == olde:
                break
            f *= n
            n += Decimal(1)
        return float(e)

    def sin(self, n: float, mode='rad'):
        """This will calculate the sin of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """
        if mode == 'rad':
            return (self.eFloat(100) ** (n * 1j)).imag
        elif mode == 'deg':
            return (self.eFloat(100) ** (self.degrees(n) * 1j)).imag
        else:
            return MathError('Invalid mode, select rad or deg.', self.console)
    
    def cos(self, n: float, mode='rad'):
        """This will calculate the cos of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """
        if mode == 'rad':
            return (self.eFloat(100) ** (n * 1j)).real
        elif mode == 'deg':
            return (self.eFloat(100) ** (self.degrees(n) * 1j)).real
        else:
            return MathError('Invalid mode, select rad or deg.', self.console)

    def tan(self, n: float, mode='rad'):
        """This will calculate the tan of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """
        if mode == 'rad':
            return self.sin(n, mode)/self.cos(n, mode)
        elif mode == 'deg':
            return self.sin(self.degrees(n), mode)/self.cos(self.degrees(n), mode)
        else:
            return MathError('Invalid mode, select rad or deg.', self.console)

    def cot(self, n: float, mode='rad'):
        """This will calculate the cot of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """
        if mode == 'rad':
            return self.cos(n, mode)/self.sin(n, mode)
        elif mode == 'deg':
            return self.cos(self.degrees(n), mode)/self.sin(self.degrees(n), mode)
        else:
            return MathError('Invalid mode, select rad or deg.', self.console)

    def log(self, x, b):
        """This will calculate the log of x of base b."""
        result = self.ln(x)/self.ln(b)
        return result

    def ln(self, x):
        """This will calculate the log of e of x, or it calculate the natural log of x."""
        val = x
        return 99999999*(x**(1/99999999)-1)

    def radians(self, r: float):
        """This will convert degrees into radians mathematically."""
        pi = self.piFloat(100)
        return r * pi / 180
    
    def degrees(self, r: float):
        """This will convert radians into degrees mathematically."""
        pi = self.piFloat(100)
        return r * 180 / pi

    def gcd(self, x, y):
        """This will calculate the greatest common denominator, or gcd for x and y."""
        while y != 0:
            (x, y) = (y, x % y)
        return x

    def fraction(self, x: float):
        """This will return the fraction of a float."""

        if (len(str(x)) > 25):
            MathError('You cannot have that big of a decimal or else I will crash ')
        xstr = str(x)
        length = len(xstr)
        if ( not ('.' in xstr)):
            return MathError('Not valid number')
        
        pos = xstr.index('.')

        pow10 = 10 ** (length - pos - 1)

        numx = x * pow10

        common = self.gcd(numx, pow10)

        if (common == None):
            return f'{int(round(numx))}/{int(pow10)}'

        return [int(round(numx) / common), int(pow10 / common)]
    
    @property
    def __version(self):
        """This will return the version of the math library in a tuple."""
        return (2, 3, 1)

class String():
    """This is a class for manipulating strings. This doesn't have much right now except for reverse a string."""
    def __init__(self, consolas = False):
        with open(f'QuexMath.pyi', 'w') as f:
            f.write('''"""

/*----------------------------------------------------------------------------------------------*
*   Copyright (c) Queryzi Inc. All rights reserved.
*   You may not decompile this software (the QuexMath.pyd file) without permittance of Queryzi Inc.
/*----------------------------------------------------------------------------------------------*

This is a math class, that does not replace the already exisiting math class for python.
This provides a bit more features than the python math library as it has HEX - Decimal, and binary conversion. 
This class is similar to the python math library, but aims to add more features, and has a bit more features. 

This library is written by Queryzi.

"""

from decimal import Decimal

class BaseMathConsoleError(Exception):
    """This is the basemath console error exception and it inherits Exception."""

    def __init__(self, message) -> None: ...

class BaseMathGuiError():
    """This is the basemath GUI error exception and it inherits Exception."""

    def __init__(self, message, consolas = False) -> None: ...

def getType(x): ...
    """This returns the type of x."""

class MathError():
    """This is the math error class, and it raises a error."""
    def __init__(self, message, console = False) -> None: ...

class Math():
    """This is a math library of basic math functions. This is a math class created by Queryzi."""

    def divide(self, x: float, y: float) -> float: ...
        """Divide two numbers by eachother, divide x by y."""

    def range(self, x: int) -> list: ...
        """Generate a range from 0 to x, where x is a integer."""

    def combination(self, n: int, r: int) -> float: ...
        """This calculates the amount of combinations for n of r."""

    def permutation(self, n: int, r: int, repeat=False) -> float: ...
        """This calculates the amount of permutations for n of r."""

    def factorial(self, x: int) -> int: ...
        """This calculates the factorial of x. Example is 9, 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1."""

    def multiply(self, x: float, y: float) -> float: ...
        """Multiply two numbers by eachother, multiply x by y."""

    def factors(self, n) -> list: ...
        """Gets the factors of n."""

    def pi(self, n: int) -> Decimal: ...
        """This will calculate pi up to n digits. This uses Decimal for better precision than float."""

    def piFloat(self, n: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def getArray(self, fr: float, ut: float, interval: float) -> list: ...
        """Returns a list starting from fr, and ends at ut, at an interval of interval."""

    def e(self, x: int) -> Decimal: ...
        """This will calculate e up to n digits. This uses Decimal for better precision than float."""

    def eFloat(self, x: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def sin(self, n: float, mode='rad') -> float: ...
        """This will calculate the sin of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cos(self, n: float, mode='rad') -> float: ...
        """This will calculate the cos of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def tan(self, n: float, mode='rad') -> float: ...
        """This will calculate the tan of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cot(self, n: float, mode='rad') -> float: ...
        """This will calculate the cot of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def log(self, x, b) -> float: ...
        """This will calculate the log of x of base b."""

    def ln(self, x) -> float: ...
        """This will calculate the log of e of x, or it calculate the natural log of x."""

    def radians(self, r: float) -> float: ...
        """This will convert degrees into radians mathematically."""

    def degrees(self, r: float) -> float: ...
        """This will convert radians into degrees mathematically."""

    def gcd(self, x, y) -> int: ...
        """This will calculate the greatest common denominator, or gcd for x and y."""

    def fraction(self, x: float) -> list: ...
        """This will return the fraction of a float."""

    @property
    def __version(self) -> tuple: ...
        """This will return the version of the math library in a tuple."""

class String():
    """This is a class for manipulating strings. This doesn't have much right now except for reverse a string."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, string: str) -> str: ...
        """Reverses a string efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Array():
    """This is a class for manipulating arrays. This doesn't have much right now except for reverse a array."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, array: list) -> list: ...
        """Reverses a array efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Binary(Math):
    """This is a class for binary conversions between decimal and text conversions."""
    
    def __init__(self, consolas = False) -> None: ...

    def texttoBinary(self, x: str) -> str: ...
        """This converts text to binary using the ord() function and converting to binary."""

    def Binarytotext(self, x: str) -> str: ...
        """Convert binary to text. This will convert it using chr and convert Binary to int and return the string."""

    def InttoBinary(self, x: int) -> int: ...
        """This will convert a integer to binary."""

    def toDecimal(self, x: int) -> int: ...
        """Convert binary to decimal (integer with base 10)."""

    @property
    def __version(self) -> tuple:
        """Returns the version of this class."""

class Hexadecimal:
    """A class for hexadecimal conversions with int to hexadecimal and hexadecimal to int, or base 16 to base 10, and base 10 to base 16."""

    def __init__(self, consolas = False) -> None: ...

    def InttoHexa(self, x: int) -> str: ...
        """Convert integer or decimal with base 10, and convert it to hexadecimal with base 16."""

    def HexatoInt(self, x: str) -> int: ...
        """Convert Hexa decimal to integer, or convert base 16 to base 10."""

    def texttoHexa(self, x: str) -> str: ...
        """Converts text to hexadecimal. This uses ASCII encoding."""

    def HexatoText(self, x: str) -> str: ...
        """This will convert hexadecimal string to a text string using ascii encoding."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""''')
            f.close()

    def reverse(self, string: str):
        """Reverses a string efficiently."""
        l = len(string)
        newstr = ""
        while l != 0:
            newstr += string[l - 1]
            l = l - 1
        
        return newstr
    
    @property
    def __version(self):
        """Returns the version of this class."""
        return (1, 0, 0)

class Array():
    """This is a class for manipulating arrays. This doesn't have much right now except for reverse a array."""
    def __init__(self, consolas = False):
        with open(f'QuexMath.pyi', 'w') as f:
            f.write('''"""

/*----------------------------------------------------------------------------------------------*
*   Copyright (c) Queryzi Inc. All rights reserved.
*   You may not decompile this software (the QuexMath.pyd file) without permittance of Queryzi Inc.
/*----------------------------------------------------------------------------------------------*

This is a math class, that does not replace the already exisiting math class for python.
This provides a bit more features than the python math library as it has HEX - Decimal, and binary conversion. 
This class is similar to the python math library, but aims to add more features, and has a bit more features. 

This library is written by Queryzi.

"""

from decimal import Decimal

class BaseMathConsoleError(Exception):
    """This is the basemath console error exception and it inherits Exception."""

    def __init__(self, message) -> None: ...

class BaseMathGuiError():
    """This is the basemath GUI error exception and it inherits Exception."""

    def __init__(self, message, consolas = False) -> None: ...

def getType(x): ...
    """This returns the type of x."""

class MathError():
    """This is the math error class, and it raises a error."""
    def __init__(self, message, console = False) -> None: ...

class Math():
    """This is a math library of basic math functions. This is a math class created by Queryzi."""

    def divide(self, x: float, y: float) -> float: ...
        """Divide two numbers by eachother, divide x by y."""

    def range(self, x: int) -> list: ...
        """Generate a range from 0 to x, where x is a integer."""

    def combination(self, n: int, r: int) -> float: ...
        """This calculates the amount of combinations for n of r."""

    def permutation(self, n: int, r: int, repeat=False) -> float: ...
        """This calculates the amount of permutations for n of r."""

    def factorial(self, x: int) -> int: ...
        """This calculates the factorial of x. Example is 9, 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1."""

    def multiply(self, x: float, y: float) -> float: ...
        """Multiply two numbers by eachother, multiply x by y."""

    def factors(self, n) -> list: ...
        """Gets the factors of n."""

    def pi(self, n: int) -> Decimal: ...
        """This will calculate pi up to n digits. This uses Decimal for better precision than float."""

    def piFloat(self, n: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def getArray(self, fr: float, ut: float, interval: float) -> list: ...
        """Returns a list starting from fr, and ends at ut, at an interval of interval."""

    def e(self, x: int) -> Decimal: ...
        """This will calculate e up to n digits. This uses Decimal for better precision than float."""

    def eFloat(self, x: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def sin(self, n: float, mode='rad') -> float: ...
        """This will calculate the sin of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cos(self, n: float, mode='rad') -> float: ...
        """This will calculate the cos of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def tan(self, n: float, mode='rad') -> float: ...
        """This will calculate the tan of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cot(self, n: float, mode='rad') -> float: ...
        """This will calculate the cot of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def log(self, x, b) -> float: ...
        """This will calculate the log of x of base b."""

    def ln(self, x) -> float: ...
        """This will calculate the log of e of x, or it calculate the natural log of x."""

    def radians(self, r: float) -> float: ...
        """This will convert degrees into radians mathematically."""

    def degrees(self, r: float) -> float: ...
        """This will convert radians into degrees mathematically."""

    def gcd(self, x, y) -> int: ...
        """This will calculate the greatest common denominator, or gcd for x and y."""

    def fraction(self, x: float) -> list: ...
        """This will return the fraction of a float."""

    @property
    def __version(self) -> tuple: ...
        """This will return the version of the math library in a tuple."""

class String():
    """This is a class for manipulating strings. This doesn't have much right now except for reverse a string."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, string: str) -> str: ...
        """Reverses a string efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Array():
    """This is a class for manipulating arrays. This doesn't have much right now except for reverse a array."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, array: list) -> list: ...
        """Reverses a array efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Binary(Math):
    """This is a class for binary conversions between decimal and text conversions."""
    
    def __init__(self, consolas = False) -> None: ...

    def texttoBinary(self, x: str) -> str: ...
        """This converts text to binary using the ord() function and converting to binary."""

    def Binarytotext(self, x: str) -> str: ...
        """Convert binary to text. This will convert it using chr and convert Binary to int and return the string."""

    def InttoBinary(self, x: int) -> int: ...
        """This will convert a integer to binary."""

    def toDecimal(self, x: int) -> int: ...
        """Convert binary to decimal (integer with base 10)."""

    @property
    def __version(self) -> tuple:
        """Returns the version of this class."""

class Hexadecimal:
    """A class for hexadecimal conversions with int to hexadecimal and hexadecimal to int, or base 16 to base 10, and base 10 to base 16."""

    def __init__(self, consolas = False) -> None: ...

    def InttoHexa(self, x: int) -> str: ...
        """Convert integer or decimal with base 10, and convert it to hexadecimal with base 16."""

    def HexatoInt(self, x: str) -> int: ...
        """Convert Hexa decimal to integer, or convert base 16 to base 10."""

    def texttoHexa(self, x: str) -> str: ...
        """Converts text to hexadecimal. This uses ASCII encoding."""

    def HexatoText(self, x: str) -> str: ...
        """This will convert hexadecimal string to a text string using ascii encoding."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""''')
            f.close()

    def reverse(self, array: list):
        """Reverses a array efficiently."""
        l = len(array)
        newlist = []
        while l != 0:
            newlist.append(array[l - 1])
            l = l - 1
        
        return newlist
    
    @property
    def __version(self):
        """Returns the version of this class."""
        return (1, 0, 1)

class Binary(Math):
    """This is a class for binary conversions between decimal and text conversions."""
    
    def __init__(self, consolas = False):
        with open(f'QuexMath.pyi', 'w') as f:
            f.write('''"""

/*----------------------------------------------------------------------------------------------*
*   Copyright (c) Queryzi Inc. All rights reserved.
*   You may not decompile this software (the QuexMath.pyd file) without permittance of Queryzi Inc.
/*----------------------------------------------------------------------------------------------*

This is a math class, that does not replace the already exisiting math class for python.
This provides a bit more features than the python math library as it has HEX - Decimal, and binary conversion. 
This class is similar to the python math library, but aims to add more features, and has a bit more features. 

This library is written by Queryzi.

"""

from decimal import Decimal

class BaseMathConsoleError(Exception):
    """This is the basemath console error exception and it inherits Exception."""

    def __init__(self, message) -> None: ...

class BaseMathGuiError():
    """This is the basemath GUI error exception and it inherits Exception."""

    def __init__(self, message, consolas = False) -> None: ...

def getType(x): ...
    """This returns the type of x."""

class MathError():
    """This is the math error class, and it raises a error."""
    def __init__(self, message, console = False) -> None: ...

class Math():
    """This is a math library of basic math functions. This is a math class created by Queryzi."""

    def divide(self, x: float, y: float) -> float: ...
        """Divide two numbers by eachother, divide x by y."""

    def range(self, x: int) -> list: ...
        """Generate a range from 0 to x, where x is a integer."""

    def combination(self, n: int, r: int) -> float: ...
        """This calculates the amount of combinations for n of r."""

    def permutation(self, n: int, r: int, repeat=False) -> float: ...
        """This calculates the amount of permutations for n of r."""

    def factorial(self, x: int) -> int: ...
        """This calculates the factorial of x. Example is 9, 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1."""

    def multiply(self, x: float, y: float) -> float: ...
        """Multiply two numbers by eachother, multiply x by y."""

    def factors(self, n) -> list: ...
        """Gets the factors of n."""

    def pi(self, n: int) -> Decimal: ...
        """This will calculate pi up to n digits. This uses Decimal for better precision than float."""

    def piFloat(self, n: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def getArray(self, fr: float, ut: float, interval: float) -> list: ...
        """Returns a list starting from fr, and ends at ut, at an interval of interval."""

    def e(self, x: int) -> Decimal: ...
        """This will calculate e up to n digits. This uses Decimal for better precision than float."""

    def eFloat(self, x: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def sin(self, n: float, mode='rad') -> float: ...
        """This will calculate the sin of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cos(self, n: float, mode='rad') -> float: ...
        """This will calculate the cos of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def tan(self, n: float, mode='rad') -> float: ...
        """This will calculate the tan of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cot(self, n: float, mode='rad') -> float: ...
        """This will calculate the cot of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def log(self, x, b) -> float: ...
        """This will calculate the log of x of base b."""

    def ln(self, x) -> float: ...
        """This will calculate the log of e of x, or it calculate the natural log of x."""

    def radians(self, r: float) -> float: ...
        """This will convert degrees into radians mathematically."""

    def degrees(self, r: float) -> float: ...
        """This will convert radians into degrees mathematically."""

    def gcd(self, x, y) -> int: ...
        """This will calculate the greatest common denominator, or gcd for x and y."""

    def fraction(self, x: float) -> list: ...
        """This will return the fraction of a float."""

    @property
    def __version(self) -> tuple: ...
        """This will return the version of the math library in a tuple."""

class String():
    """This is a class for manipulating strings. This doesn't have much right now except for reverse a string."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, string: str) -> str: ...
        """Reverses a string efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Array():
    """This is a class for manipulating arrays. This doesn't have much right now except for reverse a array."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, array: list) -> list: ...
        """Reverses a array efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Binary(Math):
    """This is a class for binary conversions between decimal and text conversions."""
    
    def __init__(self, consolas = False) -> None: ...

    def texttoBinary(self, x: str) -> str: ...
        """This converts text to binary using the ord() function and converting to binary."""

    def Binarytotext(self, x: str) -> str: ...
        """Convert binary to text. This will convert it using chr and convert Binary to int and return the string."""

    def InttoBinary(self, x: int) -> int: ...
        """This will convert a integer to binary."""

    def toDecimal(self, x: int) -> int: ...
        """Convert binary to decimal (integer with base 10)."""

    @property
    def __version(self) -> tuple:
        """Returns the version of this class."""

class Hexadecimal:
    """A class for hexadecimal conversions with int to hexadecimal and hexadecimal to int, or base 16 to base 10, and base 10 to base 16."""

    def __init__(self, consolas = False) -> None: ...

    def InttoHexa(self, x: int) -> str: ...
        """Convert integer or decimal with base 10, and convert it to hexadecimal with base 16."""

    def HexatoInt(self, x: str) -> int: ...
        """Convert Hexa decimal to integer, or convert base 16 to base 10."""

    def texttoHexa(self, x: str) -> str: ...
        """Converts text to hexadecimal. This uses ASCII encoding."""

    def HexatoText(self, x: str) -> str: ...
        """This will convert hexadecimal string to a text string using ascii encoding."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""''')
            f.close()

    def texttoBinary(self, x: str):
        """This converts text to binary using the ord() function and converting to binary."""

        lista=[ord(ch) for ch in x]
        binary = []
        for i in range(len(lista)):
            binary.append(str(self.InttoBinary(lista[i])))
        
        return " ".join(binary)
    
    def Binarytotext(self, x: str):
        """Convert binary to text. This will convert it using chr and convert Binary to int and return the string."""
        
        try:
            binary = x.split(' ')
            string = ''
            for i in range(len(binary)):
                string += chr(self.toDecimal(int(binary[i])))
            
            return string
        except Exception as e:
            MathError(e, False)

    def InttoBinary(self, x: int):
        """This will convert a integer to binary."""
        if x == 0:
            return 0
        k = x
        kx = x
        if '-' in str(k):
            k = k * -1
        
        addto = []
        while k != 1:
            addto.append(str(k % 2))
            k = k // 2
        
        addto.append(str(1))

        if '-' in str(kx):
            return int("".join(Array().reverse(addto))) * -1
        else:
            return int("".join(Array().reverse(addto)))

    # def textoMorse(self, x: str):
    #     return self.texttoBinary(x).replace('0', '.').replace('1', '-').replace(' ', '/')
    
    # def Morsetotext(self, x: str):
    #     return self.Binarytotext(x.replace('.', '0').replace('-', '1').replace('/', ' '))

    def toDecimal(self, x: int):
        """Convert binary to decimal (integer with base 10)."""
        if x == 0:
            return 0
        binary = x
        binarya = x
        if '-' in str(binary):
            binary = binary * -1
        binary1 = binary
        decimal, i, n = 0, 0, 0
        while (binary != 0):
            dec = binary % 10
            decimal = decimal + dec * pow(2, i)
            binary = binary // 10
            i += 1
        
        if '-' in str(binarya):
            return decimal * -1
        else:
            return decimal
    
    @property
    def __version(self):
        """Returns the version of this class."""
        return (1, 3, 4)

class Hexadecimal:
    """A class for hexadecimal conversions with int to hexadecimal and hexadecimal to int, or base 16 to base 10, and base 10 to base 16."""

    def __init__(self, consolas = False):
        with open(f'QuexMath.pyi', 'w') as f:
            f.write('''"""

/*----------------------------------------------------------------------------------------------*
*   Copyright (c) Queryzi Inc. All rights reserved.
*   You may not decompile this software (the QuexMath.pyd file) without permittance of Queryzi Inc.
/*----------------------------------------------------------------------------------------------*

This is a math class, that does not replace the already exisiting math class for python.
This provides a bit more features than the python math library as it has HEX - Decimal, and binary conversion. 
This class is similar to the python math library, but aims to add more features, and has a bit more features. 

This library is written by Queryzi.

"""

from decimal import Decimal

class BaseMathConsoleError(Exception):
    """This is the basemath console error exception and it inherits Exception."""

    def __init__(self, message) -> None: ...

class BaseMathGuiError():
    """This is the basemath GUI error exception and it inherits Exception."""

    def __init__(self, message, consolas = False) -> None: ...

def getType(x): ...
    """This returns the type of x."""

class MathError():
    """This is the math error class, and it raises a error."""
    def __init__(self, message, console = False) -> None: ...

class Math():
    """This is a math library of basic math functions. This is a math class created by Queryzi."""

    def divide(self, x: float, y: float) -> float: ...
        """Divide two numbers by eachother, divide x by y."""

    def range(self, x: int) -> list: ...
        """Generate a range from 0 to x, where x is a integer."""

    def combination(self, n: int, r: int) -> float: ...
        """This calculates the amount of combinations for n of r."""

    def permutation(self, n: int, r: int, repeat=False) -> float: ...
        """This calculates the amount of permutations for n of r."""

    def factorial(self, x: int) -> int: ...
        """This calculates the factorial of x. Example is 9, 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1."""

    def multiply(self, x: float, y: float) -> float: ...
        """Multiply two numbers by eachother, multiply x by y."""

    def factors(self, n) -> list: ...
        """Gets the factors of n."""

    def pi(self, n: int) -> Decimal: ...
        """This will calculate pi up to n digits. This uses Decimal for better precision than float."""

    def piFloat(self, n: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def getArray(self, fr: float, ut: float, interval: float) -> list: ...
        """Returns a list starting from fr, and ends at ut, at an interval of interval."""

    def e(self, x: int) -> Decimal: ...
        """This will calculate e up to n digits. This uses Decimal for better precision than float."""

    def eFloat(self, x: int) -> float: ...
        """This will calculate pi up to n digits, but this uses float so it is heavily limited."""

    def sin(self, n: float, mode='rad') -> float: ...
        """This will calculate the sin of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cos(self, n: float, mode='rad') -> float: ...
        """This will calculate the cos of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def tan(self, n: float, mode='rad') -> float: ...
        """This will calculate the tan of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def cot(self, n: float, mode='rad') -> float: ...
        """This will calculate the cot of n, in radians or degrees depending on the mode.
        
        Modes
            - Degrees is deg
            - Radians is rad
        """

    def log(self, x, b) -> float: ...
        """This will calculate the log of x of base b."""

    def ln(self, x) -> float: ...
        """This will calculate the log of e of x, or it calculate the natural log of x."""

    def radians(self, r: float) -> float: ...
        """This will convert degrees into radians mathematically."""

    def degrees(self, r: float) -> float: ...
        """This will convert radians into degrees mathematically."""

    def gcd(self, x, y) -> int: ...
        """This will calculate the greatest common denominator, or gcd for x and y."""

    def fraction(self, x: float) -> list: ...
        """This will return the fraction of a float."""

    @property
    def __version(self) -> tuple: ...
        """This will return the version of the math library in a tuple."""

class String():
    """This is a class for manipulating strings. This doesn't have much right now except for reverse a string."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, string: str) -> str: ...
        """Reverses a string efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Array():
    """This is a class for manipulating arrays. This doesn't have much right now except for reverse a array."""
    def __init__(self, consolas = False) -> None: ...

    def reverse(self, array: list) -> list: ...
        """Reverses a array efficiently."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""

class Binary(Math):
    """This is a class for binary conversions between decimal and text conversions."""
    
    def __init__(self, consolas = False) -> None: ...

    def texttoBinary(self, x: str) -> str: ...
        """This converts text to binary using the ord() function and converting to binary."""

    def Binarytotext(self, x: str) -> str: ...
        """Convert binary to text. This will convert it using chr and convert Binary to int and return the string."""

    def InttoBinary(self, x: int) -> int: ...
        """This will convert a integer to binary."""

    def toDecimal(self, x: int) -> int: ...
        """Convert binary to decimal (integer with base 10)."""

    @property
    def __version(self) -> tuple:
        """Returns the version of this class."""

class Hexadecimal:
    """A class for hexadecimal conversions with int to hexadecimal and hexadecimal to int, or base 16 to base 10, and base 10 to base 16."""

    def __init__(self, consolas = False) -> None: ...

    def InttoHexa(self, x: int) -> str: ...
        """Convert integer or decimal with base 10, and convert it to hexadecimal with base 16."""

    def HexatoInt(self, x: str) -> int: ...
        """Convert Hexa decimal to integer, or convert base 16 to base 10."""

    def texttoHexa(self, x: str) -> str: ...
        """Converts text to hexadecimal. This uses ASCII encoding."""

    def HexatoText(self, x: str) -> str: ...
        """This will convert hexadecimal string to a text string using ascii encoding."""

    @property
    def __version(self) -> tuple: ...
        """Returns the version of this class."""''')
            f.close()

    def InttoHexa(self, x: int):
        """Convert integer or decimal with base 10, and convert it to hexadecimal with base 16."""
        if x == 0:
            return 0
        k = x
        kx = x
        addto = []
        if '-' in str(k):
            k = k * -1
            addto.append('-')

        while k != 0:
            stored = k % 16
            if stored < 10:
                addto.append(str(stored))
            elif stored >= 10 < 16:
                pos = stored - 9
                addto.append("ABCDEF"[pos - 1])
            else:
                return
            k = k // 16

        if '-' in str(kx):
            return "".join(Array().reverse(addto))
        else:
            return "".join(Array().reverse(addto))

    def HexatoInt(self, x: str):
        """Convert Hexa decimal to integer, or convert base 16 to base 10."""
        decimal = 0
        for i, d in enumerate(x):
            strnot = 'abcdefghijklmnopqrstuvwxyzGHIJKLMNOPQRSTUVWXYZ'
            hexindex = "0123456789ABCDEF"
            index = hexindex.index(d)

            power = (len(x) - (i + 1))
            decimal += (index*(16**power))
        
        return decimal
    
    def texttoHexa(self, x: str):
        """Converts text to hexadecimal. This uses ASCII."""
        dalist = []
        for i in range(len(x)):
            dalist.append(self.InttoHexa(ord(x[i])))
        
        return " ".join(dalist)
    
    def HexatoText(self, x: str):
        """This will convert hexadecimal string to a text string using ascii encoding."""

        dalist = x.split(' ')
        newa = ''
        for i in range(len(dalist)):
            newa += chr(self.HexatoInt(dalist[i]))
        
        return newa

    @property
    def __version(self):
        """Returns the version of this class."""
        return (1, 1, 9)

if __name__ == '__main__':
    pass