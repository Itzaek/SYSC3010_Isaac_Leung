import sense_hat

"""

  Lab 2: Changes my initials (I,L) whenever an arrow key is pressed
  
"""

sense = sense_hat.SenseHat()

Y = (255, 255, 0)
G = (0, 255, 0)
B = (0, 0, 255)
X = (0, 0, 0)

toggle = False

firstname = [
    Y, Y, Y, Y, Y, Y, Y, Y,
    X, X, X, Y, Y, X, X, X,
    X, X, X, Y, Y, X, X, X,
    X, X, X, Y, Y, X, X, X,
    X, X, X, Y, Y, X, X, X,
    X, X, X, Y, Y, X, X, X,
    X, X, X, Y, Y, X, X, X,
    Y, Y, Y, Y, Y, Y, Y, Y
]

lastname = [
    Y, X, X, X, X, X, X, X,
    Y, X, X, X, X, X, X, X,
    Y, X, X, X, X, X, X, X,
    Y, X, X, X, X, X, X, X,
    Y, X, X, X, X, X, X, X,
    Y, X, X, X, X, X, X, X,
    Y, X, X, X, X, X, X, X,
    Y, Y, Y, Y, Y, Y, Y, Y
]

reset = [
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X,
    X, X, X, X, X, X, X, X
]

sense.set_pixels(reset)

while True:
    events = sense.stick.get_events()
    if events:
      for event in events:
        if event.action != 'pressed':
            #this is a hold or keyup; move on
            continue
        if(toggle):
          sense.set_pixels(firstname)
          toggle = False
        else:
          sense.set_pixels(lastname)
          toggle = True
