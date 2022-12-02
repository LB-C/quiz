import check50
import check50.c

@check50.check()
def exists():
    """ages.c exists"""
    check50.exists("ages.c")

@check50.check(exists)
def compiles():
    """ages.c compiles"""
    check50.c.compile("ages.c", lcs50=True)

@check50.check(compiles)
def years_diff_months_match_days_match():
    """correctly sorts all tas when the years are different"""
    check50.run("./ages").stdin("4").stdin("Simon").stdin("1").stdin("1").stdin("2003").stdin("Lyra").stdin("1").stdin("1").stdin("2005").stdin("Olivia").stdin("1").stdin("1").stdin("2004").stdin("Audrey").stdin("1").stdin("1").stdin("2006").stdout("Simon\nOlivia\nLyra\nAudrey\n", regex=False).exit(0)

@check50.check(compiles)
def years_match_months_diff_days_match():
    """correctly sorts all tas when years are the same but the months are different"""
    check50.run("./ages").stdin("4").stdin("Simon").stdin("3").stdin("1").stdin("2005").stdin("Lyra").stdin("2").stdin("1").stdin("2005").stdin("Olivia").stdin("5").stdin("1").stdin("2005").stdin("Audrey").stdin("7").stdin("1").stdin("2005").stdout("Lyra\nSimon\nOlivia\nAudrey\n", regex=False).exit(0)

@check50.check(compiles)
def years_match_months_match_days_diff():
    """correctly sorts all tas when some years and months are the same but the days are different"""
    check50.run("./ages").stdin("4").stdin("Simon").stdin("5").stdin("23").stdin("2005").stdin("Lyra").stdin("5").stdin("12").stdin("2005").stdin("Olivia").stdin("5").stdin("19").stdin("2005").stdin("Audrey").stdin("5").stdin("3").stdin("2005").stdout("Audrey\nLyra\nOlivia\nSimon\n", regex=False).exit(0)
    
@check50.check(compiles)
def not_all_match:
    """color1 and color3 match"""
    check50.run("./ages").stdin("4").stdin("Simon").stdin("1").stdin("1").stdin("2003").stdin("Lyra").stdin("1").stdin("1").stdin("2005").stdin("Olivia").stdin("1").stdin("1").stdin("2004").stdin("Audrey").stdin("1").stdin("1").stdin("2006").stdout("Simon\nOlivia\nLyra\nAudrey\n", regex=False).exit(0)
    
@check50.check(compiles)
def color2_and_color3_match():
    """color2 and color3 match"""
    check50.run("./color").stdin("Red").stdin("Pink").stdin("pink").stdout("Two people like the same color!\n", regex=False).exit(0)
    
@check50.check(compiles)
def no_colors_match():
    """no colors match"""
    check50.run("./color").stdin("Pink").stdin("red").stdin("BLUE").stdout("No one likes the same color!\n", regex=False).exit(0)
