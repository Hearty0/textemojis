import emojis
import keyboard

es = emojis

mainkey = ('ctrl + shift + ')

try:
    print("founded " + str(emojis.count) + " emoji")
    print("for " + "(" + es.e1[2] + ")    "  + " press " + mainkey + es.e1[0])# + "     " + es.e1[1])
    print("for " + "(" + es.e2[2] + ")    "  + " press " + mainkey + es.e2[0])# + "     " + es.e2[1])
    print("for " + "(" + es.e3[2] + ")    "  + " press " + mainkey + es.e3[0])# + "     " + es.e3[1])
    print("for " + "(" + es.e4[2] + ")    "  + " press " + mainkey + es.e4[0])# + "     " + es.e4[1])
    print("for " + "(" + es.e5[2] + ")    "  + " press " + mainkey + es.e5[0])# + "     " + es.e5[1])
    print("for " + "(" + es.e6[2] + ")    "  + " press " + mainkey + es.e6[0])# + "     " + es.e6[1])
    print("for " + "(" + es.e7[2] + ")    "  + " press " + mainkey + es.e7[0])# + "     " + es.e7[1])
    print("for " + "(" + es.e8[2] + ")    "  + " press " + mainkey + es.e8[0])# + "     " + es.e8[1])
    print("for " + "(" + es.e9[2] + ")    "  + " press " + mainkey + es.e9[0])# + "     " + es.e9[1])
    print("for " + "(" + es.e10[2] + ")    "  + " press " + mainkey + es.e10[0])# + "     " + es.e10[1])
    print("for " + "(" + es.e11[2] + ")    "  + " press " + mainkey + es.e11[0])# + "     " + es.e11[1])
    print("for " + "(" + es.e12[2] + ")    "  + " press " + mainkey + es.e12[0])# + "     " + es.e12[1])
    print("for " + "(" + es.e13[2] + ")    "  + " press " + mainkey + es.e13[0])# + "     " + es.e13[1])
    print("for " + "(" + es.e14[2] + ")    "  + " press " + mainkey + es.e14[0])# + "     " + es.e14[1])
    print("for " + "(" + es.e15[2] + ")    "  + " press " + mainkey + es.e15[0])# + "     " + es.e15[1])
    print("for " + "(" + es.e16[2] + ")    "  + " press " + mainkey + es.e16[0])# + "     " + es.e16[1])
    print("for " + "(" + es.e17[2] + ")    "  + " press " + mainkey + es.e17[0])# + "     " + es.e17[1])
    print("for " + "(" + es.e18[2] + ")    "  + " press " + mainkey + es.e18[0])# + "     " + es.e18[1])
    print("\nif you wan't set new emoji type \"new\" in console")

except AttributeError:
    pass

try:
    keyboard.add_hotkey((mainkey + es.e1[0]), lambda: keyboard.write(es.e1[1]))
    keyboard.add_hotkey((mainkey + es.e2[0]), lambda: keyboard.write(es.e2[1]))
    keyboard.add_hotkey((mainkey + es.e3[0]), lambda: keyboard.write(es.e3[1]))
    keyboard.add_hotkey((mainkey + es.e4[0]), lambda: keyboard.write(es.e4[1]))
    keyboard.add_hotkey((mainkey + es.e5[0]), lambda: keyboard.write(es.e5[1]))
    keyboard.add_hotkey((mainkey + es.e6[0]), lambda: keyboard.write(es.e6[1]))
    keyboard.add_hotkey((mainkey + es.e7[0]), lambda: keyboard.write(es.e7[1]))
    keyboard.add_hotkey((mainkey + es.e8[0]), lambda: keyboard.write(es.e8[1]))
    keyboard.add_hotkey((mainkey + es.e9[0]), lambda: keyboard.write(es.e9[1]))
    keyboard.add_hotkey((mainkey + es.e10[0]), lambda: keyboard.write(es.e10[1]))
    keyboard.add_hotkey((mainkey + es.e11[0]), lambda: keyboard.write(es.e11[1]))
    keyboard.add_hotkey((mainkey + es.e12[0]), lambda: keyboard.write(es.e12[1]))
    keyboard.add_hotkey((mainkey + es.e13[0]), lambda: keyboard.write(es.e13[1]))
    keyboard.add_hotkey((mainkey + es.e14[0]), lambda: keyboard.write(es.e14[1]))
    keyboard.add_hotkey((mainkey + es.e15[0]), lambda: keyboard.write(es.e15[1]))
    keyboard.add_hotkey((mainkey + es.e16[0]), lambda: keyboard.write(es.e16[1]))
    keyboard.add_hotkey((mainkey + es.e17[0]), lambda: keyboard.write(es.e17[1]))
    keyboard.add_hotkey((mainkey + es.e18[0]), lambda: keyboard.write(es.e18[1]))
except AttributeError:
    pass


keyboard.wait() 