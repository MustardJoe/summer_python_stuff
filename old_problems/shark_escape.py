def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
  makeit, die = "Alive", "Shark Bait!"
  if ((pontoon_distance / you_speed) < (shark_distance / shark_speed)):
    print(makeit)
    return makeit
  elif ((pontoon_distance / you_speed) < ((shark_distance * 2) / shark_speed) and dolphin == True):
        print(makeit)
        return makeit
  print(die)
  return die