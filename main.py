#Working with Tuples for SW2
from pyscript import display, document # type: ignore (quick fix feature)

def computing_grades(e):
    fname = document.getElementById('fname').value
    lname = document.getElementById('lname').value
    gr1 = int(document.getElementById('gr1').value)
    gr2 = int(document.getElementById('gr2').value)
    gr3 = int(document.getElementById('gr3').value)
    gr4 = int(document.getElementById('gr4').value)
    gr5 = int(document.getElementById('gr5').value)
    gr6 = int(document.getElementById('gr6').value)
    grades = [gr1, gr2, gr3, gr4, gr5, gr6]
    units = (5,3,1)
    sci = (grades [0] * units[0])
    ss = (grades [1] * units[1])
    math = (grades [2] * units[0])
    eng = (grades [3] * units[0])
    ve = (grades [4] * units[2])
    tle = (grades [5] * units[2])
    total_sum = sci + ss + math + eng + ve + tle
    total_unit= (units[0] * 3) + (units[1]) + (units[2] * 2)
    gwa = total_sum / total_unit

    display (f"{fname} + {lname}", target="output")
    display (f"{gr1} , {gr2} , {gr3} , {gr4} , {gr5} , {gr6}", target="output")
    display (f"You're Generat Weighted Average is {gwa}.", target="output")


