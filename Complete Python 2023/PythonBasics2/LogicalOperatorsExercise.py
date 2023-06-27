is_magician = True
is_expert = True


# Check if magician AND expert.
# True: "You are a master magician"
if is_magician and is_expert:
  print("You are a master magician")

# Check if magician but not expert
# True: "At least you're getting there"
elif is_magician and not is_expert:
  print("At least you're getting there")

# Check if not magician
# True: "Well you need magic"
elif not is_magician:
  print("You need magic powers")