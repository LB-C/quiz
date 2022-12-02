import check50
import check50.c

@check50.check()
def exists():
    """age.c exists"""
    check50.exists("age.c")

@check50.check(exists)
def compiles():
    """age.c compiles"""
    check50.c.compile("age.c", lcs50=True)

@check50.check(compiles)
def all_three_colors_match_same_case():
    """all three colors match when entered in the same way"""
    check50.run("./color").stdin("Pink").stdin("Pink").stdin("Pink").stdout("Everyone likes the same color!\n", regex=False).exit(0)

@check50.check(compiles)
def all_three_colors_match_diff_case():
    """all three colors match when entered in different cases"""
    check50.run("./color").stdin("Pink").stdin("pink").stdin("PINK").stdout("Everyone likes the same color!\n", regex=False).exit(0)

@check50.check(compiles)
def color1_and_color2_match():
    """color1 and color2 match"""
    check50.run("./color").stdin("Pink").stdin("pink").stdin("Red").stdout("Two people like the same color!\n", regex=False).exit(0)
    
@check50.check(compiles)
def color1_and_color3_match():
    """color1 and color3 match"""
    check50.run("./color").stdin("Pink").stdin("Red").stdin("pink").stdout("Two people like the same color!\n", regex=False).exit(0)
    
@check50.check(compiles)
def color2_and_color3_match():
    """color2 and color3 match"""
    check50.run("./color").stdin("Red").stdin("Pink").stdin("pink").stdout("Two people like the same color!\n", regex=False).exit(0)
    
@check50.check(compiles)
def no_colors_match():
    """no colors match"""
    check50.run("./color").stdin("Pink").stdin("red").stdin("BLUE").stdout("No one likes the same color!\n", regex=False).exit(0)
