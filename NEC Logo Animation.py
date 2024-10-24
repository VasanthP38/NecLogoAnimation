import turtle as n
n.speed(2)#2
n.width(2)
n.hideturtle()
#Eagle head
n.color("blue")
n.penup()
n.goto(12,53)#Neck line

n.pendown()

n.goto(-12,53)#Neck line

#Curve of neck right to left 
n.goto(-12,53)
n.goto(-13,55)
n.goto(-14,57)
n.goto(-16,60)
n.goto(-18,62)
n.goto(-20,63)
n.goto(-22,64)
n.goto(-24,64)
n.goto(-26,64)

#Curve left to right
n.goto(-26,64)
n.goto(-26,64)
n.goto(-26,65)
n.goto(-26,66)
n.goto(-25,67)
n.goto(-23,68)
n.goto(-21,69)
n.goto(-19,69)
n.goto(-18,69)

n.goto(-17,71)
n.goto(-16,72)
n.goto(-14,73)
n.goto(-13,74)
n.goto(-12,74)
n.goto(-11,74)
n.goto(-10,75)
n.goto(-9,75)
n.goto(-8,75)
n.goto(-7,75)
n.goto(-6,75)
n.goto(-5,75)
n.goto(-3,74)
n.goto(-1,74)
n.goto(0,74)
n.goto(1,73)
n.goto(2,73)
n.goto(3,72)
n.goto(4,72)
n.goto(5,71)
n.goto(6,71)
n.goto(7,70)
n.goto(8,68)
n.goto(9,67)
n.goto(10,65)
n.goto(10,64)
n.goto(11,62)
n.goto(11,60)
n.goto(12,53)



n.begin_fill()
n.color("blue")

n.penup()
n.goto(-10,65)
n.pendown()


n.circle(2)

n.end_fill()


#Eagle Diamond
n.penup()
n.goto(0,0)
n.pendown()
##########
n.width(2)


n.begin_fill()
n.color("blue")
n.penup()
n.goto(-14,47)
n.pendown()

n.goto(14,47)
n.goto(40,33)
n.goto(0,0)
n.goto(-40,33)
n.goto(-14,47)
n.end_fill()

n.width(1)
n.color("blue")

#Completion of Diamond

#Wings
#Right Wing
n.begin_fill()

n.color("blue")
n.width(1)

n.penup()
n.goto(20,10)
n.pendown()

n.goto(48,33)
n.goto(25,48)
n.goto(40,59)
n.goto(42,60)
n.goto(45,62)
n.goto(47,63)
n.goto(49,64)
n.goto(51,64)
n.goto(53,65)
n.goto(55,65)
n.goto(57,64)
n.goto(60,63)
n.goto(61,63)
n.goto(62,62)
n.goto(63,62)
n.goto(65,61)

n.goto(147,17)
n.goto(138,16)#Wing down

n.goto(76,48)#65#75
n.goto(72,45)

n.goto(129,16)
n.goto(120,15)#Wing down

n.goto(68,42)
n.goto(64,39)

n.goto(111,15)
n.goto(102,14)#Wing down

n.goto(60,36)
n.goto(56,33)

n.goto(93,14)
n.goto(84,13)#Wing down

n.goto(52,30)
n.goto(48,27)

n.goto(75,13)
n.goto(66,12)#Wing down

n.goto(44,24)
n.goto(40,21)

n.goto(57,12)
n.goto(48,11)#Wing down

n.goto(36,18)
n.goto(32,15)#42#17

n.goto(39,11)
n.goto(20,10)#Wing down

n.end_fill()
######

n.begin_fill()

n.color('blue')

n.penup()
n.goto(-20,10)
n.pendown()

n.goto(-48,33)
n.goto(-25,48)
n.goto(-40,59)
n.goto(-42,60)
n.goto(-45,62)
n.goto(-47,63)
n.goto(-49,64)
n.goto(-51,64)
n.goto(-53,65)
n.goto(-55,65)
n.goto(-57,64)
n.goto(-60,63)
n.goto(-61,63)
n.goto(-62,62)
n.goto(-63,62)
n.goto(-65,61)

n.goto(-147,17)
n.goto(-138,16)#Wing down

n.goto(-76,48)#65#75
n.goto(-72,45)

n.goto(-129,16)
n.goto(-120,15)#Wing down

n.goto(-68,42)
n.goto(-64,39)

n.goto(-111,15)
n.goto(-102,14)#Wing down

n.goto(-60,36)
n.goto(-56,33)

n.goto(-93,14)
n.goto(-84,13)#Wing down

n.goto(-52,30)
n.goto(-48,27)

n.goto(-75,13)
n.goto(-66,12)#Wing down

n.goto(-44,24)
n.goto(-40,21)

n.goto(-57,12)
n.goto(-48,11)#Wing down

n.goto(-36,18)
n.goto(-32,15)#42#17

n.goto(-39,11)
n.goto(-20,10)#Wing down

n.end_fill()

#Completion of left wing


#TEXT inside Diamond
n.width(1)
n.begin_fill()
n.color("white")

#N
n.penup()
n.goto(-23,42)
n.pendown()

n.goto(-23,23)
n.goto(-19,19)#16
n.goto(-20,35)#16
n.goto(-13,14)#10
n.goto(-9,10)#4
n.goto(-9,43)#4
n.goto(-13,43)#12
n.goto(-13,22)#12
n.goto(-19,43)#16
n.goto(-23,42)#22
n.end_fill()

#E
n.width(1)
n.color("blue")
n.begin_fill()
n.color("white")
n.penup()
n.goto(-5,43)
n.pendown()

n.goto(-5,8)
n.goto(-2,7)
n.goto(1,7)
n.goto(2,7)
n.goto(7,10)
n.goto(7,15)
n.goto(0,12)
n.goto(0,21)
n.goto(7,23)
n.goto(7,28)
n.goto(0,26)
n.goto(0,37)
n.goto(7,37)
n.goto(7,43)
n.goto(-5,43)
n.end_fill()

#C
n.begin_fill()
n.penup()
n.goto(11,40)
n.pendown()
n.goto(10,35)
n.goto(10,27)
n.goto(10,17)
n.goto(11,15)
n.goto(12,14)
n.goto(14,14)
n.goto(20,19)
n.goto(23,28)
n.goto(18,25)
n.goto(18,20)
n.goto(14,18)
n.goto(14,36)
n.goto(18,37)
n.goto(20,34)#18
n.goto(20,34)
n.goto(22,35)
n.goto(22,39)
n.goto(19,42)
n.goto(18,43)
n.goto(14,43)
n.goto(11,40)
n.end_fill()
#Completion of text inside diamond

#Outline
n.color("blue")
n.width(5)
n.penup()
n.goto(0,0)
n.pendown()
n.goto(200,0)
n.goto(-200,0)
n.goto(-200,-50)
n.goto(200,-50)
n.goto(200,0)
n.goto(200,20)
n.goto(200,-80)
n.goto(200,-50)
n.goto(-200,-50)
n.goto(-200,-80)
n.goto(-200,20)
n.goto(-100,110)

n.goto(100,110)
n.goto(200,20)
n.goto(200,-80)
n.goto(100,-170)
n.goto(-100,-170)
n.goto(-200,-80)

n.penup()
n.goto(-170,-65)
n.pendown()

n.begin_fill()
n.color("blue")
n.goto(170,-65)
n.goto(90,-130)
n.goto(-90,-130)
n.goto(-170,-65)
n.end_fill()

n.penup()
n.goto(-115.5,-80)
n.pendown()

n.color("white")
n.width(2)
n.goto(-82.5,-80)
n.goto(-82.5,-110)
n.goto(-49.5,-110)
n.goto(-49.5,-80)
n.goto(-16.5,-80)
n.goto(-16.5,-110)
n.goto(16.5,-110)
n.goto(16.5,-80)
n.goto(49.5,-80)
n.goto(49.5,-110)
n.goto(82.5,-110)
n.goto(82.5,-80)
n.goto(115.5,-80)

#TEXT
n.penup()
n.goto(0,-40)#-45
n.pendown()

n.color('blue')
style=('', 17,'bold')#25Tw Cen MT Condensed
n.write('NANDHA ENGINEERING COLLEGE', font=style,align='center')




n.hideturtle()

#LEARN
n.begin_fill()
n.color("blue")
n.width(1)
#L
n.penup()
n.goto(-162,-81)
n.pendown()

n.goto(-172,-92)
n.goto(-164,-99)
n.goto(-162,-97)
n.goto(-167,-92)
n.goto(-159,-83)
n.goto(-162,-81)
n.end_fill()

#E
n.begin_fill()
n.color("blue")
n.penup()
n.goto(-153,-89)
n.pendown()

n.goto(-163,-100)
n.goto(-155.6,-107)
n.goto(-153.4,-104.6)
n.goto(-158,-100)
n.goto(-156.5,-98.5)
n.goto(-152,-102)
n.goto(-150,-100)
n.goto(-154.3,-96)
n.goto(-152.7,-94.3)
n.goto(-148,-98)
n.goto(-145.5,-96)
n.goto(-153,-89)
n.end_fill()

#A

n.begin_fill()
n.color("blue")
n.penup()
n.goto(-140.4,-100.6)
n.pendown()

n.goto(-154,-108)
n.goto(-151,-111)
n.goto(-149,-109.5)
n.goto(-145,-113)
n.goto(-146,-115)
n.goto(-143,-117.7)
n.goto(-137,-104)
n.goto(-140.4,-100.6)
n.end_fill()

n.begin_fill()
n.color("white")
n.penup()
n.goto(-141,-104.6)
n.pendown()
n.goto(-146,-107.7)
n.goto(-143.7,-109.7)
n.end_fill()

#R
n.begin_fill()
n.color("blue")
n.penup()
n.goto(-132,-108)
n.pendown()

n.goto(-142,-119)
n.goto(-140,-122)
n.goto(-135.7,-118)
n.goto(-134,-119)
n.goto(-135.7,-125)
n.goto(-132.7,-128 )
n.goto(-131.3,-121.4)
n.goto(-130,-122)
n.goto(-128,-121.3)
n.goto(-126,-119.3)
n.goto(-125.4,-117.5)
n.goto(-125.4,-113.7)
n.goto(-126.4,-112)
n.goto(-132,-108)
n.end_fill()

n.begin_fill()
n.color("white")
n.penup()
n.goto(-131.5,-113)
n.pendown()

n.goto(-133.3,-115)
n.goto(-132.5,-116.7)
n.goto(-131,-117)
n.goto(-130.7,-117)
n.goto(-130,-116.8)
n.goto(-129.4,-116)
n.goto(-129.2,-115.7)
n.goto(-129.2,-115.2)
n.goto(-129.7,-115)
n.goto(-130,-114.4)
n.goto(-131.5,-113)
n.end_fill()

#N

n.begin_fill()
n.color("blue")

n.penup()
n.goto(-121,-118)
n.pendown()

n.goto(-130.7,-129)
n.goto(-128.4,-131.6)
n.goto(-122.5,-125.6)
n.goto(-124,-135.3)
n.goto(-121.6,-137.5)
n.goto(-111.5,-126.5)
n.goto(-114.3,-124.3)
n.goto(-120,-130)
n.goto(-118.3,-121)
n.goto(-121,-118)
n.end_fill()


#SERVE
#S

n.begin_fill()
n.color("blue")
n.penup()
n.goto(-23.5,-142)
n.pendown()

n.goto(-26.6,-141)
n.goto(-29.4,-141)
n.goto(-32.3,-142)
n.goto(-32,-143)
n.goto(-33,-145)
n.goto(-33,-147)
n.goto(-31.6,-149)
n.goto(-29.4,-150)
n.goto(-27.3,-150.6)
n.goto(-26.4,-152)
n.goto(-27.7,-153)
n.goto(-29.7,-153)
n.goto(-32.6,-152)
n.goto(-32.6,-156)
n.goto(-29,-157)
n.goto(-26,-156.6)
n.goto(-23.5,-155)
n.goto(-22.6,-152.6)
n.goto(-23,-149.5)
n.goto(-25,-147.5)
n.goto(-27.5,-146.7)
n.goto(-29.5,-146)
n.goto(-29,-145.3)
n.goto(-27.5,-144.5)
n.goto(-26,-145)
n.goto(-25.5,-145.3)
n.goto(-23.5,-146)
n.goto(-23.5,-142)
n.end_fill()

    
#E
n.begin_fill()
n.color("blue")
n.penup()
n.goto(-20,-140.5)
n.pendown()

n.goto(-20,-157)
n.goto(-9,-157)
n.goto(-9,-154)
n.goto(-16,-154)
n.goto(-16,-151)
n.goto(-10,-151)
n.goto(-10,-147.5)
n.goto(-16,-147.5)
n.goto(-16,-144.5)
n.goto(-9,-144.5)
n.goto(-9.,-140.5)
n.goto(-20,-140.5)
n.end_fill()

#R
n.begin_fill()
n.color("blue")
n.penup()
n.goto(-6.5,-140.5)
n.pendown()

n.goto(-6.5,-157)
n.goto(-3,-157)
n.goto(-3,-151)
n.goto(-1,-151)
n.goto(2,-156.6)
n.goto(6,-156.6)
n.goto(2.6,-151)
n.goto(4.5,-149)
n.goto(5,-147.5)
n.goto(4.5,-144.5)
n.goto(3,-142.4)

n.goto(0,-140.5)
n.goto(-6.5,-140.5)
n.end_fill()

n.begin_fill()
n.color("white")
n.penup()
n.goto(-2,-145)
n.pendown()
n.goto(-2,-148)
n.goto(0,-148)
n.goto(1,-147.5)
n.goto(1,-146)
n.goto(0,-145.3)
n.goto(-2.7,-145)
n.end_fill()

#V
n.begin_fill()
n.color("blue")
n.penup()
n.goto(6.5,-140.5)
n.pendown()
n.goto(11.4,-156.6)
n.goto(16,-156.6)
n.goto(21,-140.5)
n.goto(17,-140.5)
n.goto(13.6,-152.6)
n.goto(10.5,-140.5)
n.goto(6.5,-140.5)
n.end_fill()

#E
n.begin_fill()
n.color("blue")
n.penup()
n.goto(23,-140.5)
n.pendown()

n.goto(23,-157)
n.goto(34,-157)
n.goto(34,-154)
n.goto(27,-154)
n.goto(27,-151)
n.goto(33,-151)
n.goto(33,-147.5)
n.goto(27,-147.5)
n.goto(27,-144.5)
n.goto(34,-144.5)
n.goto(34.,-140.5)
n.goto(23,-140.5)
n.end_fill()


#SUCCEED
#S
n.begin_fill()
n.color("blue")
n.penup()
n.goto(107.6,-133.7)#115,128
n.pendown()


n.goto(105,-130.7)
n.goto(102.4,-132)
n.goto(100,-133.5)
n.goto(98.7,-136)
n.goto(98.5,-138.4)
n.goto(100,-140.6)
n.goto(102.6,-142)
n.goto(105,-141.7)
n.goto(108,-140.6)
n.goto(109,-140.4)
n.goto(110,-141.4)
n.goto(110,-142.7)
n.goto(107.6,-144)
n.goto(104.4,-145.3)
n.goto(107.4,-149)
n.goto(110.3,-147.3)
n.goto(114,-143.5)
n.goto(114,-141)
n.goto(112,-137)
n.goto(109.3,-136)
n.goto(107,-136.4)
n.goto(104.4,-137.4)
n.goto(102.6,-137)
n.goto(102.4,-136.4)
n.goto(104,-135)
n.goto(108,-133.7)
n.goto(107.6,-133.7)
n.end_fill()

#U
n.begin_fill()
n.color("blue")
n.penup()
n.goto(110.5,-125.6)
n.pendown()
n.goto(107.6,-128)
n.goto(115,-137)
n.goto(117,-138.4)
n.goto(121,-138)
n.goto(124.3,-135.6)
n.goto(125.7,-132.7)
n.goto(125.7,-131)
n.goto(125.3,-129.7)#
n.goto(125.3,-128.7)
n.goto(117.4,-119.9)
n.goto(114,-122.4)
n.goto(121,-131)
n.goto(121,-131.3)
n.goto(121,-132.7)
n.goto(119.6,-134)
n.goto(118,-134)
n.goto(110.5,-125.6)
n.end_fill()

#C
n.begin_fill()
n.color("blue")
n.penup()
n.goto(132.6,-114)
n.goto(130,-110.6)
n.goto(126,-112)
n.goto(124,-114)
n.goto(122,-117)
n.goto(122,-119.5)
n.goto(122.5,-121.6)
n.goto(124.3,-124.6)
n.goto(126,-126.4)
n.goto(128,-127.4)
n.goto(131,-128)
n.goto(134.2,-127)
n.goto(137,-125)
n.goto(138.7,-121.6)
n.goto(135.9,-118)
n.goto(134.6,-121.3)
n.goto(133,-123)
n.goto(131,-124)
n.goto(129.4,-123.6)
n.goto(126.5,-120.5)
n.goto(126,-118.7)
n.goto(127,-116.5)
n.goto(129.4,-115)
n.goto(132.6,-114)
n.end_fill()

#C
n.begin_fill()
n.penup()
n.goto(144.6,-104)
n.pendown()
n.goto(142,-100.6)
n.goto(138,-102.5)
n.goto(135.7,-104.3)
n.goto(134,-106.9)
n.goto(134,-109)
n.goto(134.6,-112)
n.goto(135,-113)
n.goto(137.9,-116.3)
n.goto(141,-117.7)
n.goto(144,-118)
n.goto(147,-116.5)
n.goto(149.5,-114.4)
n.goto(151,-111.6)
n.goto(148,-108)
n.goto(147,-111)
n.goto(145.4,-113)
n.goto(143.6,-114)
n.goto(140.7,-113)
n.goto(139,-111)
n.goto(138,-109)
n.goto(138.7,-107)
n.goto(140.7,-105)
n.goto(144.6,-104)
n.end_fill()

#E
n.begin_fill()
n.color("blue")
n.penup()
n.goto(152.5,-90.3)
n.pendown()
n.goto(144,-97)
n.goto(154.3,-110)
n.goto(163,-102.7)
n.goto(161,-100)
n.goto(155,-104.3)
n.goto(153.5,-102)
n.goto(158.4,-98)
n.goto(156,-95.4)
n.goto(151,-99.4)
n.goto(149.5,-97)
n.goto(154.7,-93)
n.goto(152.5,-90.3)
n.end_fill()

#E
n.begin_fill()
n.color("blue")
n.penup()
n.goto(166,-83)
n.pendown()
n.goto(163.5,-80.5)
n.goto(155,-88)
n.goto(165.7,-100)
n.goto(174,-93)
n.goto(172,-90)
n.goto(166.3,-94.5)
n.goto(164.7,-92.3)
n.goto(170,-88)
n.goto(167.5,-85.6)
n.goto(162.5,-89.5)
n.goto(161,-88)
n.goto(166,-83)
n.end_fill()

#D
n.begin_fill()
n.color("blue")
n.penup()
n.goto(166.7,-78.3)
n.pendown()
n.goto(177.3,-91)
n.goto(184,-86.4)
n.goto(184.6,-83.4)
n.goto(184.6,-79.7)
n.goto(184,-77.5)
n.goto(181.3,-74.4)
n.goto(178.3,-72.6)
n.goto(175.5,-72.6)
n.goto(172,-73.6)
n.goto(166.7,-78.3)
n.end_fill()

n.begin_fill()
n.color("white")
n.penup()
n.goto(172.6,-78.7)
n.pendown()
n.goto(178,-85)
n.goto(180,-83.6)
n.goto(180,-80.5)#180.5
n.goto(179,-79.3)#180
n.goto(178.3,-77.5)
n.goto(176,-76.5)
n.goto(175,-76.7)
n.goto(172.6,-78.7)
n.end_fill()
