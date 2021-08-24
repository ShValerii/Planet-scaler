k = 1000000
earth = float(input("Enter the size of the Earth you want to see in cm: "))
#earth = 1274200000
scale = (12742000 / earth)
sun = round(109.25 * earth,2)
mercury = round(0.38291 * earth,2)
venus = round(0.94986 * earth,2)
moon = round(0.272657 * earth,2)
mars = round(0.5321 * earth,2)
jupiter = round(10.97335 * earth,2)
saturn = round(9.1402 * earth,2)
uranus = round(3.9809 * earth,2)
neptune = round(3.8647 * earth,2)
dearthmoon = round((3.844 * k / scale), 2)
print("If your size of Earth is:", earth,"cm","your size Moon is", moon,
      "cm, and distance between them is :", dearthmoon, "m")
dissunmercury = round(57.91 * k / scale, 2)
dissunvenus = round(108 * k / scale, 2)
dissunearth = round(149.6 * k / scale, 2)
dissunmars = round(228 * k / scale, 2)
dissunjupiter = round(778.5 * k / scale, 2)
dissunsaturn = round(1430 * k / scale, 2)
dissunuranus = round(2800 * k / scale, 2)
dissunneptune = round(4550 * k / scale, 2)

dmercuryvenus = round((dissunvenus - dissunmercury + mercury / 100), 2)
dvenusearth = round((dissunearth - dissunvenus + venus / 100), 2)
dearthmars = round((dissunmars - dissunearth + earth / 100), 2)
dmarsjupiter = round((dissunjupiter - dissunmars + mars / 100), 2)
djupitersaturn = round((dissunsaturn - dissunjupiter + jupiter / 100), 2)
dsaturnuranus = round((dissunuranus - dissunsaturn + saturn / 100), 2)
duranusneptune = round((dissunneptune - dissunuranus + uranus / 100), 2)

print("Distance from Sun to Earth is : ",dissunearth,'m')
print("\nPlanets name and size\n")
print("1. Mercury - " + str(mercury) + " cm")
print("2. Venus - " + str(venus) + " cm")
print("3. Earth - " + str(earth) + " cm")
print("4. Mars - " + str(mars) + "cm")
print("5. Jupiter - " + str(jupiter) + " cm")
print("6. Saturn - " + str(saturn) + " cm")
print("7. Uranus - " + str(uranus) + " cm")
print("8. Neptune - " + str(neptune) + " cm")

print("        )")
print("  Sun    )")
print(round(sun/100,2),"m","  )",dissunmercury,"m", "( 1 )", dmercuryvenus,"m", "( 2 )",dvenusearth,"m","( 3 )",
      dearthmars,"m", "( 4 )", dmarsjupiter,"m", "( 5 )",djupitersaturn,"m","( 6 )", dsaturnuranus,"m", "( 7 )",
      duranusneptune,"m","( 8 )","Total:",round(dissunneptune+(neptune/100)+1,0),"m",)
print("         )")
print("        )")


