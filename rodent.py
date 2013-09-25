# tag number
#tag ID: 1805
#size 
# sightings per month
# is_large (large means > 5 oz)
# is small (small means <  3 oz)
#capture month

class Rodent:
 def __init__(self,tag_id,size):
# inititalise rodent object, we need tag, size etc
  self.tag_id=tag_id
  self.size=size
  self.sightings_per_month={}

 def is_large(self):
  # return true if the size is > 5
  return (self.size > 5)
  pass 
 def is_small(self):
  #return true is size is < 3
  return (self.size < 3)
  pass
 def plot(self):
   # return the letter of the plot at which 
   #this rodent was first captured
  return self.tag_id[0]
  pass
 def capture(self, month):
 #we captured this rodent once in this month
 if month not in self.sightings_per_month:
  self.sightings_per_month[month]=0
 self.sightings_per_months[month] + = 1
 
 pass

#pass means do nothing
 
